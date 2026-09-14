---
id: bioinformatics.entity-mapping-and-join-cardinality
title: Entity mapping and join cardinality
domain: bioinformatics
status: draft
---

# Entity mapping and join cardinality

## Summary

A valid identifier match does not imply a one-to-one biological relationship.

Genes, transcripts, proteins, isoforms, variants, samples, assays, ontology concepts, and database records are different entity types with different cardinalities and lifecycle rules. A computational join can therefore execute correctly while silently duplicating, dropping, collapsing, or misassigning biological observations.

## Core rules

- Declare the source entity type and target entity type before mapping.
- Preserve identifier namespace and version when they affect identity.
- Determine whether a mapping is one-to-one, one-to-many, many-to-one, or many-to-many before using it in analysis.
- Do not silently select the first result from an ambiguous mapping.
- Do not assume a gene maps to exactly one transcript or protein.
- Do not assume a name, symbol, alias, accession, or database row identifies the same object across resources.
- Treat unexpected row multiplication or row loss after a join as a semantic change that requires explanation.
- Do not collapse multiple mappings without an explicit biological reduction rule.
- Preserve the original source identifier and the mapping resource or release.
- Do not use row order or matrix position as biological identity unless ordering is explicitly guaranteed and verified.
- Before combining matrices or tables, verify that the entity identifiers and their order correspond.
- Distinguish exact equivalence from broader relationships such as `maps to`, `derived from`, `member of`, `transcript of`, `isoform of`, or `ortholog of`.

## Required context

For a consequential mapping or join, establish:

- source entity type
- source identifier namespace and version
- target entity type
- target identifier namespace and version
- mapping resource and release
- expected mapping cardinality
- how ambiguous mappings are handled
- how missing mappings are handled
- whether duplicate target mappings are allowed
- the intended analytical unit after the join
- row or entity counts before and after transformation
- whether ordering is meaningful and verified

## AI behaviour

Before joining or converting identifiers:

1. identify the biological entity represented on each side,
2. determine the possible mapping cardinalities,
3. define the intended unit of analysis after mapping,
4. inspect duplicates, missing mappings, and row-count changes,
5. preserve the source identifier and mapping provenance.

Do not write code that resolves an ambiguous biological mapping by selecting the first returned row unless that rule is explicitly justified.

If a join multiplies rows, determine whether the expansion represents valid biological multiplicity or accidental duplication.

If multiple matrices are combined, align them by stable identifiers rather than assuming the same row or column order.

If a mapping resource has changed, do not assume an earlier mapping is reproduced by the current release.

## Common failure modes

### Gene-level join silently duplicates variants

```python
variants.merge(transcripts, on="gene")
```

A gene can have multiple transcripts. The join can therefore produce multiple rows per variant even when the code is syntactically correct.

The correct action depends on the intended analysis:

```text
variant-level analysis
transcript-consequence analysis
gene-level aggregation
```

These are different analytical units.

### First mapping silently selected

An API returns several transcript matches and the first row is chosen because it is convenient. The result can depend on API ordering rather than a biological rule.

### Matrix axes assumed to correspond

```text
expression rows: sample_A, sample_B, sample_C
phenotype rows:  sample_B, sample_A, sample_C
```

Position-wise combination silently assigns the wrong phenotype to two samples.

### Symbol treated as stable identity

A human-readable gene symbol is useful for communication but may change over time. Stable identifiers and mapping provenance are safer for machine joins.

## Authoritative standards

Use the authority responsible for each identifier system and mapping relation. Examples include HGNC for human gene identity, Ensembl and RefSeq for genes and transcripts, MANE for explicitly matched RefSeq and Ensembl/GENCODE transcript pairs, UniProt for protein sequences and isoforms, and SIFTS for residue-level PDB-to-UniProt mapping.

Biology Skills does not prescribe one mapping database. It requires the mapping relation and its cardinality to be explicit.

## Examples

### Safe mapping contract

```text
source: HGNC gene ID
target: Ensembl transcript ID
expected cardinality: one-to-many
purpose: transcript consequence expansion
resource release: recorded
```

### Unsafe assumption

```text
one gene symbol
-> one transcript
-> one protein
-> one residue numbering system
```

Each arrow can be one-to-many or context-dependent.

## Sources

- HGNC: https://www.genenames.org/
- Ensembl: https://www.ensembl.org/
- NCBI MANE: https://www.ncbi.nlm.nih.gov/refseq/MANE/
- UniProt: https://www.uniprot.org/
- PDBe SIFTS: https://www.ebi.ac.uk/pdbe/docs/sifts/
- Wilkinson MD et al. The FAIR Guiding Principles for scientific data management and stewardship: https://doi.org/10.1038/sdata.2016.18
