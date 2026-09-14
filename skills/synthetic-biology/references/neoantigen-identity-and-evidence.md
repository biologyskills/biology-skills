---
id: synthetic-biology.neoantigen-identity-and-evidence
title: Neoantigen identity and evidence
domain: synthetic-biology
status: draft
---

# Neoantigen identity and evidence

## Summary

A personalised neoantigen candidate is not completely identified by a gene name, genomic variant, protein position, or mutation label.

The designed object is derived through a chain of patient-specific biological and computational transformations:

```text
tumour specimen
      ↓
somatic genomic event
      ↓
patient-specific transcript / haplotype sequence
      ↓
altered source sequence
      ↓
candidate peptide
      ↓
patient-specific presentation context
```

Every step can change the resulting target.

Preserve enough identity and provenance to reconstruct this chain rather than retaining only a convenient label such as `GENE p.X123Y`.

## Core rules

- Treat the patient, specimen, genomic event, transcript, altered source sequence, peptide, and peptide:HLA candidate as distinct objects.
- Establish tumour specificity from the actual tumour-normal evidence. Absence from a normal call set is not proof of absence when the site was inadequately measured or the normal specimen is biologically complicated.
- Preserve genomic reference identity, coordinates, REF and ALT alleles, and the representation used for the source event.
- Preserve the transcript accession and version used to derive coding or protein sequence.
- Do not infer an exact peptide from a gene symbol and protein position alone.
- Construct candidate sequence from the relevant patient-specific sequence context where available, not automatically from an unmodified population reference.
- Account for nearby germline or somatic variation when it changes the source sequence used to generate a candidate.
- Establish phase when multiple heterozygous variants must lie on the same molecule to define the source sequence. If phase is unresolved and materially changes the peptide, preserve the plausible alternatives or mark the sequence unresolved.
- Keep the focal genomic event separate from the final peptide. One event can generate multiple transcript-dependent or overlapping peptides and multiple peptide:HLA candidates.
- Preserve the corresponding self sequence used for comparison and record how it was derived.
- Distinguish gene expression, transcript expression, and mutant-allele expression.
- When mutant RNA support matters, retain variant-supporting and informative read counts where practical rather than only a rounded VAF.
- Do not treat equal VAF values obtained from substantially different read counts as equally precise evidence.
- Do not treat DNA VAF as cancer-cell fraction or clonality without accounting for tumour purity, local copy number, and model assumptions.
- Distinguish clonality inferred by a model from directly observed sequence measurements.
- A coding DNA event does not establish that the corresponding mutant transcript persists or that the resulting peptide is generated. Transcript usage, splicing, RNA degradation, and nonsense-mediated decay can alter the realised antigen source.
- Do not assume that all variant classes can be projected into peptide sequence using the same transformation. Substitutions, multi-nucleotide variants, indels, splice alterations, fusions, and other events require event-appropriate sequence reconstruction.
- Preserve the original source event after derived sequences have been generated.

## Required context

Preserve as applicable:

- patient or subject identifier
- tumour specimen identifier
- matched normal specimen identifier
- tumour site and sampling time when relevant
- normal specimen source
- DNA and RNA assay identity
- genomic reference assembly or accessioned sequence
- genomic variant representation
- REF and ALT alleles
- somatic-call provenance and material quality evidence
- tumour-in-normal or other contamination assessment when relevant
- transcript identifier and version
- annotation provider and release
- protein accession or isoform where used
- proximal variants that alter the source sequence
- phase or haplotype evidence when relevant
- mutant source sequence
- corresponding patient-specific self sequence
- generated peptide sequence
- peptide boundaries within the source sequence
- RNA abundance measurement
- mutant and reference RNA read support where used
- tumour purity estimate when used
- local copy-number state when used
- inferred cancer-cell fraction or clonality and its method
- candidate-generation software and version
- external reference-resource versions

## AI behaviour

- Do not create an exact neoantigen peptide from a gene symbol and amino-acid substitution unless the required transcript and sequence context are established.
- Do not silently choose a canonical transcript when the source analysis used another transcript or when transcript choice changes the peptide.
- Do not ignore a proximal variant merely because it is not the focal somatic mutation. Determine whether it changes the sequence actually present on the relevant molecule.
- Do not combine nearby heterozygous variants into one peptide without phase or another justified basis for placing them on the same haplotype.
- Do not use a generic reference peptide as the patient's self comparator when known patient-specific variation changes that sequence.
- Do not call a variant tumour-specific solely because it is absent from a normal variant list. Determine whether the matched normal measurement could resolve it and whether the normal specimen itself can contain tumour-derived or acquired clonal variation.
- Do not describe a candidate as expressed merely because its source gene has non-zero gene-level RNA abundance.
- Keep total expression, transcript expression, mutant-allele expression, and peptide presentation separate.
- Do not call a variant clonal from raw VAF alone.
- When a frameshift, splice alteration, or other transcript-disrupting event creates novel coding sequence, consider whether the relevant RNA is expected and observed to persist.
- Preserve uncertainty when multiple transcript, haplotype, or sequence reconstructions remain plausible.

## Common failure modes

