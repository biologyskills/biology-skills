---
id: genomics.qualifying-variants
title: Qualifying variants
domain: genomics
status: draft
---

# Qualifying variants

## Summary

A **qualifying variant** is a variant that satisfies a declared qualification rule under a defined genomic analysis context.

Qualification is not an intrinsic property of a variant.

The same variant can qualify under one analysis specification and not qualify under another because the purpose, inputs, thresholds, reference resources, or required evidence differ.

A **qualifying variant set (QV set)** makes these criteria explicit as a structured, versioned specification rather than leaving them embedded inside pipeline code.

This is important because variant-selection criteria are part of the scientific method. They determine which genomic records enter subsequent QC, association testing, interpretation, review, or reporting workflows.

The Qualifying Variant Set Standard (QVSS) defines a minimal interoperable representation for these criteria.

## Core rules

- Treat variant qualification as contextual, not intrinsic.
- A variant qualifies only relative to a declared QV set, version, application context, input data, and evaluation.
- Make thresholds, logical conditions, resources, and missing-value behaviour explicit when they determine variant qualification.
- Do not hide scientifically consequential selection criteria only inside scripts, command-line arguments, notebooks, or undocumented pipeline defaults.
- Distinguish a QV set from the software that evaluates it. The specification defines criteria; an implementation executes them.
- Distinguish individual rule outcomes from final set-level qualification.
- Do not call a variant a qualifying variant unless a set-level qualification rule is defined and satisfied.
- Do not equate qualification with retention, exclusion, prioritisation, pathogenicity, reportability, statistical significance, causality, or clinical action.
- Preserve the semantics and provenance of fields used by qualification rules.
- Preserve reference genome, coordinate, transcript, interval, annotation, population, or external-resource identity whenever these affect rule evaluation.
- Handle missing values explicitly. Do not silently convert missing or unresolved values into pass or fail.
- Preserve unknown outcomes rather than forcing binary results when the declared evidence is insufficient.
- Do not silently coerce incompatible datatypes or reinterpret field values.
- Use explicit profiles or extensions when a rule requires semantics beyond simple deterministic comparisons.
- Preserve stable QV-set identifiers, versions, rule identifiers, and relevant checksums.
- Treat any change to normative qualification logic as a new QV-set version.
- Record which QV set was actually applied to an analysis.

## Qualification is contextual

Consider a variant with population allele frequency:

```text
AF = 0.02
````

An illustrative common-variant study might define:

```text
AF >= 0.01
```

and the variant could qualify.

A rare-disease candidate set might instead require:

```text
AF < 0.001
```

and the same variant would not qualify.

Nothing about the underlying variant changed.

The qualification context changed.

Therefore avoid statements such as:

```text
This is a qualifying variant.
```

without enough context to answer:

```text
Qualifying under which QV set?
Which version?
For what analysis?
Using which inputs and resources?
```

## QV set, rule outcome, and qualifying variant

Keep three concepts separate.

### QV set

A structured, versioned specification containing the rules used to evaluate variants.

Conceptually:

```text
QV set
├── identity and version
├── application context
├── declared inputs
├── rules
├── resources
├── missing-value behaviour
├── profiles / extensions where required
└── optional qualification rule
```

### Rule outcome

The result of evaluating an individual rule.

For example:

```text
minimum_depth = satisfied
population_frequency = not_satisfied
panel_overlap = unknown
```

A rule outcome does not automatically determine whether the variant qualifies.

### Qualifying variant

A variant satisfies the QV set's declared final qualification rule under the actual application context.

If the QV set does not define a final qualification rule, it may produce rule outcomes without defining a single binary qualifying status.

Do not invent a final qualifying state from individual rules when the specification does not define one.

## Criteria are scientific parameters

Selection criteria can alter the population of variants entering every downstream analysis.

Examples include:

* variant or genotype quality
* read depth
* call rate
* allele frequency
* Hardy-Weinberg thresholds
* genomic-region overlap
* gene-panel membership
* consequence annotations
* database flags
* inheritance-related predicates
* structural-variant properties
* previously computed annotations or model outputs

These values should not be treated as incidental software settings when changing them can alter the scientific result.

A workflow such as:

```text
bcftools view ...
```

or:

```text
plink --maf 0.01 ...
```

does not by itself provide a durable scientific specification unless the relevant qualification logic and context remain recoverable.

## Field semantics

A field name is not necessarily a complete definition.

### Ambiguous depth

This rule is under-specified:

```text
DP >= 10
```

because `DP` could refer to:

```text
site-level INFO/DP
sample-level FORMAT/DP
derived depth
a particular member of a family
another implementation-specific field
```

Prefer an explicitly defined input whose source and scope are known.

### Ambiguous allele frequency

This rule is under-specified:

```text
AF < 0.01
```

unless the analysis establishes what `AF` represents.

Relevant distinctions may include:

```text
cohort allele frequency
global reference-population frequency
population-specific frequency
maximum population frequency
allele count-derived estimate
another defined source
```

The threshold and the quantity being thresholded are both part of the scientific rule.

### Ambiguous interval overlap

This rule is incomplete:

```text
variant overlaps disease_panel.bed
```

if the following are unknown:

```text
reference assembly
coordinate convention
interval semantics
minimum required overlap
panel release
resource checksum or immutable identity
```

Use the relevant genomic-reference and interval rules before treating the overlap as reproducible.

## Missing values and unknown outcomes

Missing information is not automatically failure and is not automatically success.

A QV rule should declare what happens when a required field is missing.

Possible behaviours can include:

```text
fail
pass
unknown
error
```

When no missing-value behaviour is declared under QVSS core semantics, treat the result as `unknown`.

For example:

```text
rule:
  population_af < 0.001

