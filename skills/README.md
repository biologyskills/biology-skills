# Skills

Biology Skills uses a small number of broad domain skills so AI agents can recognise when expert biological assumptions matter without loading every topic into context.

Each domain contains:

* `SKILL.md` for cross-cutting rules, AI behaviour, and routing
* `references/` for focused expert guidance when a particular issue becomes relevant

The broad skill tells an agent **what it must stop and check**. Reference pages provide the detailed rules needed to resolve that issue.

## Available skills

### [`biology-core`](biology-core/)

Foundational biological reasoning that applies across domains: biological context, measurement, observability, evidence, uncertainty, identifiers, provenance, and valid inference.

Use `biology-core` whenever omitted context or measurement limitations could materially change what the evidence justifies claiming.

Core question:

> **What was actually observed, under what conditions, and what does that evidence justify claiming?**

Reference examples:

* [biological context](biology-core/references/biological-context.md)
* [measurement, observability and negative evidence](biology-core/references/measurement-observability-and-negative-evidence.md)
* [evidence and claims](biology-core/references/evidence-and-claims.md)

---

### [`bioinformatics`](bioinformatics/)

Computational correctness as biological data move between files, tools, workflows, identifier systems, evidence layers, and reports.

The skill protects:

* **identity** — what biological or computational object is represented
* **lineage** — where it came from and what produced it
* **semantics** — what a field, mapping, metric, or evidence value means
* **interoperability** — whether another system can interpret it correctly

Use `bioinformatics` whenever computation can silently change biological identity, multiplicity, provenance, evidence semantics, or meaning.

Core question:

> **Has biological identity and meaning survived the computational transformation?**

Reference examples:

* [metadata and provenance](bioinformatics/references/metadata-and-provenance.md)
* [entity mapping and join cardinality](bioinformatics/references/entity-mapping-and-join-cardinality.md)
* [QC outputs and sample identity](bioinformatics/references/qc-outputs-and-sample-identity.md)

---

### [`genomics`](genomics/)

Biological and computational correctness for genomic references, sequencing data, coordinates, variants, transcripts, inheritance, expression, assay scope, and population-frequency interpretation.

Use `genomics` whenever reference identity, file semantics, variant representation, transcript choice, genotype, phase, callability, or genomic context can change the result.

Core question:

> **What genomic object is actually being described, relative to which reference and under which analytical context?**

Reference examples:

* [reference genomes](genomics/references/reference-genomes.md)
* [variant representation](genomics/references/variant-representation.md)
* [assay scope, callability and negative results](genomics/references/assay-scope-callability-and-negative-results.md)
* [population frequency, denominators and ancestry](genomics/references/population-frequency-denominators-and-ancestry.md)

---

### [`experimental-design`](experimental-design/)

Correctness rules for experimental units, replication, dependence, controls, batch structure, technical confounding, and validation.

Use `experimental-design` whenever the scientific conclusion depends on what was independently sampled, assigned, measured, replicated, or controlled.

Core question:

> **What was genuinely independent, and could the design distinguish the claimed biological effect from its technical alternatives?**

Reference example:

* [experimental unit, replication and pseudoreplication](experimental-design/references/experimental-unit-replication-and-pseudoreplication.md)

---

### [`structural-biology`](structural-biology/)

Correctness rules for protein and residue identity, isoforms, experimental constructs, structure mappings, predicted structures, confidence metrics, assemblies, and molecular state.

Use `structural-biology` whenever residue coordinates, structural models, molecular interactions, or structure-based explanations affect interpretation.

Core question:

> **Which exact molecular object and structural state does this coordinate or model represent?**

Reference examples:

* [residue identity, isoforms and construct mapping](structural-biology/references/residue-identity-isoforms-and-construct-mapping.md)
* [predicted structure confidence and biological state](structural-biology/references/predicted-structure-confidence-and-biological-state.md)

---

### [`biological-statistics`](biological-statistics/)

Statistical reasoning about the processes that generate biological observations: ascertainment, selection, denominators, controls, target populations, dependence, and transportability.

Use `biological-statistics` whenever cohort construction, sampling, missingness, QC, population structure, or dependence can change an estimate or the population to which it applies.

Core question:

> **What process generated these observations, and to which population or biological units does the inference actually apply?**

