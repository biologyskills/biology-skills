---
id: biology-core.biological-context
title: Biological context
domain: biology-core
status: draft
---

# Biological context

## Summary

Many biological statements are conditional on the system in which they were measured or inferred. Species, tissue, cell type, developmental stage, disease state, environment, perturbation, assay, and time can change the meaning of an otherwise identical-looking result.

## Core rules

- Do not treat a biological effect as universal when it was established only in a specific context.
- Gene expression, regulatory activity, signalling, chromatin state, phenotype, and molecular interactions can vary across tissues, cell types, developmental stages, and states.
- Evidence from one species, model system, organoid, or cell line does not automatically establish the same effect in another.
- Experimental context is part of the result when changing that context could change the biological conclusion.

## Required context

Preserve or recover, where relevant:

- species and strain
- tissue and anatomical source
- cell type or cellular composition
- developmental or age context
- disease or physiological state
- perturbation, treatment, or exposure
- assay and measurement modality
- time point
- comparison or control condition

## AI behaviour

- State the biological context when it materially constrains a claim.
- Do not generalise a context-specific result to all tissues, cell types, species, or states without supporting evidence.
- When combining studies, check whether their biological systems are comparable for the intended inference.
- Treat missing material context as uncertainty rather than silently filling it with a common default.

## Common failure modes

### Treating expression as a fixed property

A statement that a gene is "highly expressed" is incomplete when the measurement is specific to one tissue, cell type, state, or assay.

### Treating a model system as the target organism

An effect observed in a cell line or animal model can support a hypothesis in humans, but it does not by itself establish the same magnitude, mechanism, or clinical consequence in humans.

## Authoritative standards

Use domain-specific reporting standards and controlled vocabularies when exact metadata requirements matter. Biology Skills explains why context is needed; the relevant ontology or reporting standard defines exact terms.

## Examples

### Context-dependent expression

Prefer: "The transcript was highly expressed in the assayed liver samples."

Avoid: "The gene is highly expressed" when the evidence is limited to one tissue or condition.

## Sources

- ENCODE Project: https://www.encodeproject.org/
- GTEx Portal: https://gtexportal.org/
- Cell Ontology: https://obophenotype.github.io/cell-ontology/
