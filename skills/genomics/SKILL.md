---
name: genomics
description: Apply biological and computational correctness rules for genomic references, sequencing data, coordinates, variant representation and qualification, assay callability, population frequency, HGVS nomenclature, transcripts, inheritance, gene expression, and molecular consequences. Use for genomics tasks where reference identity, assay scope, negative findings, frequency denominators, file semantics, selection criteria, annotation, genotype, phase, or biological context can change interpretation.
---

# Genomics

Use this skill for genome analysis, sequencing data, variant representation or selection, variant interpretation, genome annotation, pedigree reasoning, sequence-based prediction, population-frequency interpretation, and reporting of genomic results.

## Core rules

- Genomic coordinates, alleles, alignments, and annotations are reference-dependent. Establish reference identity at the level required by the task rather than assuming that an assembly label alone is sufficient.
- Genome assembly, patch release, exact reference sequence or FASTA, contig set, annotation release, transcript, and protein isoform are distinct objects and should not be collapsed into one identifier.
- File formats carry semantics. FASTQ quality, SAM/BAM/CRAM alignments, genomic intervals, and VCF/BCF records must be interpreted according to their own fields, coordinate conventions, metadata, and producing workflow.
- Preserve reference and alternate alleles, ploidy, genotype, phase, uncertainty, and transformation provenance when they affect variant identity or interpretation.
- Do not assume that different textual representations describe different biological alleles. Compare variants within a common reference and representation framework.
- Treat variant qualification as contextual rather than intrinsic. A variant qualifies only relative to declared criteria, their version, the application context, input data, and rule evaluation.
- Do not equate qualification or passage through a variant-selection rule with pathogenicity, statistical significance, causality, reportability, prioritisation, or clinical action.
- Treat scientifically consequential variant-selection criteria as part of the analysis specification. Preserve their field semantics, thresholds, logical structure, missing-value behaviour, external resources, and version when these affect which variants qualify.
- A negative genomic result is interpretable only relative to assay scope, sample-level callability, event-class sensitivity, and relevant analytical limitations.
- Coverage or read depth alone does not establish sensitivity to every relevant variant class.
- A no-call, absent VCF record, or filtered record is not automatically a reference genotype.
- Population allele frequency is a property of an observed allele in a defined resource, release, denominator, and sampled population. It is not a context-free property permanently attached to the variant.
- Distinguish allele count, allele number, allele frequency, global frequency, group-specific frequency, and maximum-group frequency.
- Do not turn missing population data or `AN=0` into evidence that an allele is absent or rare.
- When reporting sequence variants using HGVS, use the current HGVS Nomenclature recommendations and an appropriate versioned reference sequence. A gene symbol, genome-build label, or VCF coordinate alone is not a complete HGVS description.
- Coding, splice, RNA, and protein consequences can be transcript-dependent. Preserve the transcript and version when they affect the claim.
- Molecular consequence, predicted functional effect, experimentally measured effect, pathogenicity, penetrance, and phenotype are different levels of inference.
- Do not assume that two heterozygous variants in the same gene are in trans or that a gene has one fixed inheritance mechanism.
- Do not treat gene expression or regulatory activity as context-free properties of a gene.
- Treat indexes as derived access structures. They must correspond to the current data file and compatible ordering or compression requirements.

## AI behaviour

Before interpreting a coordinate, interval, allele, alignment, or other reference-dependent result, establish the relevant reference. Do not infer an assembly from chromosome naming alone. For reproducible computational work, preserve the exact reference sequence collection or FASTA and stronger identifiers such as accessions or digests where available.

Before converting between genomic formats, establish the coordinate convention, reference sequence, strand semantics, and representation rules of both formats. Do not apply a universal one-base offset or assume that normalization conventions are interchangeable.

Before interpreting VCF or BCF content, inspect the header and producing workflow. Do not give `PASS`, `QUAL`, `GQ`, an absent record, or a genotype string stronger meaning than the file supports.

Before interpreting a negative sequencing result, establish:

1. whether the relevant locus was intended to be interrogated,
2. whether it was callable in this sample,
3. which event classes the assay and pipeline could detect,
4. whether the relevant allele fraction, repeat size, structural event, copy-number state, or mitochondrial state was within validated scope,
5. whether the conclusion is absence, non-detection, or unresolved measurement.

Before applying, reproducing, or interpreting variant-selection criteria, establish the analysis context and the exact criteria set used. Determine the criteria version, input-field semantics, missing-value behaviour, logical structure, and material external resources. Do not reconstruct hidden selection logic from the resulting variant list alone, and do not silently treat missing values as satisfying a criterion. If qualification is reported, distinguish individual rule outcomes from any declared set-level qualifying status.