Reference example:

* [ascertainment, selection and target population](biological-statistics/references/ascertainment-selection-and-target-population.md)

---

### [`synthetic-biology`](synthetic-biology/)

Correctness rules for converting biological observations, predictions, and selected targets into engineered biological sequences or constructs.

Personalised mRNA cancer vaccines are a central example, where patient-specific molecular evidence is transformed through target generation, prediction, selection, sequence design, and construct engineering.

Use `synthetic-biology` whenever source identity, host context, prediction semantics, uncertainty, target dependencies, sequence context, or design provenance can change whether an engineered construct represents the intended biology.

Core question:

> **Does the engineered biological object still represent the source biology and the evidence used to design it?**

Reference examples:

* [neoantigen identity and evidence](synthetic-biology/references/neoantigen-identity-and-evidence.md)
* [HLA presentation and immunogenicity](synthetic-biology/references/hla-presentation-and-immunogenicity.md)
* [target-set selection under uncertainty](synthetic-biology/references/target-set-selection-under-uncertainty.md)
* [mRNA polyepitope construct design](synthetic-biology/references/mrna-polyepitope-construct-design.md)

---

### [`quinary-inference`](quinary-inference/)

Inference about how strongly the available evidence supports a sufficiently specified biological or genotype–phenotype explanation.

Quinary inference operates above individual observations, variant calls, predictions, and interpretations. Its inferential unit can be a variant, genotype, phased allele pair, structural event, mosaic state, multilocus configuration, or another complete explanatory hypothesis.

Use `quinary-inference` when the question moves beyond:

> *What finding is present and what does it mean?*

to:

> **How strongly does the available evidence support the full causal explanation?**

Reference example:

* [explanatory hypotheses and posterior support](quinary-inference/references/explanatory-hypotheses-and-posterior-support.md)

## Important distinctions

Biology Skills deliberately separates concepts that are often collapsed in scientific software or AI-generated reasoning.

### Qualifying variants versus qualifying evidence

**Qualifying variants** asks:

> Does this genomic variant satisfy the declared criteria for this genomic analysis?

It belongs to `genomics`.

Qualification is contextual. It does not itself establish pathogenicity, causality, statistical significance, reportability, or clinical action.

**Qualifying evidence** asks:

> Is verifiable evidence available under the declared evidence rule?

It belongs to `bioinformatics`.

Evidence availability does not itself establish pathogenicity, causal truth, diagnostic correctness, or posterior probability.

### Measurement versus absence

A missing observation, failed measurement, non-detection, uncallable locus, and explicitly established negative result are not interchangeable.

The general rule belongs to `biology-core`. Domain skills then supply the relevant measurement semantics.

For example:

```text
biology-core
  → Was the claimed absence actually observable?

genomics
  → Was this locus and event class callable?
```

### Evidence versus causal inference

Evidence can be represented explicitly before it is used for causal reasoning.

These layers should remain distinct:

```text
biological state
      ↓
measurement
      ↓
observed data
      ↓
computational representation
      ↓
domain-specific interpretation
      ↓
explicit evidence
      ↓
causal / quinary inference
      ↓
report or decision
```

Each transition introduces assumptions that may need their own skill or reference.

## Using skills together

Skills are designed to compose.

A clinical genomic analysis might require:

```text
biology-core
  → What does the evidence justify claiming?

bioinformatics
  → Have identity, provenance, mappings, and evidence semantics been preserved?

genomics
  → What reference, allele, assay scope, transcript, genotype, and phase define the finding?

biological-statistics
  → What selection process and denominator produced the estimate?

quinary-inference
  → How strongly does the complete genotype–phenotype explanation follow from the available and unresolved evidence?
```

A structure-based interpretation might instead require:

```text
biology-core
  → What is observed versus predicted?

genomics
  → Which transcript and protein consequence were derived?

structural-biology
  → Which sequence, residue numbering system, construct, and structural state are being interpreted?
```

Another workflow may need only one or two domains.

Agents should load the broad skill needed to recognise the relevant constraints, then read only the focused reference pages required by the task.

The goal is not to place every biological fact into context.

The goal is to ensure that an AI **does not skip the biological, computational, experimental, or inferential conditions required for a scientifically valid conclusion**.

