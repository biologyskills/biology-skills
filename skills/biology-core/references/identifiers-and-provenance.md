---
id: biology-core.identifiers-and-provenance
title: Identifiers and provenance
domain: biology-core
status: draft
---

# Identifiers and provenance

## Summary

Biological identifiers often refer to versioned, database-specific, or reference-dependent objects. Reproducible work requires enough provenance to recover the exact object and transformation used.

## Core rules

- Preserve identifier namespaces when similar identifiers can exist in different systems.
- Preserve versions when a version change can alter sequence, annotation, or interpretation.
- A human-readable name is not always a stable computational identifier.
- Derived results should retain enough provenance to identify source data, reference systems, transformations, and relevant software or model versions.
- Do not silently map between identifiers when the mapping is ambiguous or many-to-many.

## Required context

Depending on the task, preserve:

- identifier and namespace
- version or release
- reference database or assembly
- source dataset
- transformation or mapping step
- software, model, or annotation version
- date or release when an external resource changes over time

## AI behaviour

- Prefer stable identifiers over names when reproducibility matters.
- Report ambiguity rather than silently choosing one of several plausible mappings.
- Keep source and derived identifiers distinct.
- Include a database, annotation, model, or software version when the conclusion depends on it.

## Common failure modes

### Name treated as identifier

Gene symbols, protein names, and phenotype labels can change or be reused. A name alone can be insufficient for computational reproducibility.

### Version removed during presentation

Removing transcript, sequence, ontology, or database versions can make a result impossible to reproduce or can change the object being described.

## Authoritative standards

Use the authority that owns the identifier or namespace for exact syntax and lifecycle rules. Examples include HGNC for human gene nomenclature, NCBI and Ensembl for sequence and annotation identifiers, and domain ontologies for controlled terms.

## Examples

### Version-sensitive object

Prefer an identifier plus version when the exact sequence or annotation version affects the result.

Avoid stripping version information merely to make a user interface shorter.

## Sources

- HGNC: https://www.genenames.org/
- NCBI Datasets: https://www.ncbi.nlm.nih.gov/datasets/
- Ensembl: https://www.ensembl.org/