observed input:
  population_af = missing
```

must not silently become:

```text
population_af = 0
```

and must not automatically imply:

```text
rare variant = true
```

unless the declared rule explicitly defines that behaviour.

Unknown values must also remain unknown through logical operations when the result cannot otherwise be determined.

For example:

```text
not(unknown) = unknown
```

Do not use Boolean coercion that converts unknown evidence into false certainty.

## External resources

Many qualification rules depend on external resources.

Examples include:

```text
gene panels
BED interval sets
population-frequency databases
clinical databases
annotation releases
transcript sets
blacklists
reference genomes
```

The rule:

```text
overlaps current disease panel
```

is not reproducible if "current disease panel" changes over time.

Preserve sufficient resource provenance to identify the resource used during the actual analysis.

Where appropriate, preserve:

```text
resource identifier
version / release
reference assembly
retrieval date
checksum
```

Changing a normative external resource can change qualification even when the visible rule text is unchanged.

## Complex genomic rules

Not every genomic criterion is a simple per-variant comparison.

Examples include:

```text
compound heterozygosity
phase-dependent inheritance
multi-variant genotype configurations
family segregation
grouped variant counts
multi-record structural events
```

Do not reduce these to a misleading atomic expression merely to fit a simple rule format.

If the complex result has already been computed upstream, it can be supplied as an explicitly defined input predicate.

If the computation itself is part of the qualification semantics, use a declared profile or extension that defines the required behaviour.

The implementation must not invent hidden semantics.

## Multi-stage qualification

QV criteria can be applied at several stages of one genomic workflow.

For example:

```text
called variants
      ↓
QV set A: technical quality
      ↓
analysis-ready variants
      ↓
QV set B: study eligibility
      ↓
candidate variants
      ↓
QV set C: disease-specific criteria
      ↓
variants for downstream interpretation
```

A variant can therefore:

```text
qualify under QV set A
```

and:

```text
not qualify under QV set C
```

without inconsistency.

Each statement answers a different genomic question.

Do not collapse sequential QV sets into one unexplained label such as:

```text
filtered variant
```

when the distinction affects reproducibility or interpretation.

## Versioning and audit

A QV set should have stable identity independent of the filename used to store it.

Preserve as applicable:

```text
QVSS version
QV set identifier
QV set version
QV set title
rule identifiers
checksum
declared profiles or extensions
external resource provenance
```

A published QV set should be treated as immutable.

Changing any normative component, including:

```text
threshold
operator
rule statement
logical structure
missing-value behaviour
profile
normative extension
```

creates a different QV-set version.

Do not edit a released QV set in place while retaining the same version.

## QV application record

The specification and its use are separate objects.

A QV application record identifies which specification was actually applied.

Conceptually:

```text
qv_application:
  qv_set_id: rare_disease_candidates
  qv_set_version: 2.1.0
  qvss_version: 1.0
  qv_set_checksum: <digest>
  applied_at: <timestamp>
  implementation:
    name: <software>
    version: <version>
  input_data: <dataset identifier>
```

This record supports questions such as:

```text
Which criteria were applied to this genome?
Which version was used?
Can I retrieve the exact rule set?
Was the same QV set used for another analysis?
```

It does not assert that a resulting variant is pathogenic, causal, reportable, or clinically actionable.

## Relationship to qualifying evidence

Qualifying variants and qualifying evidence solve different problems.

### Qualifying variants

Ask:

> Does this genomic variant satisfy the declared criteria for this analysis context?

Conceptually:

```text
variant
  +
QV set
  ↓
rule outcomes
  ↓
optional qualifying status
```

### Qualifying evidence

Asks:

> Is verifiable evidence available under a declared evidence rule?

Conceptually:

```text
evaluated item
  +
evidence rule
  ↓
raw evidence outcome
  ↓
