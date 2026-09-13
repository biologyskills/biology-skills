---
id: genomics.variant-call-files-and-indexes
title: Variant call files and indexes
domain: genomics
status: draft
---

# Variant call files and indexes

## Summary

VCF represents genomic variant records and optional sample genotypes; BCF is a binary representation of the same data model. gVCF-style files add reference-confidence information for later joint genotyping. Correct interpretation depends on the header, reference sequence, allele indexing, ploidy, caller conventions, and any matching coordinate index.

## Core rules

- VCF records are reference-dependent. `CHROM`, `POS`, `REF`, and `ALT` together contribute to allele representation.
- VCF `POS` is 1-based, and `ALT` can contain multiple alternate alleles.
- Genotype values are allele indices, not literal bases, and genotype ploidy is not universally diploid.
- `/` denotes unphased allele order and `|` phased allele order; additional fields can be needed to define phase sets.
- INFO and FORMAT semantics come from the header and producing workflow.
- `QUAL`, `FILTER`, and sample genotype-quality fields are distinct. `PASS` is not biological validation or pathogenicity.
- Absence from a variant-only VCF does not establish a homozygous-reference genotype.
- gVCF-style files add reference-confidence information, but block and symbolic-allele semantics depend on the generating workflow.
- BCF is a binary representation of the VCF data model, not a different biological result.
- Indexed VCF is commonly BGZF-compressed with TBI or CSI. TBI uses an older fixed binning range; CSI supports configurable binning and larger coordinate spaces. An index belongs to the exact data file and can become stale after modification.

## Required context

Preserve or establish:

- VCF or BCF version
- complete header definitions
- reference assembly and exact reference sequence where relevant
- caller, caller version, and workflow
- sample identities and ploidy assumptions
- genotype and phasing fields
- filtering model
- normalisation or decomposition history
- whether the file is variant-only, sites-only, all-sites, gVCF-style, or another specialised representation
- compression type
- index type and evidence that the index matches the current data file

## AI behaviour

- Read the header before interpreting INFO or FORMAT values.
- Do not use `QUAL` as a substitute for sample genotype confidence.
- Do not interpret `0/1` as universally meaning diploid heterozygosity without considering ploidy and the file context.
- Do not interpret an absent VCF record as reference genotype unless the workflow provides reference-confidence or callable-region evidence supporting that conclusion.
- Do not treat `PASS` as clinical validation.
- Do not split or normalise multiallelic records with naive text processing. Allele-indexed INFO and FORMAT fields can require coordinated transformation.
- When comparing VCFs, normalise and compare against a common reference where appropriate rather than relying on string equality alone.
- Treat gVCF records according to the caller and joint-genotyping workflow that produced them. Do not assume every file labelled gVCF has identical block or symbolic-allele semantics.
- Before indexed region queries, confirm compatible coordinate sorting, BGZF or relevant binary encoding, and a matching TBI or CSI index.

## Common failure modes

### Missing record called homozygous reference

A standard variant-only VCF generally reports selected variant sites. No line at a position can mean no emitted call, not necessarily `0/0`.

### Genotype indices treated as nucleotide values

For `REF=C` and `ALT=A,G`, genotype `1/2` refers to alleles `A` and `G`. The numbers are indexes into the record's allele list.

### Site quality confused with genotype quality

Record-level `QUAL` is not the same quantity as a sample-level `GQ` field. Exact semantics can also vary by caller and should be checked in metadata.

### Naive multiallelic splitting

Splitting `ALT=A,G` into two rows without updating allele-dependent INFO and FORMAT fields can corrupt genotype and annotation meaning.

### Stale index

Changing, re-sorting, filtering, or recompressing a `.vcf.gz` can invalidate an existing `.tbi` or `.csi` even if the filename is reused.

## Authoritative standards

Use the current VCF/BCF specification in `hts-specs` for exact field and representation rules. Use htslib or producing-tool documentation for BGZF, tabix, CSI, and gVCF workflow behaviour. Biology Skills does not redefine those specifications.

## Examples

### Multiallelic genotype

```text
REF=C
ALT=A,G
GT=1/2
```

The genotype contains the first and second alternate alleles. It does not contain the reference allele.

### Variant-only versus reference confidence

A missing position in a variant-only VCF is not sufficient evidence for a reference genotype. A gVCF-style workflow can preserve reference-confidence evidence in non-variant blocks for later joint genotyping, but its exact fields must be interpreted according to the caller.

## Sources

- VCF and BCF specifications: https://samtools.github.io/hts-specs/
- htslib tabix documentation: https://www.htslib.org/doc/tabix.html
- htslib bgzip documentation: https://www.htslib.org/doc/bgzip.html
- GATK gVCF overview: https://gatk.broadinstitute.org/hc/en-us/articles/360035531642-HaplotypeCaller
