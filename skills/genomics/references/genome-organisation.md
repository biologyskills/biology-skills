---
id: genomics.genome-organisation
title: Genome organisation
domain: genomics
status: draft
---

# Genome organisation

## Summary

DNA, chromosomes, genomes, genes, transcripts, and proteins describe different levels of biological organisation. Treating them as interchangeable creates errors in annotation, interpretation, and software interfaces.

## Core rules

- DNA is the molecular sequence material; a chromosome is a packaged DNA molecule or chromosomal structure; a genome is the complete genetic material considered for an organism or sample.
- A gene is a genomic feature with biological function, not a synonym for a transcript or protein.
- One gene can produce multiple transcripts and protein isoforms, and genes can overlap on the same genomic sequence.
- Not all genomic DNA belongs to protein-coding exons. Regulatory, non-coding, repetitive, and structural sequence can be biologically important.
- In humans, genomic analysis may involve both the nuclear genome and mitochondrial DNA, which have different inheritance, ploidy, and sequence conventions.
- A reference genome is a coordinate and sequence representation used for analysis. It is not a complete description of any person's diploid genome.
- Different cell types usually share the same inherited genome, but somatic mutation, mosaicism, rearrangement, copy-number change, and cancer can create cell-to-cell genomic differences.

## Required context

Preserve or establish as applicable:

- organism and genome compartment
- chromosome, contig, or sequence accession
- ploidy and sex-chromosome context when genotype interpretation depends on them
- gene identifier rather than gene symbol alone when stable identity matters
- transcript and protein identifiers for transcript-dependent or protein-dependent claims
- whether the material or variant is germline, somatic, mitochondrial, mosaic, or otherwise context-specific
- annotation release when genomic features are being named or compared

## AI behaviour

- Do not use gene, transcript, exon, chromosome, genome, and protein as interchangeable terms.
- Do not assume that one gene corresponds to exactly one transcript or one protein.
- Do not infer that non-coding sequence is functionally irrelevant because it does not encode protein.
- Do not describe a reference genome as a normal, ideal, or complete human genome.
- Do not assume every cell in an individual has an identical genome when mosaicism, somatic evolution, immune rearrangement, or cancer is relevant.
- Distinguish genetic from inherited. A genetic alteration can arise de novo or somatically and need not have been inherited from a parent.

## Common failure modes

### Gene symbol treated as a complete molecular object

A symbol such as `CFTR` identifies a gene but does not identify a transcript sequence, protein isoform, genomic assembly, or annotation release.

### Genome treated as coding genes only

Whole-genome data include coding and non-coding sequence, repetitive regions, structural variation, and mitochondrial sequence where captured. Gene-centric interfaces can hide these distinctions.

### Reference genome treated as a person's genome

A reference assembly provides sequences and coordinates for comparison. Individual genomes contain two homologous nuclear chromosome copies in most diploid contexts and can differ from the reference at many loci.

## Authoritative standards

Use HGNC for human gene nomenclature, Sequence Ontology for formal feature terms, and NCBI, Ensembl, or another relevant annotation authority for genomic feature definitions and identifiers. Biology Skills provides the conceptual distinctions and does not replace those maintained resources.

## Examples

### Distinct objects

`CFTR` is a gene on chromosome 7. A specific RefSeq or Ensembl transcript is one transcript model for that gene. A translated product from that transcript is a protein isoform. A genomic variant affecting the gene is represented relative to a reference sequence and may have different consequences on different transcripts.

### Genetic does not mean inherited

A tumour can contain somatic driver variants that are genetic changes but were not inherited through the germline.

## Sources

- National Human Genome Research Institute genetics glossary: https://www.genome.gov/genetics-glossary
- HGNC: https://www.genenames.org/
- Sequence Ontology: http://www.sequenceontology.org/
- NCBI Gene: https://www.ncbi.nlm.nih.gov/gene/
- Ensembl: https://www.ensembl.org/
