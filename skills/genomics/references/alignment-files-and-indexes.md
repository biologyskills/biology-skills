---
id: genomics.alignment-files-and-indexes
title: Alignment files and indexes
domain: genomics
status: draft
---

# Alignment files and indexes

## Summary

SAM, BAM, and CRAM represent sequencing reads and their alignments to reference sequences. SAM is text, BAM is the binary BGZF-compressed representation of SAM alignment records, and CRAM uses a different compressed representation that can exploit reference sequence and configurable preservation options. BAI, CSI, and CRAI are auxiliary indexes for region-based access. Correct interpretation depends on reference identity, sort order, flags, CIGAR operations, read groups, coordinate conventions, and a matching index.

## Core rules

- Alignments are defined relative to the reference sequence used for mapping. A label such as `chr1` does not identify the assembly or exact FASTA.
- SAM, BAM, and CRAM can contain mapped and unmapped records. Mapping state is defined by FLAG semantics, not coordinates alone.
- SAM `POS` is 1-based; BAM stores the corresponding internal coordinate zero-based. APIs and region queries may use other conventions.
- CIGAR operations describe alignment structure and cannot be reduced to read length.
- Base quality, mapping quality, FLAG state, duplicate state, read groups, and secondary or supplementary status are distinct properties.
- BAM commonly uses BAI or CSI; CRAM commonly uses CRAI. An index belongs to a particular file and compatible ordering.
- BAI cannot address coordinates at or beyond its 2^29 limit on a reference sequence; CSI supports configurable binning and larger coordinate spaces.
- CRAM reference requirements and data-preservation choices depend on the file and encoding configuration. Do not assume every CRAM is fully self-contained or losslessly equivalent to an originating BAM.

## Required context

For reproducible interpretation preserve or establish:

- alignment format and relevant format version
- reference sequence dictionary, including names and lengths
- exact reference identity where available, including accessions or checksums
- declared and actual sort order
- aligner and relevant processing provenance
- read groups and sample identity when they matter
- duplicate, secondary, and supplementary alignment handling
- index type and evidence that the index belongs to the current alignment file
- coordinate convention used by the API, command-line region, or downstream format
- for CRAM, reference and preservation settings needed to reproduce decoding or downstream analysis

## AI behaviour

- Treat BAI, CSI, and CRAI files as access structures, not independent biological datasets.
- Do not infer a reference build from chromosome naming alone. Use sequence dictionaries and provenance.
- Do not describe an alignment file as invalid merely because an index is absent. Sequential access can still be possible; what is missing is efficient indexed retrieval.
- Before relying on indexed region access, ensure the file ordering is compatible with the index and the index matches the current file.
- Use FLAG semantics to determine mapped, unmapped, secondary, supplementary, duplicate, paired, and related states.
- Do not compare MAPQ values from different aligners as if they were guaranteed to have identical calibration or semantics.
- Establish coordinate conventions explicitly when converting between SAM/BAM internals, BED-like intervals, VCF positions, APIs, and browser displays.
- When reading CRAM, preserve access to the correct reference resources or reference-resolution mechanism required by the file.

## Common failure modes

### Inferring GRCh38 from `chr1`

A header containing `SN:chr1` is not enough to establish GRCh38. Sequence lengths, checksums, accessions, and pipeline provenance provide stronger reference identity.

### Treating an index as interchangeable

Resorting, filtering, rewriting, or replacing an alignment file can invalidate an older index even when the basename is unchanged.

### Calling a coordinate-bearing record mapped

A record must be interpreted using its FLAG state. Coordinates and CIGAR fields cannot independently override the unmapped flag.

### Assuming all alignment coordinates are 1-based

SAM text is 1-based for `POS`, BAM binary coordinates are zero-based internally, and software APIs can choose either convention.

### Assuming CRAM always reconstructs from one external FASTA

CRAM reference use is configurable and implementation-aware. Treat the actual CRAM metadata and decoder requirements as authoritative for that file.

## Authoritative standards

Use the current SAM/BAM, CRAM, CSI, and related `hts-specs` documents for exact field definitions, flag bits, binning rules, and version-specific syntax. Biology Skills describes the interpretation constraints around those specifications.

## Examples

### Reference dictionary

```text
@HD VN:1.6 SO:coordinate
@SQ SN:chr1 LN:248956422 M5:<checksum>
```

`SO:coordinate` declares sort order. The `@SQ` record describes a reference sequence. The name `chr1` alone does not establish the assembly.

### Missing index

A coordinate-sorted `sample.bam` with no BAI or CSI can still be read sequentially. Efficient random access to selected regions requires a suitable index.

### Mapping state

A record with a position field should not be called mapped without checking FLAG bit `0x4` and interpreting the remaining fields consistently with the specification.

## Sources

- SAM/BAM Format Specification Working Group, `hts-specs`: https://samtools.github.io/hts-specs/
- SAM/BAM and BAI specification: https://samtools.github.io/hts-specs/SAMv1.pdf
- CRAM specification: https://samtools.github.io/hts-specs/CRAMv3.pdf
- Coordinate-sorted index specification: https://samtools.github.io/hts-specs/CSIv1.pdf
