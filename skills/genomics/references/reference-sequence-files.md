---
id: genomics.reference-sequence-files
title: Reference sequence files
domain: genomics
status: draft
---

# Reference sequence files

## Summary

FASTA stores named biological sequences. In genomics, a reference FASTA often provides the actual sequence collection used by aligners, variant callers, and annotation tools. The biological reference identity and the physical FASTA file are related but not identical concepts.

## Core rules

- A FASTA record contains a header beginning with `>` followed by sequence data. A multi-FASTA contains multiple records.
- The sequence identifier is part of computational identity. Tools commonly use the first whitespace-delimited token of the header as the sequence name, but exact behaviour is tool-specific.
- Line wrapping is normally not part of the biological sequence, but it is part of the byte layout used by indexes such as `.fai`.
- Lower-case sequence can encode soft masking or other pipeline intent. Do not blindly change case when masking semantics might matter.
- Ambiguity symbols such as `N` are sequence content, not missing file data.
- A FASTA index such as `.fai` is derived from the exact file layout. Rewrapping, editing, recompressing, or replacing the FASTA can make an existing index stale.
- A sequence dictionary and a FASTA index serve different purposes. A dictionary can carry sequence names, lengths, checksums, and other metadata; an FAI primarily supports sequence retrieval from the indexed FASTA.
- A filename or assembly label does not prove exact reference identity. Sequence checksums or accessions provide stronger provenance.

## Required context

For a reference FASTA used in analysis, preserve as applicable:

- assembly or source collection
- source URL or accession
- file version or release
- sequence names and lengths
- checksums for the file and, where useful, individual sequences
- inclusion or exclusion of alternate, decoy, unplaced, and unlocalised sequences
- masking state
- mitochondrial sequence identity
- associated `.fai` and sequence dictionary files
- compression format and whether random access is supported by the toolchain

## AI behaviour

- Do not infer exact reference identity from a filename such as `hg38.fa`.
- Do not rename FASTA sequence identifiers to fix downstream compatibility unless the corresponding data files and sequence equivalence are understood.
- When an FAI or other derived index is present, treat it as belonging to the exact indexed FASTA, not as an independent reusable resource.
- Do not describe FASTA as storing sequence quality. FASTA stores sequence and identifiers or descriptions, not FASTQ-style per-base quality.
- Do not assume that upper-casing a reference is always harmless when repeat masking or case-sensitive preprocessing may matter.
- When reproducibility matters, prefer stable accessions or checksums over informal filenames.

## Common failure modes

### Stale FAI after reformatting

Rewrapping sequence lines can leave the nucleotide sequence unchanged while changing byte offsets. An FAI created for the previous file layout can therefore become invalid.

### Sequence name treated as assembly identity

A record headed `>chr1` does not establish whether the sequence came from GRCh37, GRCh38, T2T-CHM13, or another resource.

### Dictionary and index treated as interchangeable

A `.dict` or equivalent sequence dictionary can preserve reference metadata such as sequence checksums. A `.fai` supports indexed retrieval. They are related supporting files but not the same object.

## Authoritative standards

FASTA is an established sequence format with conventions implemented by many tools rather than a single genomics-wide normative specification. Use the documentation of the sequence provider and the indexing tool in the workflow. For samtools/htslib FAI behaviour, use current samtools and htslib documentation.

## Examples

### FASTA

```text
>chr1
ACCTGATCGTACGATCGATCGATC
```

The label `chr1` is a sequence identifier. It does not, by itself, identify an assembly.

### Reference provenance

A reproducible alignment workflow should retain the exact FASTA or a stable way to recover it, plus the sequence dictionary or checksums needed to confirm reference identity.

## Sources

- NCBI FASTA format guidance: https://www.ncbi.nlm.nih.gov/genbank/fastaformat/
- samtools faidx documentation: https://www.htslib.org/doc/samtools-faidx.html
- htslib faidx documentation: https://www.htslib.org/doc/faidx.html
- NCBI Assembly: https://www.ncbi.nlm.nih.gov/assembly/
