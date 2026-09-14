---
id: structural-biology.residue-identity-isoforms-and-construct-mapping
title: Residue identity, isoforms and construct mapping
domain: structural-biology
status: draft
---

# Residue identity, isoforms and construct mapping

## Summary

A residue number does not uniquely identify a residue unless the sequence and numbering system are known.

The same gene can produce multiple transcripts and protein isoforms. Protein databases can designate representative or canonical sequences. Experimental structures can use truncated, mutated, tagged, fused, or otherwise engineered constructs, and PDB residue numbering can differ from UniProt or transcript-derived numbering.

A statement such as `Arg117 in protein X` can therefore be incomplete even when the amino acid and position appear precise.

## Core rules

- A residue coordinate belongs to a particular protein sequence.
- Preserve the protein accession and relevant isoform when a residue-level claim matters.
- Preserve sequence version or exact sequence when changes could alter numbering.
- Distinguish representative or canonical protein sequence from alternative isoforms.
- Distinguish precursor numbering from mature-chain numbering after cleavage or processing.
- Distinguish native biological sequence from the sequence present in an experimental construct.
- Preserve PDB entry, chain or entity, and residue numbering system for structure-specific claims.
- Do not equate PDB residue numbering with UniProt numbering without an explicit mapping.
- Do not infer that a residue absent from atomic coordinates is absent from the protein sequence.
- Preserve engineered substitutions, truncations, linkers, tags, fusion partners, non-native residues, and unresolved regions when they affect mapping or interpretation.
- Do not silently project structural observations from one isoform or construct onto another.
- Use an explicit sequence-to-structure mapping such as SIFTS where available.

## Required context

For a residue-level structural claim, establish as applicable:

- gene identifier when biologically relevant
- transcript accession and version
- protein accession
- protein isoform
- sequence version or exact sequence
- precursor or mature-protein state
- experimental construct boundaries
- engineered mutations or tags
- PDB entry
- structural entity or chain
- author and archive numbering where they differ
- unresolved or missing coordinates
- mapping between structure and reference protein sequence

## AI behaviour

When given a residue statement such as:

```text
Arg117 is in the binding interface.
```

do not assume the coordinate is universal.

Recover or request:

```text
protein accession / isoform
sequence coordinate system
construct, if structural work is involved
PDB entry and chain, if applicable
sequence-to-structure mapping
```

If a publication, model, or database uses `canonical residue 117`, identify which authority defines that canonical sequence.

Do not silently convert residue coordinates across isoforms by adding or subtracting offsets. Sequence differences can include internal insertions, deletions, alternative exons, processing events, and construct modifications.

When a structure lacks coordinates for a region, distinguish unresolved structure from absent sequence.

## Common failure modes

### Gene name treated as residue identity

```text
BRCA1 residue 1000
```

does not by itself specify:

```text
transcript
protein isoform
protein accession
sequence version
construct
structure chain
```

### Canonical sequence treated as biologically unique

A database can designate a representative sequence for operational consistency. That designation does not establish that alternative isoforms are irrelevant in every tissue, disease, assay, or structural context.

### PDB numbering copied into protein annotation

A structural construct can start at a non-native residue, use insertion codes, omit unresolved residues, or preserve author numbering that differs from UniProt.

### Missing density treated as deletion

A residue with no resolved atomic coordinates can still be present in the experimental molecule and reference sequence.

## Authoritative standards

Use UniProt for protein sequence and isoform identity, PDB/mmCIF for structural entities and coordinates, and SIFTS for residue-level mappings between PDB structures and reference resources.

Use HGVS for exact sequence-variant nomenclature relative to a defined protein reference when that is the task. Use MANE when connecting human genomic and transcript-derived protein coordinates and an appropriate MANE transcript is required.

## Examples

### Incomplete residue statement

```text
Protein X Arg117
```

Better:

```text
UniProt: <accession>
isoform: <isoform>
sequence residue: Arg117
PDB: <entry>
chain/entity: <id>
PDB residue: <mapped residue>
mapping: SIFTS or explicit sequence alignment
```

Only include fields actually established by the source.

## Sources

- UniProt: https://www.uniprot.org/
- UniProt sequence and isoform help: https://www.uniprot.org/help/canonical_and_isoforms
- Protein Data Bank in Europe: https://www.ebi.ac.uk/pdbe/
- PDBe SIFTS: https://www.ebi.ac.uk/pdbe/docs/sifts/
- HGVS Nomenclature: https://hgvs-nomenclature.org/
- NCBI MANE: https://www.ncbi.nlm.nih.gov/refseq/MANE/
