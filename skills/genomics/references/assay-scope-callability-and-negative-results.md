---
id: genomics.assay-scope-callability-and-negative-results
title: Assay scope, callability and negative results
domain: genomics
status: draft
---

# Assay scope, callability and negative results

## Summary

`No variant found` is not a complete genomic conclusion.

A negative sequencing result is meaningful only relative to what was actually interrogated in that sample and what the assay, library design, sequencing process, caller, and analysis workflow could detect. Locus coverage, callability, variant class, allele fraction, genomic context, and analytical validation can all limit what a negative result excludes.

## Core rules

- Separate assay scope from sample-level callability.
- Separate locus coverage from sensitivity to a specific event class.
- Depth alone does not prove that a locus or event was reliably callable.
- A no-call is not a reference call.
- An absent record in a variant-only VCF is not a reference genotype.
- A negative SNV or small-indel result does not exclude structural variants, copy-number changes, repeat expansions, complex variation, mitochondrial variation, mosaicism, or other event classes unless those classes were adequately interrogated.
- Targeted and exome assays can have capture gaps and uneven coverage that are specific to the assay design and sample.
- Variant sensitivity can depend on sequence context, mapping ambiguity, allele fraction, ploidy, read length, library preparation, and calling method.
- Preserve the capture design, relevant target intervals, assay version, pipeline, caller, and validated limitations when they affect interpretation.
- `No second allele found` should identify which plausible second-allele classes were adequately assessed and which remain unresolved.
- Do not infer molecular neutrality from a coding consequence label. Synonymous, intronic, or nominally missense alleles can affect splicing or transcript fate.

## Required context

For a negative genomic finding, establish as applicable:

- specimen and biological source
- assay type
- library and capture or enrichment design
- sequencing platform and relevant run metadata
- reference genome and exact analysis reference where material
- intended target region
- sample-level coverage and callability
- event classes in validated scope
- minimum reliable allele fraction where relevant
- mapping or sequence-context limitations
- variant caller and workflow version
- relevant QC and filtering
- whether reference-confidence information is available
- known regions or event classes that remain unresolved

## AI behaviour

Before saying that no causal variant, second allele, or pathogenic event exists:

1. determine what the assay was designed to measure,
2. determine whether the relevant locus was callable in this sample,
3. determine whether the relevant event class was detectable,
4. determine whether allele fraction, repeat size, copy-number state, genomic context, or mosaicism could fall outside validated sensitivity,
5. state remaining unresolved classes explicitly.

Do not turn adequate mean coverage into a claim that every medically relevant base and event class was adequately interrogated.

Do not use `PASS` or lack of a VCF record as a substitute for sample-level reference confidence.

If the workflow does not evaluate a relevant event class, report the limitation rather than treating the class as absent.

When a synonymous or other apparently low-impact DNA consequence is relevant to a splice region or RNA phenotype, keep the DNA consequence separate from predicted or observed RNA effect.

## Common failure modes

### Exome negative treated as genome negative

```text
No pathogenic SNV or small indel detected by exome sequencing.
```

does not establish:

```text
No pathogenic genetic cause exists.
```

Relevant structural, repeat, deep intronic, poorly captured, mitochondrial, mosaic, or other events can remain unresolved.

### Depth treated as callability

A reported depth of 30 reads does not by itself establish that the reads are uniquely mapped, high quality, balanced across alleles, or sufficient for the relevant variant class.

### No second allele found

In a suspected recessive disorder, one pathogenic allele plus no second small variant does not establish that a second pathogenic allele is absent. Phase, CNV, structural, splice-altering, repeat, mosaic, or technically unresolved explanations may remain.

### Consequence term treated as complete molecular effect

A `synonymous_variant` consequence means the selected coding translation predicts no amino-acid substitution. It does not exclude altered splicing, RNA stability, translation, or another sequence-dependent effect.

## Authoritative standards

Use current assay-specific clinical or research validation standards for exact coverage and sensitivity requirements. Use the VCF/gVCF specification and caller documentation for exact reference-confidence semantics.

Use maintained transcript and splicing guidance when a DNA consequence may affect RNA. Biology Skills does not replace ClinGen or other formal variant-interpretation frameworks.

## Examples

### Resolved and unresolved negative

```text
Resolved:
  target exon adequately covered
  SNV/small-indel calling validated
  confident reference genotype

Unresolved:
  exon poorly captured
  mapping ambiguous
  structural event not assessed
```

Both can produce no reported alternate allele, but they carry different evidence.

## Sources

- GA4GH Experiments Metadata Checklist: https://www.ga4gh.org/product/experiments-metadata-standard/
- VCF/BCF specifications: https://samtools.github.io/hts-specs/
- ClinGen splicing guidance: https://clinicalgenome.org/docs/application-of-the-acmg-amp-framework-to-capture-evidence-relevant-to-predicted-and-observed-impact-on-splicing-recommendations/
- Rehm HL et al. ACMG clinical laboratory standards for next-generation sequencing: https://doi.org/10.1038/gim.2013.92
- gnomAD: https://gnomad.broadinstitute.org/
