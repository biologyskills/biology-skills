# Skills

Biology Skills uses a small number of broad domain skills so AI agents can activate the relevant biological guidance reliably without loading every topic into context.

Each domain contains:

- `SKILL.md` for cross-cutting rules, AI behaviour, and routing
- `references/` for focused expert guidance on individual biological or computational topics

The broad skill tells an agent **what kinds of assumptions must be checked**. Reference pages provide the detailed rules needed when a particular topic matters.

## Available skills

### [`biology-core`](biology-core/)

Foundational biological reasoning that applies across domains.

Covers:

- biological and experimental context
- evidence and claim strength
- observation versus prediction and inference
- association, mechanism, and causality
- model outputs and uncertainty
- identifiers, namespaces, versions, and provenance
- ambiguity and interpretation boundaries

Use `biology-core` whenever omitted context, provenance, evidence type, uncertainty, or inference level could materially change a biological conclusion.

Core question:

> **What does the available biological evidence actually justify claiming?**

Current references:

- biological context
- evidence and claims
- identifiers and provenance

---

### [`bioinformatics`](bioinformatics/)

Computational correctness as biological data move between files, tools, workflows, evidence systems, and reports.

The skill focuses on preserving:

- **identity** — what biological or computational object is represented
- **lineage** — where it came from and what produced it
- **semantics** — what a file, field, metric, or evidence value means
- **interoperability** — whether the next system can interpret it correctly

Covers:

- subject, sample, library, run, lane, file, and derived-data identity
- experimental and computational metadata
- data and sample provenance
- file identity and checksums
- input/output conventions
- QC outputs and sample-name resolution
- downstream file discovery and parser expectations
- MultiQC interoperability
- evidence availability and rule-based evidence exchange
- Qualifying Evidence Matrix (QEM) semantics
- preservation of raw versus reduced evidence representations

Use `bioinformatics` whenever computational handling can change or obscure biological identity, provenance, meaning, evidence availability, or interoperability.

Core question:

> **Has biological identity and computational meaning survived the workflow?**

Current references:

- QC outputs and sample identity
- metadata and provenance
- qualifying evidence

---

### [`genomics`](genomics/)

Biological and computational correctness for genomic data, variant analysis, interpretation, and reporting.

Covers:

- genome organisation
- reference genomes and exact reference identity
- FASTA and reference sequence files
- FASTQ and sequencing quality
- SAM, BAM, CRAM, and alignment indexes
- genomic intervals and coordinate conventions
- VCF, BCF, gVCF, and variant indexes
- variant representation and normalisation
- contextual and versioned variant qualification
- Qualifying Variant Set Standard (QVSS)
- HGVS variant nomenclature
- transcripts and isoforms
- coding and protein consequences
- inheritance, phase, segregation, and mosaicism
- gene expression and regulatory context

Use `genomics` whenever reference sequences, coordinates, file semantics, variants, selection criteria, transcripts, genotypes, inheritance, or genomic interpretation affect correctness.

Core question:

> **What genomic object is actually being described, and under which reference, representation, selection, and biological context?**

Current references:

- genome organisation
- reference genomes
- reference sequence files
- sequencing reads and quality
- alignment files and indexes
- genomic intervals
- variant call files and indexes
- variant representation
- qualifying variants
- variant nomenclature
- transcripts
- coding sequence and protein consequences
- inheritance and phase
- gene expression

---

### [`quinary-inference`](quinary-inference/)

Inference about how strongly the complete biological or genotype-phenotype explanation is supported.

Quinary inference operates above individual variant calling and variant interpretation. Its inferential unit is a sufficiently specified explanatory hypothesis, which may involve one variant, a genotype, phased alleles, a structural event, mosaicism, a multilocus configuration, or another complete causal account.

Covers:

- explanatory hypothesis definition
- causal scope
- prior plausibility, likelihood, and posterior support
- resolved negative versus unresolved evidence
- observed and potentially unobserved causal events
- competing and residual explanations
- appropriate hypothesis spaces
- measurement limitations
- versioned reference models
- separation of causal truth, posterior belief, interpretation, and reported decisions

Use `quinary-inference` when the question moves beyond:

> *What finding is present and what does it mean?*

to:

> **How strongly does the available evidence support the full causal explanation?**

Current reference:

- explanatory hypotheses and posterior support

## Important distinctions

Several concepts in Biology Skills deliberately occupy different domains.

### Qualifying variants versus qualifying evidence

**Qualifying variants** asks:

> Does this genomic variant satisfy the declared criteria for this genomic analysis?

It belongs to `genomics`.

A variant can qualify under one QV set and not qualify under another. Qualification is contextual and does not itself imply pathogenicity, causality, statistical significance, reportability, or clinical action.

**Qualifying evidence** asks:

> Is verifiable evidence available under the declared evidence rule?

It belongs to `bioinformatics`.

An evidence-availability representation does not itself establish pathogenicity, causality, diagnostic correctness, or posterior probability.

### Evidence versus causal inference

Qualifying evidence can provide an explicit evidence layer.

Quinary inference can use evidence as input to reasoning about an explanatory hypothesis.

These layers should not be collapsed:

```text
biological observations and data
          ↓
domain-specific interpretation
          ↓
explicit qualifying evidence
          ↓
causal / quinary inference
          ↓
report or decision
````

Each transition introduces additional assumptions.

## Using skills together

Skills are designed to compose.

`biology-core` provides the general reasoning foundation. `bioinformatics` protects identity, provenance, semantics, and interoperability. `genomics` provides genomic constraints. `quinary-inference` addresses support for the complete causal explanation.

For example, a clinical variant analysis might require:

```text
biology-core
  → What does the evidence justify claiming?

bioinformatics
  → Are sample identity, provenance, metadata, and evidence semantics preserved?

genomics
  → What reference, allele, qualification criteria, transcript, genotype, and phase define the finding?

quinary-inference
  → How strongly does the complete genotype-phenotype explanation follow from the available and unresolved evidence?
```

Another workflow may need only one or two of these skills.

Agents should load the broad skill needed to recognise the relevant constraints, then read only the reference pages required by the task.

The goal is not to load every biological fact into context.

The goal is to ensure that an AI **does not skip the biological or computational conditions required for a scientifically valid conclusion**.

