# Skills

Biology Skills uses a small number of broad domain skills so AI agents can activate the relevant biological guidance reliably.

Each domain contains:

- `SKILL.md` for cross-cutting rules and routing
- `references/` for focused expert guidance on individual biological or computational topics

## Available skills

### [`biology-core`](biology-core/)

Foundational biological reasoning that applies across domains.

Covers:

- biological and experimental context
- evidence and claim strength
- observation versus prediction and inference
- association, mechanism, and causality
- identifiers, versions, and provenance
- ambiguity and interpretation boundaries

Use `biology-core` whenever omitted context, provenance, evidence type, or inference level could materially change a biological conclusion.

### [`genomics`](genomics/)

Biological and computational correctness for genomic data, analysis, interpretation, and reporting.

Covers:

- genome organisation
- reference genomes and exact reference identity
- FASTA and reference sequence files
- FASTQ and sequencing quality
- SAM, BAM, CRAM, and alignment indexes
- genomic intervals and coordinate conventions
- VCF, BCF, gVCF, and variant indexes
- variant representation and normalisation
- HGVS variant nomenclature
- transcripts and isoforms
- coding and protein consequences
- inheritance, phase, segregation, and mosaicism
- gene expression and regulatory context

Use `genomics` whenever reference sequences, coordinates, file semantics, variants, transcripts, genotypes, inheritance, or genomic interpretation affect correctness.

## Using skills together

`biology-core` provides the general foundation. Domain skills add the rules specific to a field.

For example, a variant-interpretation task may require both:

```text
biology-core
  → What does the evidence justify claiming?

genomics
  → What reference, allele, transcript, phase, and nomenclature define the result?
```

Agents should load only the relevant detailed references for the task rather than treating every topic page as required context.


