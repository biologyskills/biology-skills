---
id: bioinformatics.qualifying-evidence
title: Qualifying evidence
domain: bioinformatics
status: draft
---

# Qualifying evidence

## Summary

Scientific conclusions often depend on many evidence checks performed inside heterogeneous, proprietary, or otherwise non-interoperable analysis systems.

A final result alone does not show which supporting information was actually available, which checks were performed, which checks could not be evaluated, or whether a potential contradiction was detected.

Qualifying evidence makes this evidential layer explicit.

A qualifying-evidence representation records whether predefined, verifiable evidence requirements have been satisfied for an evaluated item under a declared rule set and interpretation context. It allows the evidential basis of a result to be inspected and exchanged independently of the algorithm that originally produced the result.

The Qualifying Evidence Matrix (QEM) standard provides a minimal interoperable representation for this purpose.

Qualifying evidence describes **evidence availability**. It does not by itself establish pathogenicity, causality, diagnostic correctness, or posterior probability.

## Core rules

- Keep evidence availability separate from biological interpretation, pathogenicity, causality, ranking, and decision-making.
- Define evidence checks explicitly rather than relying on undocumented logic embedded inside an analysis pipeline.
- Every evidence rule must have a stable identity and declared semantics.
- Preserve the version of the evidence rule set used for each evaluation.
- Preserve the identity of the evaluated item.
- Preserve raw rule outcomes and their provenance even when a reduced evidence representation is produced.
- Do not infer the meaning of a binary evidence value without knowing the rule and mapping that produced it.
- Distinguish an evaluated contradiction from an unevaluable rule.
- Missing or unavailable information must not increase qualifying evidence.
- Do not interpret absence of qualifying evidence as evidence against a hypothesis without inspecting the underlying raw outcome.
- Do not treat qualifying evidence as a measure of causal probability or pathogenicity.
- Do not assume evidence rules are statistically independent.
- Do not compare evidence counts or profiles produced from materially different rule sets as though they measured the same thing.
- Use registered, versioned, or otherwise reproducibly identifiable rule definitions when evidence must be exchanged across systems or institutions.

## Evidence model

A qualifying-evidence workflow has four distinct components:

```text
evaluated item
      ↓
versioned evidence rule
      ↓
raw rule outcome
      ↓
interoperable evidence representation
````

The evaluated item might be a genomic variant, sample, experimental result, candidate finding, or another uniquely identifiable entity.

The evidence rule defines a specific check.

The raw outcome records what happened when that rule was evaluated.

The reduced evidence representation records whether qualifying evidence is available for downstream use.

Do not collapse these components.

## QEM rule semantics

Under SGA-QEM-1.0, evidence rules are deliberately defined using negative polarity.

A rule is written so that:

```text
TRUE
→ a contradiction, absence, or weakening signal was detected

FALSE
→ no such contradiction or weakening signal was detected