evidence-availability representation
```

Do not assume the Boolean semantics are interchangeable.

In QVSS, a satisfied rule can be represented as a positive rule outcome.

In QEM, raw `TRUE` is deliberately defined as detection of a contradiction, absence, or weakening signal and therefore maps differently.

Never copy QVSS rule outcomes directly into a QEM matrix without an explicitly defined evidence rule and mapping.

## AI behaviour

Before describing a variant as qualifying:

1. Identify the genomic analysis context.
2. Identify the QV set.
3. Verify the QV-set version.
4. Determine whether the QV set actually defines a final qualification rule.
5. Identify the variant representation and relevant genomic reference.
6. Resolve the declared input fields and their meanings.
7. Check the operators, values, and logical structure.
8. Check the declared missing-value behaviour.
9. Identify external resources and their relevant versions.
10. Determine whether profiles or extensions are required.
11. Evaluate unknown values without silently coercing them.
12. Preserve the resulting rule outcomes separately from downstream interpretation.
13. Record the QV application sufficiently to identify which criteria were actually used.

Do not infer that a variant is:

```text
pathogenic
causal
significant
reportable
actionable
```

merely because it qualifies.

When reproducing an analysis, use the exact declared QV-set version and external resources rather than recreating the criteria from prose or memory.

## Common failure modes

### Qualification treated as an intrinsic variant property

A database field says:

```text
qualifying_variant = true
```

but does not identify the criteria.

The statement is incomplete.

Qualification requires a declared context and QV set.

### Hard-coded scientific criteria

A script contains:

```text
if AF < 0.001 and DP >= 10:
```

but the thresholds are not represented anywhere outside the code.

The software may be reproducible while the scientific selection protocol remains difficult to discover, compare, audit, or reuse.

### Missing value treated as passing

A rare-variant rule requires:

```text
AF < 0.001
```

but `AF` is unavailable.

The system substitutes zero and the variant qualifies.

This converts missing information into evidence of rarity.

### Ambiguous field source

Two implementations evaluate:

```text
DP >= 10
```

One uses `INFO/DP`.

The other uses sample `FORMAT/DP`.

Both claim to implement the same criterion.

They are not necessarily evaluating the same quantity.

### Unversioned gene panel

A QV set says:

```text
overlaps paediatric disease panel
```

but does not identify which release of the panel was used.

The panel changes later.

The analysis can no longer be reconstructed reliably.

### Qualification treated as pathogenicity

A variant satisfies all candidate-selection criteria.

The system reports:

```text
pathogenic variant
```

Qualification only establishes that the declared criteria were satisfied.

Pathogenicity requires a separate interpretive process.

### Qualification treated as an action

A variant satisfies the QV set and is automatically reported clinically.

QVSS qualification does not itself specify whether a variant should be retained, excluded, ranked, interpreted, reported, or acted upon.

### Complex inheritance reduced to a per-variant filter

A compound-heterozygous model requires two variants, phase, and appropriate inheritance context.

The system represents this as:

```text
compound_het = variant_A == true
```

without defining how the pair or phase was established.

Complex multi-record semantics require explicit computation and provenance.

### Released criteria edited in place

A QV set version `1.0.0` changes:

```text
AF < 0.01
```

to:

```text
AF < 0.001
```

without changing its version.

Historical analyses referring to `1.0.0` are now ambiguous.

## Examples

### Example 1: the same variant in different analyses

Suppose:

```text
variant population AF = 0.02
```

An illustrative GWAS QV set requires:

```text
AF >= 0.01
```

Result:

```text
qualifies for this GWAS criterion
```

An illustrative rare-disease QV set requires:

```text
AF < 0.001
```

Result:

```text
does not qualify for this rare-disease criterion
```

The genomic variant has not changed.

The analysis question has.

### Example 2: sequential QV sets

A variant has:

```text
QUAL = 80
sample DP = 35
population AF = 0.005
```

An upstream technical QV set might require:

```text
QUAL >= 30
DP >= 10
```

and the variant qualifies.

A downstream rare-disease QV set might require:

```text
population AF < 0.001
```

and the variant does not qualify.

Do not summarise both results simply as:

```text
variant passed filtering
```

Record which criteria were satisfied at which stage.

### Example 3: missing population frequency

Rule:

```text
population AF < 0.001
missing: unknown
```

Variant:

```text
population AF = missing
```

Result:

```text
rule outcome = unknown
```

not:

```text
rule outcome = true
```

Missing population data are not evidence that the variant is rare.

### Example 4: panel overlap

Rule:

```text
variant overlaps disease panel
```

A reproducible implementation must establish enough context to interpret that statement, including the relevant genomic reference and the identity of the panel resource.

Two analyses using different panel releases can legitimately produce different qualifying sets.

## Authoritative standards

The Qualifying Variant Set Standard (QVSS) defines the normative representation of qualifying variant criteria.

Biology Skills explains the biological and computational distinctions that an AI must preserve when designing or applying such criteria. It does not replace the current QVSS specification.

Use the current QVSS standard for exact:

* required fields
* rule structure
* logical operators
* comparison operators
* datatype behaviour
* missing-value semantics
* three-valued logic
* profile and extension requirements
* conformance requirements
* registry and application-record requirements

QVSS defines how qualification criteria are represented.

It does not establish whether a particular threshold, resource, gene panel, biological assumption, or clinical criterion is scientifically correct.

## Sources

* Lawless D, Saadat A, Ait Oumelloul M, et al. *Application of qualifying variants for genomic analysis.* Bioinformatics. 2026;42(2):btaf676.
  https://doi.org/10.1093/bioinformatics/btaf676
* Swiss Genomics Association. *Qualifying Variant Set Standard.* SGA-QVSS-1.0. 2026.


