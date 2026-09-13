---
id: genomics.reference-genomes
title: Reference genomes
domain: genomics
status: draft
---

# Reference genomes

## Summary

A genomic coordinate is meaningful only relative to a defined reference sequence.

Labels such as `GRCh38`, `GRCh38.p14`, `hg38`, or `chr17` provide useful context but do not necessarily identify the exact sequence collection used in an analysis. Reproducible genomic work should preserve reference identity at the level required to reconstruct the analysis.

Reference assembly, exact reference sequence, FASTA distribution, contig set, annotation release, and chromosome naming convention are related but distinct provenance.

## Core rules

- Never interpret a genomic coordinate without identifying its reference assembly or reference sequence.
- Prefer accessioned, versioned reference identifiers over informal names when precise reporting is required.
- An assembly label such as `GRCh38` does not uniquely identify an analysis reference.
- A patch designation such as `GRCh38.p14` identifies the assembly release more precisely, but still does not uniquely identify every FASTA derived from that assembly.
- Exact reference FASTAs can differ in alternate loci, patch sequences, decoys, unplaced or unlocalised sequences, masking, mitochondrial sequence, and contig naming.
- Browser names such as `hg19`, `hg38`, and `hs1` are ecosystem identifiers, not complete sequence provenance.
- A chromosome label such as `chr17` or `17` does not identify an assembly.
- Where a genomic variant is reported against a specific accessioned sequence, preserve the accession and version, for example an `NC_...` chromosome accession where appropriate.
- Annotation releases such as GENCODE, RefSeq, or Ensembl are separate from the reference assembly and must be reported independently when they affect interpretation.
- Liftover changes coordinates. It does not prove that the underlying allele, local sequence, annotation, or alignment is equivalent between references.
- Aligned reads remain aligned to the reference against which the alignment was generated until they are remapped.

## Reference identity levels

### Level 1: coordinate interpretation

For an isolated genomic coordinate or allele, preserve at minimum:

- species
- assembly or accessioned reference sequence
- contig or sequence identifier
- position
- reference allele
- alternate allele

Prefer:

