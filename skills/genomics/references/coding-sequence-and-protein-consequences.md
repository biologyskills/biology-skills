---
id: genomics.coding-sequence-and-protein-consequences
title: Coding sequence and protein consequences
domain: genomics
status: draft
---

# Coding sequence and protein consequences

## Summary

A predicted protein consequence is derived from a particular transcript, coding sequence, reading frame, strand, and genetic code. Codon-level annotation describes a molecular consequence of sequence representation; it is not a clinical pathogenicity classification.

## Core rules

- Translation reads mRNA 5-prime to 3-prime in codons of three nucleotides within a defined reading frame.
- In a simple coding example, the coding DNA strand has the same base order as mRNA except T replaces U; the template strand is complementary and antiparallel.
- A genomic allele cannot be translated without the relevant transcript, strand, coding boundaries, and reading frame.
- Human mitochondrial translation differs from the standard nuclear genetic code at several codons.
- Substitutions, insertions, and deletions can have different consequences across transcripts and coding frames.
- A synonymous consequence does not prove absence of biological effect.
- Sequence Ontology terms and Ensembl IMPACT categories describe predicted molecular consequence or heuristic severity, not clinical pathogenicity.
- Protein notation is reference-sequence dependent. Exact HGVS nomenclature must use the appropriate reference sequence and current HGVS rules.

## Required context

For a coding or protein consequence preserve:

- genomic reference sequence
- gene and transcript identifier
- transcript version
- transcript strand
- coding sequence boundaries and reading frame
- protein accession or isoform when reporting protein coordinates
- genetic code used
- annotation software and release when consequence terms are generated computationally
- distinction between predicted consequence and experimentally measured molecular effect

## AI behaviour

- Do not translate a genomic variant into a protein change without establishing transcript and coding-frame context.
- Do not assume the standard nuclear genetic code for mitochondrial sequence.
- Do not infer pathogenicity from a consequence term such as missense, frameshift, HIGH, MODERATE, or stop-gained.
- Do not describe a synonymous variant as biologically neutral solely because the amino acid is unchanged.
- Do not use a copied consequence-severity table as a substitute for the current annotation provider or Sequence Ontology definition.
- When exact amino-acid or HGVS notation matters, use the current authoritative sequence and nomenclature standard.
- Separate predicted consequence from functional evidence. A predicted stop-gained consequence does not by itself demonstrate transcript degradation, protein truncation, disease mechanism, or phenotype.

## Common failure modes

### Protein change derived from gene name alone

A gene symbol does not define one coding sequence. Alternative transcripts can change codon position, reading frame, or whether the genomic variant is coding at all.

### Ensembl IMPACT treated as pathogenicity

`HIGH`, `MODERATE`, `LOW`, and `MODIFIER` are annotation categories used for predicted consequence severity. They are not clinical variant classifications.

### Synonymous treated as no effect

No amino-acid change does not exclude splice, regulatory, RNA, or translational effects.

### Nuclear code applied to mitochondrial DNA

Several mitochondrial codons differ from the standard nuclear genetic code. Using the wrong code can assign the wrong amino acid or stop consequence.

## Authoritative standards

Use NCBI genetic-code resources for translation tables, HGVS for exact sequence-variant nomenclature, Sequence Ontology for formal consequence terms, and the current annotation-provider documentation for provider-specific consequence categories.

## Examples

### Coding-strand example

```text
DNA coding strand:  ATG GAA TGG
mRNA:               AUG GAA UGG
protein:            Met Glu Trp
```

This simple correspondence assumes that the displayed DNA is the coding strand and that the reading frame is already established.

### Molecular consequence is not clinical classification

A `stop_gained` annotation states that the selected transcript model predicts creation of a premature termination codon. Clinical interpretation still requires evidence about gene-disease mechanism, transcript relevance, nonsense-mediated decay, population frequency, segregation, functional data, and other applicable evidence.

## Sources

- NCBI genetic codes: https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi
- HGVS Sequence Variant Nomenclature: https://hgvs-nomenclature.org/
- Sequence Ontology: http://www.sequenceontology.org/
- Ensembl calculated variant consequences: https://www.ensembl.org/info/genome/variation/prediction/predicted_data.html
