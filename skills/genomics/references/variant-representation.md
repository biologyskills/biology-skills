---
id: genomics.variant-representation
title: Variant representation
domain: genomics
status: draft
---

# Variant representation

## Summary

The same biological allele can have different textual or coordinate representations. Representation depends on the reference sequence, coordinate system, normalisation convention, and standard being used, particularly for indels, repeats, multiallelic sites, and complex variants.

## Core rules

- Variant identity is not determined by a coordinate string alone.
- Preserve reference sequence context and alleles when comparing variant records.
- Equivalent alleles can be represented differently after trimming, left alignment, right shifting, decomposition, or standard-specific normalisation.
- VCF and HGVS use different representation conventions. A VCF-normalised indel and an HGVS expression can legitimately place an equivalent change differently in repetitive sequence.
- Different standards can have different canonicalisation rules; string inequality does not necessarily mean biological inequality.
- An rs identifier, ClinVar identifier, HGVS expression, VCF record, and GA4GH identifier are different identifier or representation systems and are not interchangeable.
- Multiallelic and complex records can require decomposition or normalisation for some analyses, but transformation provenance and allele-dependent annotations must be preserved.
- Structural variants and copy-number changes can have imprecise breakpoints, symbolic alleles, or interval uncertainty. A simple position-plus-allele model is not sufficient for every variant class.

## Required context

Preserve as applicable:

- reference assembly or sequence accession
- chromosome or contig
- coordinate convention
- reference and alternate alleles
- variant class
- representation standard
- normalisation method
- decomposition or transformation steps
- uncertainty intervals or breakpoint confidence where relevant
- original record when transformations are analytically important

## AI behaviour

- Do not conclude that two variant strings describe different alleles until they have been compared on the same reference using an appropriate representation framework.
- Do not rewrite an allele into HGVS, VCF, or another notation without the reference information required by that notation.
- Preserve the original representation when reporting a transformed or normalised representation.
- Do not assume an rs identifier uniquely specifies one allele in one assembly and one molecular context.
- Do not apply VCF left-normalisation rules as if they were HGVS nomenclature rules, or vice versa.
- Do not decompose multiallelic or complex variants using naive string operations when genotype or allele-indexed annotation fields must be transformed consistently.
- Use the authoritative specification when exact syntax, canonicalisation, or uncertainty representation matters.

## Common failure modes

### Different strings treated as different biology

Equivalent indels in repetitive sequence can occupy different textual positions under different representation conventions.

### Identifier treated as a complete allele definition

A database identifier can refer to multiple mappings, alleles, or historical representations and may not substitute for the reference-specific allele required by an analysis.

### Normalisation without provenance

A transformed record can be valid for analysis while obscuring how the original call was represented if the transformation is not recorded.

### VCF and HGVS canonicalisation conflated

VCF workflows often left-align and trim alleles, whereas HGVS applies nomenclature-specific rules including its 3-prime rule. The resulting strings can differ while representing the same sequence change.

## Authoritative standards

Use the VCF specification for VCF representation, HGVS for sequence-variant nomenclature, and GA4GH Variation Representation Specification when interoperable computational variant identity is required. Use database-specific documentation for database identifiers.

## Examples

### Comparison workflow

Before declaring two indel records different:

1. establish the same reference sequence,
2. confirm that the alleles are represented on compatible strands and coordinates,
3. normalise or canonicalise according to the relevant standard,
4. compare the represented sequence change,
5. retain the original source representation.

Do not compare only the visible coordinate strings.

## Sources

- VCF specifications: https://samtools.github.io/hts-specs/
- HGVS Sequence Variant Nomenclature: https://hgvs-nomenclature.org/
- GA4GH Variation Representation Specification: https://vrs.ga4gh.org/
- NCBI dbSNP: https://www.ncbi.nlm.nih.gov/snp/
