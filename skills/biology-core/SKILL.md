---
name: biology-core
description: Apply foundational biological correctness rules for context, evidence, claims, identifiers, provenance, and uncertainty. Use whenever biological meaning depends on experimental context, evidence type, reference systems, versions, model outputs, or the distinction between observation, prediction, association, mechanism, and causality.
---

# Biology core

Use this skill whenever biological context, evidence type, provenance, or inference level could materially change the meaning of a result.

This skill provides cross-cutting rules. Use it together with the relevant domain skill when more specific biological or technical conventions apply.

## Core rules

- Treat biologically material context as part of the result, not optional metadata.
- Do not generalise a context-specific result across species, model systems, tissues, cell types, developmental stages, physiological states, disease states, perturbations, assays, or time points without supporting evidence.
- Distinguish what was directly observed or measured from what was predicted, inferred, associated, interpreted, mechanistically proposed, or causally established.
- Do not make a claim stronger than the evidence supports.
- Interpret model outputs according to their defined target, scale, uncertainty, and validation. A score, rank, percentile, or transformed quantity is not automatically a probability, diagnosis, mechanism, or causal estimate.
- Preserve identifiers, namespaces, versions, reference systems, and provenance when they affect biological meaning, reproducibility, or interpretation.
- Do not silently resolve ambiguous identifier mappings, reference choices, comparison groups, or other biologically consequential uncertainty.
- Keep source data and identifiers distinct from mapped, transformed, annotated, predicted, or otherwise derived results.
- When an authoritative community resource governs exact nomenclature, identifiers, ontology terms, or syntax, use that maintained standard rather than inventing a local substitute.

## AI behaviour

Before making, comparing, or summarising a biological claim, identify:

1. what was directly measured or observed,
2. what was predicted or inferred,
3. the biological and experimental context,
4. the comparison or reference frame,
5. the relevant uncertainty,
6. the provenance needed to recover the objects being discussed.

If omitted context could materially change the conclusion, recover it from the available evidence where possible. If it remains unknown, state the limitation rather than silently filling it with a common default.

When combining studies or datasets, establish that their biological systems, assays, units, comparison conditions, identifiers, and reference systems are sufficiently compatible for the intended inference.

Do not turn association into mechanism, prediction into observation, ranking into probability, or statistical evidence into biological causality without the additional evidence required for that claim.

Do not silently choose among ambiguous identifiers or mappings. Preserve the source identifier and report ambiguity when more than one mapping is plausible.

When simplifying technical material, preserve distinctions whose removal could change the biological interpretation.

## References

Read the relevant reference when the task depends on it:

- [`references/biological-context.md`](references/biological-context.md) for species, model systems, tissue, cell type, developmental or disease state, perturbation, assay, time, and other context-dependent biology
- [`references/evidence-and-claims.md`](references/evidence-and-claims.md) for distinguishing observation, measurement, prediction, association, mechanism, causality, model outputs, and appropriate validation
- [`references/identifiers-and-provenance.md`](references/identifiers-and-provenance.md) for identifier namespaces, versions, mappings, reference systems, source-versus-derived objects, and reproducibility

