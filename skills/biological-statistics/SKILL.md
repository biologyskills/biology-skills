---
name: biological-statistics
description: Apply statistical correctness rules for biological observation-generating processes, ascertainment, selection, denominators, target populations, relatedness, dependence, and transportability. Use when cohort construction, sampling, controls, population structure, missingness, or dependence can change a biological estimate or inference.
---

# Biological statistics

Use this skill when a statistical result depends on how biological observations entered the dataset, which observations contributed to the denominator, or to whom the result is intended to generalise.

The central question is:

> What process generated these observations, and to which population or biological units does the inference actually apply?

## Core rules

- Distinguish source population, eligible population, recruited population, measured population, analysed population, and target population when they differ.
- An estimate inherits the process that selected the observations used to calculate it.
- Preserve eligibility, referral, recruitment, consent, survival, follow-up, measurement, exclusion, attrition, and QC mechanisms when they can affect inclusion.
- A `control` is defined by its ascertainment criteria, not by the label `control`.
- `Control` does not automatically mean healthy, phenotype-negative, disease-free for life, population-representative, or exchangeable with cases except for the exposure of interest.
- Do not use a denominator without establishing what observations were eligible to contribute to it.
- Selection related to exposure, outcome, or common causes can change observed associations.
- Treat missingness and technical QC as potential selection mechanisms when exclusion can correlate with biology, ancestry, disease severity, sample quality, site, or other relevant variables.
- Distinguish internal validity from transportability to another target population.
- Do not assume a predictive model, frequency estimate, or treatment effect transports unchanged to a different population.
- Preserve relatedness, repeated measurements, clustering, and hierarchical dependence when they affect effective independence.
- Population structure and ancestry can alter genetic associations and frequency estimates; adjustment strategy must match the inferential target.
- Statistical precision does not repair an undefined target population or selection mechanism.

## AI behaviour

Before interpreting or generalising an estimate, establish:

1. what population generated the eligible observations,
2. how subjects or samples became included,
3. who or what was excluded before and after measurement,
4. what the denominator counts,
5. what `case`, `control`, `exposed`, or other group labels actually mean,
6. whether missingness or QC changed the analysed population,
7. whether observations are independent,
8. which population or biological units the requested conclusion targets.

When a cohort is recruited through a specialist clinic, registry, biobank, hospital, referral network, or voluntary study, do not silently reinterpret it as a random sample of the general population.

When controls were not systematically assessed for the phenotype, do not call them phenotype-negative.

When age, treatment, survival, or follow-up affects manifestation, do not convert non-observation into lifelong absence.

When a result is transported to another population, state the assumptions or limitations rather than presenting transportability as automatic.

## References

Read the relevant reference when the task depends on it:

- [`references/ascertainment-selection-and-target-population.md`](references/ascertainment-selection-and-target-population.md) for source and target populations, eligibility, recruitment, attrition, controls, QC selection, denominators, selection bias, and transportability
