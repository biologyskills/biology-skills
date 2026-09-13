---
id: genomics.genomic-intervals
title: Genomic intervals
domain: genomics
status: draft
---

# Genomic intervals

## Summary

Genomic intervals describe spans on a reference sequence. BED is a common interval format, but interval meaning depends on reference identity, coordinate convention, strand, and feature semantics. Off-by-one and cross-assembly errors are common because different genomics formats use different coordinate systems.

## Core rules

- A BED interval is defined by sequence name, zero-based start, and end-exclusive end. The start is included and the end is excluded.
- A one-base BED interval covering the tenth base of a sequence is represented as start `9`, end `10`.
- BED coordinates are not directly interchangeable with one-based positions used by formats such as SAM text and VCF.
- The sequence name does not identify the assembly. `chr1:100-200` is incomplete without reference context when biological interpretation depends on it.
- Strand is a separate attribute. An interval's genomic coordinates do not reverse when the feature is on the minus strand.
- BED3 supplies the three core interval columns. BED6 and BED12 add standard fields, but many tools also use BED-like tabular formats with non-standard extra columns. Their semantics must be documented rather than inferred.
- BED12 block starts are relative to `chromStart`, not absolute genomic coordinates.
- Sorting is not part of interval identity, but many algorithms and indexing methods require a defined coordinate sort order.
- GFF and GTF use different coordinate conventions and richer feature models. Do not convert by renaming columns alone.

## Required context

For reliable interval work preserve:

- reference assembly or sequence collection
- chromosome or contig naming convention
- coordinate convention
- strand where biologically relevant
- interval semantics, such as exon, capture target, peak, deletion, or callable region
- BED column schema or any custom extension
- sort order when required by downstream tools
- annotation release when intervals represent genes, transcripts, exons, or regulatory features
- conversion history when intervals were lifted or transformed

## AI behaviour

- Do not mix BED coordinates with one-based coordinates without an explicit conversion.
- Do not infer genome build from sequence names or interval magnitudes.
- Before intersecting two interval sets, establish that they use compatible references and coordinate conventions.
- Do not assume a BED interval describes a gene, exon, or variant merely because it overlaps one.
- Do not assume every BED-like file follows all BED12 field semantics. Inspect its producing tool or documentation.
- When converting strand-aware biological features, distinguish genomic interval coordinates from transcript-relative orientation.
- Do not assume a sorted file is required unless the consuming operation or index requires it.

## Common failure modes

### One-base shift during conversion

A VCF SNV at one-based position 10 corresponds to the genomic base represented by BED interval `9 10`, not `10 11`.

### Mixing assemblies

Two BED files with matching `chr1` names can describe different physical sequence if one uses GRCh37 and the other GRCh38.

### Strand used to reverse coordinates

BED `chromStart` must remain less than or equal to `chromEnd` irrespective of `+` or `-` strand. Strand records biological orientation, not a reversed coordinate ordering.

### Custom BED columns treated as standard

Many pipelines append arbitrary fields after the standard BED columns. Their meaning cannot be safely inferred from column position alone once the file departs from the documented schema.

## Authoritative standards

Use the current BED specification or UCSC documentation for standard BED fields, and use the GFF/GTF specification for those formats. Use tool-specific documentation for custom BED-like outputs and indexing requirements.

## Examples

### One-base interval

```text
chr1	9	10
```

This BED interval covers one base. In a one-based closed representation that same genomic base is position 10.

### Strand-aware feature

```text
chr7	127471196	127472363	feature1	0	-
```

The coordinates remain ascending. The minus strand records feature orientation.

## Sources

- SAMtools `hts-specs` BED specification: https://samtools.github.io/hts-specs/
- UCSC BED format documentation: https://genome.ucsc.edu/FAQ/FAQformat.html#format1
- GFF3 specification: https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md
