---
id: synthetic-biology.mrna-polyepitope-construct-design
title: mRNA polyepitope construct design
domain: synthetic-biology
status: draft
---

# mRNA polyepitope construct design

## Summary

A selected target set does not uniquely define an mRNA vaccine construct.

Target order, retained source sequence, boundaries, linkers, engineered substitutions, coding sequence, and regulatory sequence can change the physical RNA and the biological behaviour produced from it.

Keep distinct:

```text
selected target set
        ↓
ordered amino-acid construct
        ↓
exact coding nucleotide sequence
        ↓
complete mRNA design
        ↓
manufactured product
```

The final engineered construct must be evaluated as a sequence in its own right rather than assumed to inherit every property of its isolated components.

## Core rules

- Treat the selected target set and encoded construct as separate versioned objects.
- Preserve the exact ordered amino-acid sequence used to build the construct.
- Preserve the amount and identity of source-sequence context retained around each intended target.
- Preserve every linker, spacer, trimming operation, substitution, and boundary modification.
- Concatenating sequences creates novel junction context that did not exist in the source proteins.
- Evaluate junction-spanning peptide windows when they could create unintended presentation candidates relevant to the design.
- Do not assume that two constructs containing the same target set are biologically equivalent when their order or boundaries differ.
- Reordering, trimming, adding a linker, or modifying a boundary changes the construct and can require re-evaluation.
- Do not remove an unintended sequence feature by changing the construct without checking whether the change also affects intended antigen processing or target identity.
- Keep tumour-side source sequence and vaccine-side construct sequence distinct.
- Demonstrating that the vaccine construct can generate a peptide does not establish that the tumour naturally generates the same peptide.
- Preserve the exact coding nucleotide sequence separately from its translated amino-acid sequence.
- Synonymous nucleotide sequences should not automatically be treated as equivalent mRNA designs. Codon choice and sequence context can alter RNA structure, stability, translation, and other RNA-level behaviour while preserving the encoded protein.
- Preserve untranslated regions, poly(A) specification, cap specification, modified-nucleoside state, and other platform elements when they are part of the product identity or material to the analysis.
- Do not infer a proprietary platform sequence or manufacturing parameter when it has not been disclosed.
- Preserve the exact final digital sequence or another exact content identity when that sequence is transferred into manufacturing.
- A regenerated construct should receive a new design identity when material sequence, target order, design algorithm, or platform specification changes.
- Manufacturing QC, release testing, formulation, dosing, and process engineering are separate from the computational construct-design record.

## Source context versus construct context

A tumour-derived target begins in a native sequence context:

```text
native tumour protein
        ↓
cellular processing
        ↓
tumour peptide
        ↓
tumour HLA
```

The vaccine target can instead be embedded in:

```text
synthetic segment A
+
synthetic segment B
+
linker or boundary
+
synthetic segment C
        ↓
engineered polyepitope
        ↓
cellular processing
        ↓
vaccine-derived peptide
```

These processing contexts are not identical.

The intended shared object can be the same peptide:HLA target, but its route of generation differs.

Do not infer tumour-side processing solely from vaccine-side processing.

## Junction sequence

Consider two selected source regions:

```text
A = ABCDE
B = FGHIJ
```

The concatemer:

```text
ABCDE|FGHIJ
```

contains junction-spanning windows such as:

```text
...CDEFG...
...DEFGH...
...EFGHI...
```

that do not exist in either isolated source sequence.

Changing the order:

```text
B|A
```

creates different junctions.

Adding a linker:

```text
A|LINKER|B
```

also creates new boundaries.

A linker therefore changes the sequence problem rather than simply making the original junction disappear.

## Required context

Preserve as applicable:

- design identifier
- design version
- selected target identifiers
- ordered target list
- exact amino-acid source segment for each target
- source-segment boundaries
- intended peptide within each segment
- linker or spacer sequences
- boundary modifications
- engineered substitutions
- complete translated amino-acid sequence
- junction-analysis method
- HLA repertoire used for junction analysis
- prediction model and version
- exact coding nucleotide sequence
- nucleotide-sequence design algorithm and version
- exact content digest or equivalent identity
- 5-prime and 3-prime UTR identity when material
- poly(A) specification when material
- cap specification when material
- modified-nucleoside specification when material
- platform or backbone version
- relationship between computational design and manufacturing record

## AI behaviour