Before using a population-frequency value, establish the exact allele representation, resource and release, AC and AN where available, relevant population or ancestry grouping, and whether the site was callable. Do not interpret unavailable frequency as zero.

When exact sequence-variant nomenclature is required, use current HGVS Nomenclature. Establish the reference-sequence accession and version before generating the description. Do not convert VCF to HGVS by coordinate or string manipulation alone. For human transcript-based reporting, use the transcript specified by the source analysis or, when an appropriate standard transcript must be selected, follow current MANE guidance. Do not silently replace a supplied transcript. Mark predicted RNA or protein consequences as predicted, and validate complex or uncertain HGVS descriptions rather than extrapolating syntax.

Before reporting a coding or protein consequence, establish the transcript, transcript version where relevant, coding frame, strand, and genetic code. Do not present a Sequence Ontology consequence, Ensembl IMPACT category, or similar molecular annotation as a clinical pathogenicity classification.

Before inferring inheritance or disease from genotype data, establish relevant ploidy, phase, segregation, germline or somatic context, and the applicable gene-disease mechanism. Keep segregation, population frequency, computational prediction, functional evidence, and clinical interpretation as distinct evidence types.

Qualify expression and regulatory claims by their biological and technical context when that context affects interpretation. Do not infer protein abundance, activity, or universal biological relevance directly from an assay-specific RNA measurement.

When exact syntax, field definitions, identifiers, nomenclature, rule semantics, or ontology terms matter, use the current authoritative specification or maintained resource rather than reproducing a local substitute.

## References

Read the relevant reference when the task depends on it:

- [`references/genome-organisation.md`](references/genome-organisation.md) for DNA, chromosomes, genes, genomes, genomic compartments, and the distinction between genetic and inherited
- [`references/reference-genomes.md`](references/reference-genomes.md) for assemblies, patch releases, exact reference identity, sequence provenance, coordinate systems, and migration
- [`references/reference-sequence-files.md`](references/reference-sequence-files.md) for FASTA, sequence identifiers, FAI indexes, dictionaries, masking, and reference-file provenance
- [`references/sequencing-reads-and-quality.md`](references/sequencing-reads-and-quality.md) for FASTQ, paired reads, preprocessing, and Phred-scaled quality
- [`references/alignment-files-and-indexes.md`](references/alignment-files-and-indexes.md) for SAM, BAM, CRAM, alignment semantics, BAI, CSI, and CRAI
- [`references/genomic-intervals.md`](references/genomic-intervals.md) for BED, interval coordinate conventions, strand, and interval semantics
- [`references/variant-call-files-and-indexes.md`](references/variant-call-files-and-indexes.md) for VCF, BCF, gVCF, genotype fields, BGZF, TBI, and CSI
- [`references/variant-representation.md`](references/variant-representation.md) for allele identity, normalization, decomposition, equivalent representations, and VCF-versus-HGVS representation
- [`references/qualifying-variants.md`](references/qualifying-variants.md) for contextual variant qualification, explicit and versioned selection criteria, QVSS, input-field semantics, missing-value handling, external-resource provenance, and QV application records
- [`references/variant-nomenclature.md`](references/variant-nomenclature.md) for HGVS sequence-variant descriptions, versioned reference sequences, MANE transcript selection, molecular-level prefixes, and predicted versus observed consequences
- [`references/transcripts.md`](references/transcripts.md) for transcript identity, versions, isoforms, transcript selection, and transcript-dependent consequences
- [`references/coding-sequence-and-protein-consequences.md`](references/coding-sequence-and-protein-consequences.md) for coding frames, codons, genetic codes, molecular consequence terms, and protein consequences
- [`references/inheritance-and-phase.md`](references/inheritance-and-phase.md) for genotype, ploidy, inheritance, phase, segregation, mosaicism, heteroplasmy, and pedigree reasoning
- [`references/gene-expression.md`](references/gene-expression.md) for gene and transcript expression, assay context, cellular composition, normalization, and regulatory interpretation
- [`references/assay-scope-callability-and-negative-results.md`](references/assay-scope-callability-and-negative-results.md) for sample-level callability, assay scope, variant-class sensitivity, coverage limitations, and interpretation of negative genomic findings
- [`references/population-frequency-denominators-and-ancestry.md`](references/population-frequency-denominators-and-ancestry.md) for AC, AN, AF, callability, population and ancestry context, resource releases, and safe interpretation of population frequencies