NA
→ the rule could not be evaluated
```

The corresponding binary evidence value is:

| Raw rule outcome | QEM value | Meaning                                                    |
| ---------------- | --------: | ---------------------------------------------------------- |
| `FALSE`          |       `1` | qualifying evidence is present under this rule             |
| `TRUE`           |       `0` | a contradiction, absence, or weakening signal was detected |
| `NA`             |       `0` | the rule could not be evaluated                            |

Formally:

```text
FALSE → 1
TRUE  → 0
NA    → 0
```

This polarity can appear counterintuitive.

Do not reinterpret `TRUE` as “good evidence” merely because the word normally sounds affirmative.

The meaning comes from the rule definition.

## Binary values are deliberately lossy

A QEM value of:

```text
1
```

means that qualifying evidence is present under the corresponding rule.

A value of:

```text
0
```

does not identify a single upstream state.

It may mean:

```text
a contradiction or weakening signal was detected
```

or:

```text
the rule could not be evaluated
```

Therefore:

```text
QEM 0
≠
evidence against
```

without additional information.

The raw tri-state outcome must remain recoverable whenever the distinction between contradiction and missing information matters.

Do not discard the raw outcomes merely because the binary matrix has been generated.

## Required provenance

A qualifying-evidence profile must remain interpretable independently of the system that generated it.

Preserve or reference as applicable:

* evaluated item identifier
* identifier namespace
* evidence rule identifier
* evidence rule definition
* evidence rule-set identifier
* evidence rule-set version
* raw rule outcome
* QEM standard version when QEM is used
* interpretation context required by the rule
* source data or evidence source
* source-data version where material
* evaluation software or process where material
* evaluation time where material

For a QEM instance, stable item and rule identifiers and the applicable versions must permit deterministic reconstruction of the matrix from the raw rule outcomes.

A matrix without identifiable rule semantics is not sufficient for independent interpretation.

## AI behaviour

When generating or interpreting qualifying evidence:

1. Identify the item being evaluated.
2. Identify the evidence rule and its exact semantics.
3. Establish the applicable interpretation context.
4. Identify the rule-set version.
5. Evaluate the rule using the source information available.
6. Preserve the raw result as `TRUE`, `FALSE`, or `NA`.
7. If QEM is being produced, apply the normative mapping exactly:
   `FALSE → 1`, `TRUE → 0`, `NA → 0`.
8. Preserve enough provenance to reconstruct why that outcome occurred.
9. Do not infer pathogenicity, causality, or diagnostic probability from the resulting matrix.
10. If a binary `0` needs interpretation, inspect the raw outcome before describing it as contradictory or missing.
11. If missingness is itself scientifically informative, represent that question using a separate explicit evidence rule.
12. If evidence profiles from different systems are compared, first establish that their rule identities, versions, and interpretation contexts are compatible.

Do not invent an evidence result when the required source information is unavailable. Return `NA` at the raw-rule level when the rule cannot be evaluated.

## Evidence availability is not evidence strength

Suppose an evidence profile contains:

```text
rule_01 = 1
rule_02 = 1
rule_03 = 1
```

This establishes that qualifying evidence is present for those three rules.

It does not establish that:

```text
the hypothesis is 100% supported
```

or:

```text
the evidence has equal statistical weight
```

or:

```text
the evaluated item is causal
```

QEM does not define rule weights and does not assume rule independence.

A downstream statistical or interpretive method may use qualifying evidence, but that is a separate layer and must state its own assumptions.

## Rule design

A rule should answer one clear, verifiable question under a declared context.

Under QEM semantics, formulate the rule so that `TRUE` identifies the contradiction, absence, or weakening condition.

Prefer:

```text
parent_gt_unavailable
```

over:

```text
parent_gt_available
```

if the rule is intended for direct QEM evaluation.

Likewise, a rule checking population-frequency compatibility might be expressed conceptually as:

```text
population_frequency_too_high
```

rather than using an ambiguous positive label such as:

```text
population_frequency_ok
```

Rule names alone are not sufficient, however. The exact definition, threshold, population context, and source must remain specified in the rule set.

## Common failure modes

### TRUE treated as evidence present

A system sees:

```text
parent_gt_unavailable = TRUE
```

and encodes:

```text
QEM = 1
```

because `TRUE` is interpreted as affirmative.

This reverses the QEM semantics.

The correct mapping is:

```text
TRUE → 0
```

because the rule detected unavailable parental information.

### NA treated as successful evidence

A rule cannot be evaluated, but the system treats this as neutral or successful evidence.

Under QEM:

```text
NA → 0
```

Unavailable information does not accrue qualifying evidence.

### Binary zero interpreted as contradiction

A downstream system sees:

```text
QEM = 0
```

and reports:

```text
evidence contradicts the hypothesis
```

This is not justified.

The raw outcome may have been `NA`.

Inspect the raw rule outcome.

### Evidence availability treated as pathogenicity

A variant has qualifying evidence for many checks.

The system concludes:

```text
variant is pathogenic
```

This is invalid.

The evidence profile states which verifiable evidence requirements were satisfied. Pathogenicity requires separate biological interpretation.

### Evidence profile treated as causal probability

A candidate satisfies 18 of 24 evidence rules.

The system reports:

```text
P(causal) = 18 / 24 = 0.75
```

This is invalid unless a separately defined and validated probabilistic model establishes that interpretation.

A proportion of qualifying rules is not inherently a causal probability.

### Rule-set versions compared without reconciliation

Laboratory A evaluates 20 rules.

Laboratory B evaluates 30 different or revised rules.

Their evidence counts are compared directly.

The numbers do not necessarily measure the same evidential space.

Rule identity, semantics, version, and context must be reconciled before comparison.

### Raw evidence discarded after binary conversion

Only the binary matrix is retained.

Later, a `0` cannot be distinguished as:

```text
contradiction
```

versus:

```text
not evaluable
```

The reduction has destroyed information needed for re-interpretation.

Preserve the raw outcomes upstream.

### Correlated rules counted as independent observations

Several rules are derived from the same underlying evidence source and are treated as statistically independent.

QEM does not make this assumption.

Dependencies must be handled by the downstream method if statistical combination is attempted.

## Examples

### Example 1: parental genotype availability

Consider the rule:

```text
parent_gt_unavailable
```

The rule asks whether required parental genotype information is unavailable.

| Situation                                   | Raw outcome | QEM |
| ------------------------------------------- | ----------- | --: |
| required parental genotypes are available   | `FALSE`     | `1` |
| a required parental genotype is unavailable | `TRUE`      | `0` |
| availability cannot be established          | `NA`        | `0` |

This rule answers only an availability question.

It does not establish whether the parental genotypes support the proposed inheritance model.

That requires a separate rule.

### Example 2: inheritance consistency

Consider a separate rule:

```text
inheritance_inconsistent
```

If parental genotypes are available:

```text
genotypes contradict the declared inheritance model
→ TRUE
→ QEM 0
```

```text
no inheritance contradiction detected
→ FALSE
→ QEM 1
```

If the required parental genotypes are unavailable:

```text
rule cannot be evaluated
→ NA
→ QEM 0
```

This illustrates why:

```text
evidence available
```

and:

```text
evidence consistent
```

are different questions and should not be hidden inside one ambiguous flag.

### Example 3: population-frequency evidence

Suppose a rare-disease rule is defined as:

```text
population_frequency_too_high
```

against a declared population resource and threshold.

If the measured frequency exceeds the rule's threshold:

```text
TRUE → QEM 0
```

If adequate population evidence establishes that the threshold is not exceeded:

```text
FALSE → QEM 1
```

If the population resource cannot adequately evaluate the variant:

```text
NA → QEM 0
```

Do not convert lack of population data into:

```text
variant is absent from the population
```

or:

```text
variant is rare
```

without supporting evidence.

### Example 4: opaque candidate-generation pipeline

A proprietary system reports:

```text
candidate: variant_A
rank: 1
```

The ranking algorithm may remain proprietary.

A separate qualifying-evidence profile can still expose whether predefined checks were verifiably evaluated:

```text
population_frequency_too_high       FALSE → 1
parent_gt_unavailable               FALSE → 1
inheritance_inconsistent            FALSE → 1
phenotype_evidence_unavailable      TRUE  → 0
functional_evidence_unavailable     NA    → 0
```

A reviewer can inspect the evidential basis without requiring access to the ranking algorithm.

The evidence profile does not explain why the proprietary system ranked the variant first and does not prove that the candidate is causal.

## Relationship to downstream inference

Qualifying evidence is an input layer.

Conceptually:

```text
domain-specific biological evidence
              ↓
explicit rule evaluation
              ↓
qualifying-evidence representation
              ↓
optional evidence-sufficiency modelling
              ↓
optional causal / quinary inference
              ↓
report or decision
```

Do not collapse these layers.

A downstream evidence-sufficiency model may quantify how complete the verifiable evidence profile is.

A causal inference model may estimate support for an explanatory hypothesis.

Neither quantity is supplied by QEM itself.

## Authoritative standards

The Swiss Genomics Association Qualifying Evidence Matrix standard defines the normative semantics of QEM.

Biology Skills should explain when these distinctions matter and how an AI should preserve them. It should not redefine the QEM mapping or reproduce domain-specific evidence rule sets as though they were universal.

For exact QEM semantics, versioning, and normative requirements, use the current standard.

## Sources

* Swiss Genomics Association. *Qualifying Evidence Matrix standard for verifiable evidence.* SGA-QEM-1.0.
  https://www.swissgenomicsassociation.ch/pages/sga_qem/
* Latest QEM standard:
  https://www.swissgenomicsassociation.ch/assets/release/sga_qem/latest/sga_qem_1.0.pdf
* DOI:
  https://doi.org/10.5281/zenodo.17936587


