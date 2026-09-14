---
id: biological-statistics.ascertainment-selection-and-target-population
title: Ascertainment, selection and target population
domain: biological-statistics
status: draft
---

# Ascertainment, selection and target population

## Summary

An analysed dataset is the result of a selection process.

People, specimens, organisms, cells, records, or variants can enter or leave the dataset through eligibility, recognition, referral, recruitment, consent, survival, follow-up, measurement, missingness, filtering, and QC. The resulting estimate therefore describes the analysed population under that observation-generating process unless additional assumptions justify transport to another target population.

## Core rules

- Distinguish the source population from the final analysed population.
- Define the target population before generalising an estimate.
- Record eligibility, referral, recruitment, consent, survival, follow-up, measurement, filtering, attrition, and QC mechanisms when they can change inclusion.
- Do not assume that a convenience, clinic, registry, hospital, biobank, or volunteer sample represents the general population.
- A control group is defined by how controls were selected and assessed.
- `Not selected as a case` is not automatically equivalent to `phenotype absent`.
- A young control can be unresolved for an age-dependent phenotype.
- A treated or resolved phenotype is not equivalent to a phenotype that was never present.
- Selection on variables influenced by both an exposure and an outcome, or their causes, can create or distort associations.
- Missingness can be informative rather than random.
- Technical QC can be a biological selection mechanism if data quality depends on ancestry, disease state, sample type, site, severity, or another relevant factor.
- Do not use the analysed sample size as the denominator for a population claim without establishing why that denominator is appropriate.
- Internal validity in the study population does not guarantee transportability to another target population.
- Large sample size does not remove selection bias.

## Population layers

A useful decomposition is:

```text
source population
    ↓ eligibility
eligible population
    ↓ recognition / referral / recruitment
study population
    ↓ consent / measurement / follow-up
measured population
    ↓ filtering / missingness / QC
analysed population
    ↓ transport assumptions
target population
```

Not every study needs every layer explicitly, but collapsing materially different layers can hide selection.

## Required context

For a population-level estimate, establish where relevant:

- source population
- eligibility criteria
- recruitment or ascertainment route
- case definition
- control definition
- referral pathway
- consent process
- age and follow-up
- survival requirements
- measurement availability
- exclusion and attrition
- missing-data process
- QC and filtering
- relatedness or clustering
- target population
- assumptions used for generalisation or transport

## AI behaviour

Before generalising:

1. reconstruct how observations entered the analysed dataset,
2. identify important exclusion and attrition mechanisms,
3. define what each comparison group actually represents,
4. identify the denominator used by the estimate,
5. determine the intended target population,
6. state whether transport from the study population is justified or uncertain.

Do not describe tertiary-clinic prevalence as population prevalence without a defensible sampling or transport argument.

Do not call unscreened controls `healthy controls` merely because they were not diagnosed with the case condition.

Do not infer absence of an age-dependent phenotype in someone who has not yet reached the relevant age or observation window.

Treat post-measurement QC exclusions as potential selection, not merely technical housekeeping.

## Common failure modes

### Specialist referral cohort treated as population sample

```text
study:
  adults referred to an inherited-cardiomyopathy clinic
```

does not directly support:

```text
prevalence among all adults
```

without a population sampling or transport model.

### Control label overinterpreted

A control selected because they were not enrolled as a case may still have unassessed, preclinical, age-dependent, or unrelated disease.

### QC changes ancestry composition

If one ancestry group has systematically poorer mapping or capture performance and therefore higher QC exclusion, the analysed cohort can differ from the recruited cohort in a biologically structured way.

### Survivor selection ignored

A study enrolling only adults cannot directly observe people with the same underlying condition who died before recruitment.

## Authoritative standards

Use the reporting standard appropriate to the study design. STROBE requires transparent reporting of participant selection and study populations in observational research.

For causal reasoning about selection and transportability, use explicit epidemiological or causal-inference frameworks rather than assuming representativeness from sample size.

Structured phenotype standards such as GA4GH Phenopackets can help preserve explicit phenotype presence, exclusion, and temporal context, but they do not themselves remove selection bias.

## Examples

### Case-control interpretation

```text
cases:
  referred patients meeting disease criteria

controls:
  biobank participants not selected as cases
```

Before interpreting a genetic frequency difference, establish whether controls were assessed for the disease, their age distribution, ancestry, recruitment process, and relevant technical comparability.

## Sources

- STROBE Statement: https://www.strobe-statement.org/
- Hernán MA, Robins JM. Causal Inference: What If: https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/
- GA4GH Phenopackets: https://www.ga4gh.org/product/phenopackets/
- gnomAD: https://gnomad.broadinstitute.org/
