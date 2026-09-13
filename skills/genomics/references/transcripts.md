---
id: genomics.transcripts
title: Transcripts
domain: genomics
status: draft
---

# Transcripts

## Summary

A gene can produce multiple transcripts and protein isoforms. The coding, splice, UTR, intronic, and protein consequences assigned to a genomic variant can therefore depend on the transcript model and transcript version used for annotation.

## Core rules

- A gene is not equivalent to a single transcript.
- The same genomic allele can have different consequences on different transcripts.
- Coding DNA and protein coordinates are transcript or isoform dependent.
- Transcript identifiers and transcript versions are distinct provenance. A version change can change the underlying sequence or annotation.
- Annotation release and transcript version are related but separate pieces of provenance.
- A preferred, canonical, MANE Select, or MANE Plus Clinical transcript is selected for a defined purpose. Selection does not make alternative transcripts biologically nonexistent.
- Transcript strand determines how genomic sequence is interpreted as transcript sequence.
- Transcript expression and disease relevance can depend on tissue, cell type, developmental stage, disease state, and other biological context.
- A consequence term is an annotation relative to a feature model. It does not by itself establish functional effect or pathogenicity.

## Required context

For transcript-dependent interpretation preserve as applicable:

- gene identifier
- transcript identifier
- transcript version
- annotation provider and release
- transcript strand
- coding sequence boundaries
- protein isoform or accession when a protein consequence is reported
- transcript-selection rule when one transcript is prioritised
- biological context when transcript usage or expression is material

## AI behaviour

- Do not report a transcript-dependent coding or protein consequence as if it were universal across the gene.
- State the transcript and, when reproducibility matters, transcript version used for a coding or protein consequence.
- If no transcript is given, do not invent one from the gene symbol alone.
- Do not use the word canonical as a synonym for biologically unique or universally clinically relevant.
- Keep transcript selection separate from transcript expression. A MANE or canonical transcript can be useful for consistent reporting without being the dominant transcript in every tissue.
- When exact sequence-variant nomenclature is required, consult current HGVS guidance and the referenced transcript sequence.
- When comparing annotation outputs, account for annotation release and transcript set differences before calling results contradictory.

## Common failure modes

### Protein consequence without transcript

`p.Arg123Trp` appears precise but residue 123 is defined on a particular protein sequence. Another isoform can have a different residue number or no corresponding coding consequence.

### Gene-level consequence treated as universal

A genomic variant can be exonic in one transcript, intronic in another, or outside another transcript entirely.

### Transcript version discarded

A bare accession can fail to identify the exact sequence used in a historical analysis if the accession has since gained a new version.

### Canonical transcript treated as biological truth

Software often displays one selected consequence for usability. That is a presentation choice, not proof that other transcript consequences are irrelevant.

## Authoritative standards

Use HGVS for exact variant nomenclature. Use MANE documentation for MANE transcript definitions. Use NCBI RefSeq, Ensembl, GENCODE, or the relevant annotation provider for transcript sequence and version information.

## Examples

### Better reporting

Prefer a transcript-dependent consequence reported with its transcript accession and version, plus the annotation source when relevant.

Avoid presenting a protein residue change without isoform or transcript context when alternative isoforms can change the coordinate or consequence.

## Sources

- HGVS Sequence Variant Nomenclature: https://hgvs-nomenclature.org/
- MANE project: https://www.ncbi.nlm.nih.gov/refseq/MANE/
- NCBI RefSeq: https://www.ncbi.nlm.nih.gov/refseq/
- Ensembl: https://www.ensembl.org/
- GENCODE: https://www.gencodegenes.org/
