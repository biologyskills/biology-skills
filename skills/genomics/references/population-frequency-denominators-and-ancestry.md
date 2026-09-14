---
id: genomics.population-frequency-denominators-and-ancestry
title: Population frequency, denominators and ancestry
domain: genomics
status: draft
---

# Population frequency, denominators and ancestry

## Summary

Allele frequency is not a fixed property attached permanently to a variant.

It is an estimate for a defined allele representation in a particular resource, release, callable denominator, and sampled population. A compact field such as `AF=0.001` can hide the denominator, ancestry composition, technical callability, filtering, and sampling process that produced the estimate.

## Core rules

- Distinguish allele count (`AC`), allele number (`AN`), and allele frequency (`AF`).
- `AC=0` is interpretable only with an informative callable denominator.
- `AN=0` or unavailable frequency is not equivalent to `AF=0`.
- Absence of an observed allele from a resource is not proof that the allele is absent from the population.
- Preserve the exact allele representation used for the frequency lookup.
- Preserve the population-frequency resource and release.
- Distinguish global frequency from ancestry- or population-group-specific frequency.
- Distinguish overall frequency from maximum-group or filtering frequency when those quantities are used.
- Do not infer rarity from missing population data.
- Consider whether the locus and event class were callable in the contributing data.
- Consider whether exome and genome data, sequencing technologies, coverage, filtering, or sample composition differ across groups.
- Population labels are analytical groupings, not biological essences. Interpret them according to the resource's definitions.
- Sampling and ascertainment can affect a reference resource even when it is large.
- For rare alleles, uncertainty can remain substantial even in large datasets; do not present a point estimate as exact population truth.

## Required context

For a population-frequency statement, preserve or establish:

- exact allele identity and representation
- reference assembly or sequence context where required
- database or resource
- resource release
- allele count
- allele number
- allele frequency
- population or ancestry grouping
- whether the value is global, group-specific, or a maximum-group statistic
- callability or coverage when relevant
- filtering status
- data type or subset when the resource separates exomes, genomes, or other assays

## AI behaviour

Before using allele frequency as evidence:

1. verify the exact allele being queried,
2. identify the resource and release,
3. inspect AC and AN where available,
4. identify the relevant population or ancestry grouping,
5. check whether the locus and event class were adequately callable,
6. distinguish missing frequency from zero frequency,
7. state whether the value is global or group-specific.

Do not write:

```text
absent from gnomAD
```

when the underlying state is:

```text
no alternate allele observed in this release and subset,
with the following callable denominator and limitations
```

Do not compare frequencies across resources or releases without checking allele representation, sample composition, filtering, and technical differences.

Do not treat ancestry-specific frequency as interchangeable with a global aggregate when the intended inference is population-specific.

## Common failure modes

### Zero denominator interpreted as zero frequency

```text
AC = 0
AN = 0
```

does not support:

```text
AF = 0
therefore absent from the population
```

There were no callable alleles contributing to the denominator.

### Global frequency hides population structure

A low global frequency can combine a higher frequency in one population with near absence in others. The biologically or clinically relevant comparison may require the appropriate group-specific estimate.

### Missing lookup treated as rarity evidence

Failure to find a variant can result from representation mismatch, resource scope, filtering, unsupported event class, or lack of callable observations.

### Resource release omitted

An allele count or classification can change as samples, pipelines, filtering, and annotations change between releases.

## Authoritative standards

Use the current documentation for the population resource supplying the frequency. For gnomAD, interpret AC, AN, AF, filtering, ancestry groups, release-specific data, and callability according to current gnomAD definitions.

Use an explicit variant representation before frequency lookup. Biology Skills does not replace GA4GH VRS, HGVS, VCF, or resource-specific identity rules.

## Examples

### Informative absence

```text
AC = 0
AN = 120000
```

supports the statement that no alternate alleles were observed among the callable alleles contributing to that estimate.

It does not prove a true population frequency of exactly zero.

### Uninformative absence

```text
AC = 0
AN = 0
```

contains no callable denominator and should not be interpreted as evidence that the allele is absent.

## Sources

- gnomAD: https://gnomad.broadinstitute.org/
- gnomAD v4.1 release: https://gnomad.broadinstitute.org/news/2024-04-gnomad-v4-1
- gnomAD population-frequency display and allele-number guidance: https://gnomad.broadinstitute.org/news/
- GA4GH Variation Representation Specification: https://vrs.ga4gh.org/
- Karczewski KJ et al. The mutational constraint spectrum quantified from variation in 141,456 humans: https://doi.org/10.1038/s41586-020-2308-7