- Do not reconstruct a supposedly exact vaccine sequence from the selected neoantigen list alone.
- Do not assume that target order is arbitrary.
- Before comparing two constructs, compare the actual ordered sequences rather than only the set of targets they contain.
- Evaluate the final construct, not merely each isolated target, when junction-derived sequence is relevant.
- If a problematic junction is modified, re-evaluate the resulting boundaries.
- Do not say that a synthetic concatemer reproduces the native tumour protein environment.
- Do not interpret successful vaccine-side antigen processing as direct proof of tumour-side processing.
- Do not describe two mRNAs as the same design merely because they translate to the same amino-acid sequence when nucleotide-level behaviour matters.
- Do not discard the nucleotide sequence after translating it to protein.
- Preserve the final digital sequence supplied to manufacturing rather than only the upstream algorithm that generated it.
- When a patent describes linker, ordering, trimming, or sequence-engineering strategies, label them as patent-described embodiments unless independent evidence establishes production use.
- Do not fill undisclosed UTR, cap, poly(A), nucleoside, formulation, or manufacturing fields with common platform defaults.

## Common failure modes

### Correct targets, unrecoverable construct

The report stores:

```text
neoantigen_1
neoantigen_2
neoantigen_3
```

but not:

```text
order
source flanks
boundaries
linkers
amino-acid sequence
coding sequence
```

The construct cannot be reconstructed from the target list.

### Junction pseudoepitope ignored

Each target individually has an acceptable predicted profile.

After concatenation, a new high-ranking HLA-binding sequence spans the boundary.

The isolated-target analysis never evaluated it.

### Linker treated as sequence-neutral

A linker is inserted to alter one problematic boundary.

The system assumes the problem is solved without evaluating the two new boundaries created by the linker.

### Reordering treated as the same design

```text
A|B|C
```

and:

```text
C|A|B
```

contain the same selected targets.

They are not the same sequence and do not have the same junction contexts.

### Tumour processing inferred from vaccine processing

A T-cell response is generated against a peptide encoded by the vaccine concatemer.

The result is described as proof that the tumour naturally presents the same peptide.

The vaccine and tumour source proteins have different sequence contexts, so tumour-side processing remains a separate proposition.

### Amino-acid identity treated as mRNA identity

Two mRNA coding sequences translate to the same polyepitope protein.

The nucleotide sequences differ substantially.

They should not automatically be treated as identical product designs because RNA-level behaviour can differ.

### Patent embodiment treated as manufacturing recipe

A patent describes several possible strategies for reducing junctional epitopes.

The workflow records one of those strategies as though it were known to be used in every current clinical product.

The evidence does not justify that conclusion.

## Authoritative standards

There is no universal sequence architecture for personalised polyepitope mRNA vaccines.

Use product-specific validated design rules where available and preserve them as versioned design provenance.

Use patent disclosures as evidence of disclosed embodiments, not confirmation of undisclosed production methods.

Biology Skills should preserve the biological distinctions around construct design rather than prescribe one linker, codon strategy, UTR, cap, modified nucleoside, poly(A) length, formulation, or manufacturing process.

## Examples

### Versioned construct

```text
design: P017-v3

ordered_segments:
  1: target_A_source
  2: target_C_source
  3: target_B_source

boundaries:
  A|C: <defined sequence>
  C|B: <defined sequence>

protein_sequence:
  <exact amino-acid sequence>

coding_sequence:
  <exact nucleotide sequence>

coding_sequence_digest:
  sha256:<digest>

junction_analysis:
  HLA_set: <patient-specific set>
  model: <name>
  version: <version>
```

This is a different computational object from:

```text
selected_targets = [A, B, C]
```

### Construct revision

Version 1:

```text
A|B
```

A junction-spanning candidate is identified.

Version 2:

```text
A|linker|B
```

The revised design introduces:

```text
A|linker
linker|B
```

and should be evaluated as a new construct rather than assumed to have solved the original problem.

### Tumour and vaccine identity

```text
tumour source protein
        ↓
target peptide
        ↓
patient HLA
```

and:

```text
vaccine concatemer
        ↓
same target peptide
        ↓
patient HLA
```

can share the intended peptide:HLA identity.

The upstream proteins and processing contexts remain different.

## Sources

- ModernaTX, Inc. Personalized cancer vaccine epitope selection. US20210268086A1. https://patents.google.com/patent/US20210268086A1/en
- Ojalvo LS et al. Intismeran Autogene Therapy: An End-to-End Pathway From Tumor Tissue to Individualized Neoantigen Treatment for Patients With Cancer. JCO Oncology Advances. 2026. https://doi.org/10.1200/OA-25-00206
- Thess A et al. Sequence-engineered mRNA Without Chemical Nucleoside Modifications Enables an Effective Protein Therapy in Large Animals. Molecular Therapy. 2015. https://doi.org/10.1038/mt.2015.103
- Jin L et al. mRNA vaccine sequence and structure design and optimization: Advances and challenges. Journal of Biological Chemistry. 2025. https://doi.org/10.1016/j.jbc.2024.108015
