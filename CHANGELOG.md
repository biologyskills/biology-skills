# Changelog

## 0.3.0

Expanded Biology Skills with synthetic-biology guidance for personalised mRNA vaccine design.

* Added the `synthetic-biology` Agent Skill for converting biological observations, predictions, and selected targets into engineered biological sequences and constructs.
* Added guidance for patient-specific neoantigen identity, tumour-normal evidence, transcript and haplotype reconstruction, mutant-sequence context, and clonality.
* Added guidance for HLA identity, peptide:HLA prediction, presentation, T-cell recognition, immunogenicity, and the distinction between prediction and experimental evidence.
* Added guidance for finite target-set selection under uncertainty, including candidate-universe definition, score semantics, missing evidence, dependence, redundancy, and set-level constraints.
* Added guidance for mRNA polyepitope construct design, including target order, artificial junction sequences, amino-acid versus nucleotide identity, sequence engineering, and design-to-manufacturing provenance.
* Added explicit distinctions between source biological state, predicted target behaviour, selected vaccine targets, engineered constructs, manufactured products, immune responses, and clinical outcomes.
* Updated skill routing, repository documentation, and website domain listings to include `synthetic-biology`.

## 0.2.0

Expanded Biology Skills with new bioinformatics and causal-inference guidance.

* Added the `bioinformatics` Agent Skill for computational identity, metadata, provenance, interoperability, QC outputs, and evidence exchange.
* Added the `quinary-inference` Agent Skill for reasoning about complete causal explanations, unresolved evidence, competing hypotheses, and posterior support.
* Added bioinformatics references for QC outputs and sample identity, metadata and provenance, and qualifying evidence.
* Added genomics guidance for qualifying variants and explicit, versioned variant-selection criteria using the Qualifying Variant Set Standard (QVSS).
* Added support for the Qualifying Evidence Matrix (QEM) as an interoperable representation of verifiable evidence availability.
* Expanded genomics guidance for sequencing files, genomic intervals, alignment files and indexes, variant call files, HGVS nomenclature, coding and protein consequences, and exact reference provenance.
* Updated skill routing and repository documentation to clarify the boundaries between biological reasoning, bioinformatics, genomics, qualifying evidence, qualifying variants, and quinary inference.

## 0.1.0

Initial public release.

- Added `biology-core` and `genomics` Agent Skills.
- Added concise reference topics for biological context, evidence, identifiers, reference genomes, variant representation, transcripts, inheritance, phase, and gene expression.
- Added public source, review, style, contribution, and governance policies.
- Added structural validation, portable bundle export, tests, and behaviour evaluations.
