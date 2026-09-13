# Biology Skills

**Biological operating rules for AI agents.**

Biology Skills is an open-source collection of concise [Agent Skills](https://agentskills.io/) for biologically correct AI work. It helps agents preserve reference systems, provenance, experimental context, inheritance logic, and inference boundaries that are easy to lose in simplified interfaces or model outputs.

Website: https://biologyskills.com

## Quick start

```bash
git clone https://github.com/biologyskills/biology-skills.git
```

Use:

- [`skills/biology-core/`](skills/biology-core/) for general biological reasoning
- [`skills/genomics/`](skills/genomics/) for genomic coordinates, variants, transcripts, inheritance, phase, and expression

Install or expose those directories using the Agent Skills mechanism supported by your AI client. See [`INSTALL.md`](INSTALL.md).

## Browse

### Biology core

- [Biological context](skills/biology-core/references/biological-context.md)
- [Evidence and claims](skills/biology-core/references/evidence-and-claims.md)
- [Identifiers and provenance](skills/biology-core/references/identifiers-and-provenance.md)

### Genomics

- [Genome organisation](skills/genomics/references/genome-organisation.md)
- [Reference genomes](skills/genomics/references/reference-genomes.md)
- [Reference sequence files](skills/genomics/references/reference-sequence-files.md)
- [Sequencing reads and quality](skills/genomics/references/sequencing-reads-and-quality.md)
- [Alignment files and indexes](skills/genomics/references/alignment-files-and-indexes.md)
- [Genomic intervals](skills/genomics/references/genomic-intervals.md)
- [Variant call files and indexes](skills/genomics/references/variant-call-files-and-indexes.md)
- [Variant representation](skills/genomics/references/variant-representation.md)
- [Transcripts](skills/genomics/references/transcripts.md)
- [Coding sequence and protein consequences](skills/genomics/references/coding-sequence-and-protein-consequences.md)
- [Inheritance and phase](skills/genomics/references/inheritance-and-phase.md)
- [Gene expression](skills/genomics/references/gene-expression.md)

## Why this exists

A genomic coordinate can be meaningless without its reference. A protein consequence can change with the transcript. Two heterozygous variants are not automatically in trans. A model rank is not automatically a probability. Expression is not a context-free property of a gene.

These details are often treated as secondary metadata even when they change the biological conclusion. Biology Skills makes them explicit as compact rules that an AI agent can apply during analysis, coding, interpretation, and presentation.

## What belongs here

Biology Skills contains:

- biological distinctions that materially affect correctness
- the minimum context an agent should preserve or recover
- common failure modes in computational and AI-assisted biology
- operational instructions for agent behaviour
- links to authoritative standards where exact nomenclature or syntax already has an owner

It is not a replacement for HGVS, GA4GH, VCF, MANE, HGNC, NCBI, professional guidelines, databases, or primary literature. Where a maintained authority exists, Biology Skills explains when it matters and points to it rather than creating a competing local standard.

## Format

Each domain is an installable skill:

```text
skills/
  biology-core/
    SKILL.md
    references/
  genomics/
    SKILL.md
    references/
```

`SKILL.md` stays short and operational. Detailed topics live under `references/` and are read only when relevant.

Every reference topic uses the same structure:

```text
Summary
Core rules
Required context
AI behaviour
Common failure modes
Authoritative standards
Examples
Sources
```

Short, standard, and complete copies are generated from these canonical files rather than maintained separately.

```bash
python scripts/validate.py
python scripts/export.py
python -m unittest discover -s tests
```

Generated output is written to `build/` and is not committed.

## Scientific review

Every topic has an explicit status:

- `draft`: open working content
- `reviewed`: reviewed by an appropriate domain expert
- `verified`: independently reviewed by at least two appropriate experts and supported by relevant evaluations
- `consensus`: stable guidance grounded in an established standard or broad expert consensus

The initial public release starts conservatively at `draft`. Review status changes through public pull requests so the review record remains inspectable.

See [`SOURCE_POLICY.md`](SOURCE_POLICY.md), [`STYLE_GUIDE.md`](STYLE_GUIDE.md), and [`GOVERNANCE.md`](GOVERNANCE.md).

## Contributing

Small, precise contributions are preferred. A useful pull request usually does one of four things:

- corrects a biological rule
- adds missing context or a failure mode
- improves an authoritative source
- adds an evaluation for an AI behaviour that should or should not occur

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Stewardship

Biology Skills is an independent open-source project initiated and maintained by [Switzerland Omics](https://switzerlandomics.ch/). Scientific contribution and maintainership are open to the wider biology and AI communities.

## Licence

Apache License 2.0. See [`LICENSE`](LICENSE).