```text
Homo sapiens
assembly: GRCh38
reference sequence: NC_000017.11
position: 43045700
REF: C
ALT: T
````

over:

```text
chr17:43045700 C>T
```

If the exact sequence accession is unavailable, report the assembly explicitly and state that the exact reference sequence was not provided.

### Level 2: reproducible analysis

For alignment, variant calling, benchmarking, or other reference-dependent computation, additionally preserve:

* assembly release or patch level when known
* assembly accession and version
* exact FASTA distribution or sequence collection
* contig names and lengths
* sequence accessions where available
* inclusion of alternate loci
* inclusion of patch sequences
* inclusion of decoy sequences
* inclusion of unplaced or unlocalised sequences
* mitochondrial reference sequence
* masking or other sequence transformation
* sequence dictionary
* checksum or content digest where available

A filename alone is not sufficient provenance.

For exact reproducibility, a content identifier such as a cryptographic checksum or GA4GH-compatible sequence digest is stronger than a human-readable filename.

### Level 3: biological annotation

When genes, transcripts, coding consequences, regulatory elements, or other annotations are interpreted, additionally preserve:

* annotation provider
* annotation release
* transcript accession and version where relevant
* protein accession and version where relevant
* annotation or consequence software version where relevant

Assembly identity and annotation identity must never be collapsed into one field.

## Human reference assemblies

Human work commonly encounters several distinct reference systems, including:

* GRCh37-derived references
* GRCh38-derived references
* T2T-CHM13-derived references
* pangenome or graph references

These are different coordinate and sequence systems.

Within an assembly family there may also be multiple operational reference distributions.

For example, a resource described as GRCh38 may use:

* the primary assembly
* the primary assembly plus unplaced or unlocalised sequences
* alternate loci
* patch sequences
* decoy sequences
* an analysis set
* masked or transformed sequence
* an aligner-specific reference package

Do not assume these references are computationally interchangeable.

## Patch releases

Patch releases must be distinguished from new major assemblies.

For GRCh38, patch releases can add or refine patch sequence while preserving the coordinate system of the primary assembly chromosomes.

This means two datasets can both use primary GRCh38 chromosome coordinates while differing in additional sequence content.

Therefore:

```text
GRCh38
```

is less precise than:

```text
GRCh38.p14
```

but:

```text
GRCh38.p14
```

still does not necessarily identify the exact FASTA used for alignment or variant calling.

When reproducibility matters, report both the assembly release and the actual reference sequence collection.

## AI behaviour

* Never silently assume GRCh38, GRCh37, or another reference.
* Never infer the assembly solely from `chr1` versus `1`.
* Do not treat `GRCh38` as sufficient provenance for a reproducible alignment or variant-calling workflow.
* When the patch release is known, preserve it rather than reducing `GRCh38.p14` to `GRCh38`.
* Do not invent a patch level when only `GRCh38` was supplied.
* When an exact reference accession or FASTA is available, preserve it.
* If only an assembly family is known, state that the exact analysis reference is unspecified.
* Do not claim two files use the same reference merely because both say `GRCh38` or `hg38`.
* Before merging coordinate-based datasets, verify assembly, reference sequence compatibility, contig identities, and coordinate conventions.
* Do not repair reference incompatibility by renaming contigs unless the underlying sequences are known to be identical.
* Do not treat liftover as equivalent to remapping.
* Keep reference assembly, exact FASTA, gene annotation, and transcript version as separate provenance fields.

## Common failure modes

### Coordinate without a reference

Incorrect:

```text
chr17:43045700 C>T
```

The coordinate cannot be interpreted uniquely without reference context.

### Assembly family treated as exact provenance

Insufficient for a reproducible pipeline:

```text
reference: GRCh38
```

Better:

```text
assembly: GRCh38.p14
assembly accession: <accession.version>
reference FASTA: <distribution or sequence collection>
reference digest: <checksum or sequence digest>
```

Only report identifiers actually used by the analysis.

### Patch level treated as exact FASTA identity

```text
GRCh38.p14
```

identifies an assembly release, but different FASTA distributions can still contain different sets of sequences or transformations.

### Browser name treated as assembly identity

```text
hg38
```

is useful ecosystem terminology but should not replace accessioned reference provenance in reproducible work.

### Annotation confused with assembly

```text
GRCh38
```

does not specify whether genes or transcripts were assigned using GENCODE, RefSeq, Ensembl, or another annotation release.

### Contig renaming treated as reference conversion

Changing:

```text
1
```

to:

```text
chr1
```

changes an identifier, not the underlying sequence or coordinate system.

## Reporting examples

### Human-readable variant report

```text
Species: Homo sapiens
Assembly: GRCh38
Reference sequence: NC_000017.11
Variant: g.43045700C>T
```

Where transcript interpretation is involved:

```text
Assembly: GRCh38
Genomic reference: NC_000017.11
Transcript: <accession.version>
Annotation release: <provider and version>
```

### Reproducible computational analysis

```text
Species: Homo sapiens
Assembly: GRCh38.p14
Assembly accession: <accession.version>
Reference FASTA: <exact reference distribution>
Reference digest: <checksum>
Contig dictionary: <recorded>
Annotation: <provider and release>
```

The exact values must come from the files or workflow actually used. Do not infer them from the label `GRCh38`.

## Migration

If reads were aligned against a GRCh37-derived reference and a project moves to a GRCh38-derived reference, lifting the final variant coordinates does not convert the original BAM or CRAM into a GRCh38 alignment.

The reads remain aligned against their original reference until they are remapped.

Variant conversion should also verify REF alleles and representation against the target sequence.

## Authoritative standards

Use authoritative resources rather than maintaining local copies of reference definitions:

* NCBI Assembly and sequence records for accessioned assembly and sequence provenance
* Genome Reference Consortium for GRC assemblies and patch structure
* UCSC and Ensembl for their distributed reference ecosystems
* GA4GH refget and related standards for content-based sequence identification where appropriate
* HGVS for sequence-variant nomenclature using accessioned reference sequences

## Sources

* Genome Reference Consortium: https://www.ncbi.nlm.nih.gov/grc/
* NCBI Assembly: https://www.ncbi.nlm.nih.gov/assembly/
* NCBI Nucleotide: https://www.ncbi.nlm.nih.gov/nuccore/
* GA4GH refget: https://www.ga4gh.org/product/refget/
* HGVS nomenclature: https://hgvs-nomenclature.org/
* UCSC Genome Browser: https://genome.ucsc.edu/
* Ensembl: https://www.ensembl.org/
* T2T Consortium: https://github.com/marbl/CHM13
* Human Pangenome Reference Consortium: https://humanpangenome.org/