### Mutation label treated as target identity

```text
GENE p.Arg123Gly
```

does not identify:

```text
which transcript
which transcript version
which protein isoform
which nearby patient variants
which haplotype
which source sequence
which peptide window
which HLA molecule
```

The display label can be useful for humans while remaining insufficient for reconstruction.

### Reference sequence substituted for the patient haplotype

The focal somatic substitution is placed into a standard reference sequence even though the patient carries a nearby in-phase germline or somatic variant.

The resulting candidate can be a peptide that does not occur in that patient's tumour.

### Unphased variants combined

Two nearby heterozygous variants are placed into one synthetic source sequence because both appear in a VCF.

If they are in trans, that combined peptide may not exist on either chromosome.

### Normal sample treated as infallible germline truth

A variant is removed from the somatic candidate set because supporting reads are present in the matched normal.

Tumour-in-normal contamination, clonal haematopoiesis, sample source, depth, and technical artefact can complicate this interpretation. The normal specimen is an observation with its own biology and assay limitations.

### DNA VAF treated as clonality

```text
VAF = 0.40
→ 40% of tumour cells carry the mutation
```

is not generally valid.

Tumour purity, local copy number, zygosity, and subclonal structure alter the relationship between VAF and cancer-cell fraction.

### Gene expression treated as mutant expression

```text
gene TPM > 0
```

supports RNA abundance assigned to the gene under the stated quantification.

It does not by itself establish expression of the mutant transcript or allele.

### Frameshift treated as guaranteed antigen source

A DNA frameshift predicts altered coding sequence under a selected transcript model.

It does not establish that the resulting RNA escapes degradation, is translated, or generates the predicted peptide.

### Overlapping peptides collapsed into one object

Several peptide windows containing the same altered residue are stored as:

```text
mutation X neoantigen
```

Their processing, HLA interaction, presentation, and recognition can differ.

Preserve the exact peptide sequences.

## Authoritative standards

Use the relevant genomics standards for upstream molecular objects rather than defining a neoantigen-specific substitute.

Use:

- HGVS when exact sequence-variant nomenclature is required
- accessioned genomic references for genomic identity
- RefSeq, Ensembl, GENCODE, or the source annotation system for transcript identity
- MANE when an appropriate standard human transcript is required, while preserving the transcript actually used by the source analysis
- the relevant HLA nomenclature authority for HLA identity

There is no single identifier that replaces the complete source-to-peptide lineage.

## Examples

### Recoverable candidate identity

Insufficient:

```text
gene: GENE1
mutation: p.Arg123Gly
neoantigen: PEPTIDE1
```

Prefer a representation capable of retaining:

```text
subject: P017
tumour_sample: T02
normal_sample: N01

source_event:
  assembly: GRCh38
  chromosome: <contig>
  position: <position>
  ref: <allele>
  alt: <allele>

transcript:
  accession: <accession.version>
  annotation: <provider release>

sequence_context:
  phase: <resolved / unresolved / not applicable>
  proximal_variants: <identifiers>
  self_source_sequence: <sequence>
  mutant_source_sequence: <sequence>

candidate:
  peptide: <exact amino-acid sequence>
  source_start: <position in source sequence>
  source_end: <position in source sequence>

rna_evidence:
  transcript_abundance: <value and unit>
  mutant_reads: <count if available>
  informative_reads: <count if available>

clonality:
  value: <estimate if used>
  method: <method and version>
```

Unavailable fields should remain unavailable rather than being reconstructed from assumptions.

### Same VAF, different evidence

```text
Candidate A:
mutant RNA reads = 10
informative reads = 20
VAF = 0.50

Candidate B:
mutant RNA reads = 500
informative reads = 1000
VAF = 0.50
```

The point estimates are equal.

The amount of sequence evidence is not.

The appropriate uncertainty model can be more complex than a simple binomial model because read errors, mapping, duplication, allele-specific effects, and other dependencies can matter, but the ratio alone should not erase the denominator.

### Unresolved haplotype

```text
focal somatic variant: heterozygous
nearby germline variant: heterozygous
phase: unknown
```

If the nearby variant changes the peptide, the alternative sequence configurations should remain distinct possibilities until phase is resolved sufficiently for the intended design.

## Sources

- Hundal J et al. Accounting for proximal variants improves neoantigen prediction. Nature Genetics. 2019. https://doi.org/10.1038/s41588-018-0283-9
- Carter SL et al. Absolute quantification of somatic DNA alterations in human cancer. Nature Biotechnology. 2012. https://doi.org/10.1038/nbt.2203
- Taylor-Weiner A et al. DeTiN: overcoming tumor-in-normal contamination. Nature Methods. 2018. https://doi.org/10.1038/s41592-018-0036-9
- Litchfield K et al. Escape from nonsense-mediated decay associates with anti-tumor immunogenicity. Nature Communications. 2020. https://doi.org/10.1038/s41467-020-17526-5
- HGVS Sequence Variant Nomenclature: https://hgvs-nomenclature.org/
- MANE: https://www.ncbi.nlm.nih.gov/refseq/MANE/
- GENCODE: https://www.gencodegenes.org/
