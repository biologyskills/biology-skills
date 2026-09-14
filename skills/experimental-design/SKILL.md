---
name: experimental-design
description: Apply biological experimental-design correctness rules for experimental units, replication, batch structure, controls, technical dependence, validation, and assay design. Use when the meaning of a biological result depends on what was independently sampled, assigned, measured, replicated, controlled, or technically confounded.
---

# Experimental design

Use this skill when a biological conclusion depends on the structure of an experiment rather than only on the number of measurements produced.

The central question is:

> What was genuinely independent, and could the design distinguish the claimed biological effect from its technical alternatives?

## Core rules

- Identify the experimental unit before interpreting sample size or independence.
- The unit measured is not automatically the unit independently assigned to treatment or condition.
- Distinguish biological replication, technical replication, subsampling, repeated measurement, and duplicated computation.
- Do not infer independent `n` from the number of rows, cells, reads, fields, wells, images, libraries, or other measurements.
- Preserve nesting and clustering when multiple observations derive from the same donor, animal, specimen, culture, library, batch, or experimental unit.
- Match the statistical model to the level at which treatment, exposure, or sampling was independently varied.
- Distinguish the intended experimental design from the realised design after exclusion, assay failure, missingness, and QC.
- Do not rely on post hoc batch correction to identify a biological effect when batch and biological condition are completely confounded.
- Controls must address the alternative explanation relevant to the claim; a nominal control label does not guarantee process matching.
- Technical replication can estimate technical variability but does not by itself establish biological reproducibility.
- An orthogonal validation is strongest when it does not simply reproduce the same upstream failure mechanism under a different tool or assay name.
- Preserve randomisation, blocking, processing order, plate, lane, batch, and other design variables when they can affect the result.

## AI behaviour

Before treating observations as independent, determine:

1. what unit was independently sampled or assigned,
2. what unit received the intervention or exposure,
3. which observations share a biological source,
4. which observations share a technical process,
5. which repeated measurements or subsamples belong to the same unit,
6. what `n` actually counts.

If treatment and batch are aligned, state the confounding rather than assuming normalization can uniquely recover the missing comparison.

When a study reports many cells, reads, images, wells, or fields from a small number of donors or animals, preserve the higher-level biological structure.

When describing replication, name the replication level rather than using `replicate` without qualification.

## References

Read the relevant reference when the task depends on it:

- [`references/experimental-unit-replication-and-pseudoreplication.md`](references/experimental-unit-replication-and-pseudoreplication.md) for experimental units, biological and technical replication, subsampling, nested observations, repeated measures, effective independence, and pseudoreplication
