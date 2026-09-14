---
id: biology-core.measurement-observability-and-negative-evidence
title: Measurement, observability and negative evidence
domain: biology-core
status: draft
---

# Measurement, observability and negative evidence

## Summary

A biological state can be confidently described as absent only when the measurement or assessment had an adequate opportunity to observe that state.

`Absent`, `not detected`, `not measured`, `not callable`, `below detection limit`, `unknown`, and `not applicable` are different scientific states. Collapsing them can create false negative evidence and can make downstream statistical or causal inference stronger than the data justify.

## Core rules

- A negative result is evidence against a biological state only relative to a measurement process capable of observing that state.
- Lack of a positive record is not itself a negative measurement.
- Preserve the difference between observed absence, non-detection, missingness, lack of assessment, lack of callability, below-detection values, unknown states, and not-applicable states.
- Observability can be location-specific, event-class-specific, sample-specific, phenotype-specific, state-specific, and time-specific.
- A measurement can have adequate data volume while still being insensitive to the relevant event or biological state.
- Preserve the reason for missing or unresolved information when that reason affects interpretation.
- Do not convert an unresolved measurement into evidence against a hypothesis.
- Detection limits, analytical sensitivity, assessment criteria, and relevant QC can be part of the meaning of a negative result.
- Derived datasets must not strengthen the meaning of an upstream negative state merely by reducing its representation.

## Observation states

The exact vocabulary varies by domain, but these concepts should remain separable when relevant:

```text
observed present
observed absent
not detected
not measured
not assessed
not callable
below detection limit
missing
unknown
not applicable
```

A binary representation may be useful downstream, but the upstream state and reduction rule should remain recoverable when the distinction can affect scientific interpretation.

## Required context

For a negative or unresolved observation, establish where relevant:

- what biological state is being assessed
- the specimen, tissue, cell type, individual, or other measurement target
- the assay or assessment method
- whether the relevant location or state was in assay scope
- analytical sensitivity or detection limit
- technical quality required for interpretation
- temporal context
- whether the result is explicit negative evidence or merely absent from the data
- why a value is missing or unresolved
- the denominator or coverage supporting a negative claim

## AI behaviour

Before stating that something is absent, negative, reference, normal, or not present:

1. identify the exact state being claimed absent,
2. determine whether it was explicitly measured or assessed,
3. determine whether the method could detect it in the relevant context,
4. distinguish a resolved negative result from an unresolved or missing result,
5. preserve the relevant detection, quality, or denominator information.

Do not infer a negative phenotype from lack of documentation.

Do not infer a reference genotype from lack of a variant record.

Do not infer absence of expression from failure to detect a transcript without considering assay sensitivity and context.

When the available data support only non-detection, say `not detected` rather than strengthening the claim to biological absence.

## Common failure modes

### Missing record treated as negative evidence

```text
Observed:
  no record for locus X

Unsafe:
  locus X is reference

Required:
  determine whether the locus was measured and callable
```

No emitted record can reflect a variant-only representation, filtering, missing coverage, parser behaviour, or a genuinely resolved reference state.

### Unassessed phenotype treated as absent

A phenotype omitted from a clinical record may never have been assessed. This is not equivalent to an explicit negative examination.

### Below detection limit treated as zero

A result below a method's detection threshold does not establish a true biological quantity of zero.

### Unsupported event class excluded

A sequencing assay that reliably detects SNVs does not automatically exclude copy-number changes, repeat expansions, structural rearrangements, mosaic events, or other event classes outside its validated scope.

## Authoritative standards

Use domain-specific assay and reporting standards for exact requirements. Biology Skills defines the interpretive distinction: negative evidence requires adequate observability.

Where structured phenotype exchange is required, use maintained standards such as GA4GH Phenopackets rather than inventing local missing-versus-excluded semantics. Where genomic experiment metadata affect observability, use maintained experiment metadata standards and assay documentation.

## Examples

### Genomic observation

```text
no variant record
!= callable reference genotype
!= unresolved locus
```

### Phenotype observation

```text
not mentioned in record
!= assessed and absent
```

### Quantitative assay

```text
signal < detection limit
!= biological concentration = 0
```

## Sources

- GA4GH Phenopackets: https://www.ga4gh.org/product/phenopackets/
- GA4GH Experiments Metadata Checklist: https://www.ga4gh.org/product/experiments-metadata-standard/
- gnomAD: https://gnomad.broadinstitute.org/
- Wilkinson MD et al. The FAIR Guiding Principles for scientific data management and stewardship: https://doi.org/10.1038/sdata.2016.18
