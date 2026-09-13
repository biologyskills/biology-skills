---
id: genomics.inheritance-and-phase
title: Inheritance and phase
domain: genomics
status: draft
---

# Inheritance and phase

## Summary

Genetic interpretation depends on how alleles are distributed across chromosomes, cells, and family members. Zygosity, phase, segregation, inheritance model, penetrance, mosaicism, and phenotype are related but distinct concepts. Genetic does not necessarily mean inherited.

## Core rules

- Two heterozygous variants in the same gene are not automatically in trans.
- Cis and trans configuration can change interpretation under recessive disease models.
- Zygosity is meaningful only relative to ploidy and genomic context. Diploid assumptions do not apply universally to sex chromosomes, mitochondrial DNA, aneuploid regions, copy-number changes, or all tumour genomes.
- A de novo claim requires appropriate evidence about parental genotypes, sample identity, biological relationships, and assay sensitivity.
- Autosomal dominant, autosomal recessive, X-linked, mitochondrial, parent-of-origin, mosaic, and other mechanisms impose different constraints.
- A genetic cause or genetic alteration does not necessarily imply inheritance. Germline variants can be inherited or de novo, while somatic variants can drive disease without being transmitted through the germline.
- Mitochondrial inheritance and heteroplasmy require reasoning different from simple diploid nuclear genotypes.
- Pedigree segregation can support or oppose an interpretation without proving molecular mechanism.
- Genotype does not determine phenotype automatically. Penetrance, variable expressivity, age, environment, sex, genetic background, and other modifiers can matter.
- Inheritance belongs to a defined gene-disease, allele-disease, or genotype-disease relationship rather than to a gene symbol in isolation.

## Required context

Depending on the question preserve:

- sample identity and biological relationships
- sex-chromosome and ploidy context
- zygosity or allele fraction
- genotype quality and allele balance where relevant
- phase and evidence used to establish or infer it
- parental and other family genotypes
- pedigree structure
- germline versus somatic context
- mosaicism or mitochondrial heteroplasmy
- disease model and inheritance mechanism
- penetrance and age-related assumptions
- relevant phenotype and ascertainment information

## AI behaviour

- Do not infer compound heterozygosity from two heterozygous variants unless trans phase is established or appropriately supported.
- State when phase is unknown or inferred rather than directly established.
- Do not label a variant de novo solely because it is absent from a summary of parental findings.
- Do not infer a fixed inheritance pattern from a gene name. Resolve the relevant gene-disease relationship and mechanism.
- Do not assume no family history argues strongly against a genetic cause. De novo variants, recessive inheritance, reduced penetrance, small families, mosaicism, and incomplete ascertainment can remove an obvious pedigree pattern.
- Do not use dominant as a synonym for severe or recessive as a synonym for mild.
- Treat recurrence-risk percentages as conditional probabilities under stated assumptions, not deterministic family outcomes.
- Keep segregation evidence distinct from functional evidence and from clinical classification.

## Common failure modes

### Two variants treated as confirmed biallelic disease

Two heterozygous variants in the same recessive disease gene can be in cis on one homolog. Without phase or other supporting evidence, a trans genotype is not established.

### Genetic treated as inherited

A pathogenic somatic variant in a tumour is a genetic alteration but is not thereby hereditary. A germline de novo variant can cause genetic disease despite no prior family history.

### Twenty-five percent treated as one-in-four family destiny

For a simple autosomal recessive model with two heterozygous carrier parents, each pregnancy can have a 25 percent probability of inheriting both disease-associated alleles under the model. Four pregnancies do not guarantee one affected child.

### Inheritance label attached to a gene

The same gene can be associated with different diseases, allelic mechanisms, penetrance, or inheritance patterns. The disease relationship must be resolved explicitly.

## Authoritative standards

Use disease-specific and clinical genetics guidance for formal interpretation and counselling. Use ClinGen gene-disease and variant-curation resources where applicable. Use professional pedigree, HGVS, and genomic data standards for structured exchange rather than local shorthand.

## Examples

### Phase-aware wording

Prefer: "Two heterozygous variants were identified; phase is not established."

Use "compound heterozygous" only when the alleles are established or appropriately supported to be in trans.

### De novo wording

Prefer: "The variant was not detected in tested parental samples under the stated assay conditions" when biological parentage, sample identity, mosaicism sensitivity, or full de novo criteria have not been established.

## Sources

- ClinGen: https://clinicalgenome.org/
- American College of Medical Genetics and Genomics: https://www.acmg.net/
- GeneReviews: https://www.ncbi.nlm.nih.gov/books/NBK1116/
- NCBI MedGen: https://www.ncbi.nlm.nih.gov/medgen/
