---
id: genomics.gene-expression
title: Gene expression
domain: genomics
status: draft
---

# Gene expression

## Summary

Gene expression is a measured or inferred quantity in a defined biological and technical context. It is not a single fixed property permanently attached to a gene, and RNA abundance is not interchangeable with protein abundance or biological activity.

## Core rules

- Expression can vary across tissues, cell types, developmental stages, physiological states, disease states, perturbations, and time.
- Gene-level and transcript-level expression are different quantities.
- RNA abundance, transcription rate, translation, protein abundance, and protein activity are related but distinct biological measurements.
- Bulk measurements can reflect changing cell composition as well as changes within cells.
- Counts, normalised abundance, TPM-like quantities, relative fold changes, and absolute molecule numbers are not interchangeable.
- Assay platform, library preparation, strandedness, annotation, quantification method, and normalisation can affect the reported value.
- Failure to detect expression is not equivalent to proving biological absence.
- A reference transcript selected for reporting does not establish that it is the predominantly expressed transcript in the biological system being studied.

## Required context

Preserve as applicable:

- organism
- tissue, cell type, or cell composition
- developmental or disease state
- perturbation and time point
- assay type
- bulk or single-cell design
- gene-level or transcript-level quantification
- annotation provider and release
- normalisation method and unit
- comparison group and statistical model
- relevant batch, replicate, and study-design information

## AI behaviour

- Qualify expression claims with biological system and measurement context when they affect interpretation.
- Do not infer absence of function from low or undetected expression in one unrelated tissue, cell type, condition, or assay.
- Do not treat bulk expression changes as cell-intrinsic without considering composition.
- Keep gene-level and transcript-level claims separate.
- Do not convert an assay-specific quantity into generic "expression level" when the unit or normalisation carries meaning.
- Do not infer protein abundance or activity directly from RNA abundance without supporting evidence.
- When comparing datasets, check annotation, quantification, normalisation, and biological context before attributing differences to biology.

## Common failure modes

### Context-free expression claim

"Gene X is not expressed" can be incorrect when the evidence only shows that it was not detected in one tissue, condition, assay, or dataset.

### Bulk signal treated as cell-intrinsic

A change in bulk RNA abundance can arise because cell-type proportions changed rather than because each cell changed transcription.

### RNA treated as protein activity

A transcript can be abundant while translation, localisation, degradation, post-translational modification, or inhibition limits protein function.

### Transcript selection confused with expression

A MANE or canonical transcript can be selected for consistent reporting without being the most abundant transcript in every relevant tissue.

## Authoritative standards

Use assay-specific reporting standards, annotation resources, and controlled vocabularies when exact metadata requirements matter. Use the relevant quantification and statistical method documentation for the meaning of units and normalisation.

## Examples

### Better statement

Prefer: "Gene X had low RNA abundance in this bulk liver RNA-seq dataset under the stated normalisation."

Avoid: "Gene X has low expression" when the claim is intended to be universal.

### Transcript-level statement

Prefer a statement that identifies the transcript, tissue, assay, and quantification method when transcript usage is central to the claim.

## Sources

- GTEx Portal: https://gtexportal.org/
- ENCODE Project: https://www.encodeproject.org/
- Human Cell Atlas: https://www.humancellatlas.org/
- GENCODE: https://www.gencodegenes.org/
