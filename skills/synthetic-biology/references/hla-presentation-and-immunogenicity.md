---
id: synthetic-biology.hla-presentation-and-immunogenicity
title: HLA presentation and immunogenicity
domain: synthetic-biology
status: draft
---

# HLA presentation and immunogenicity

## Summary

Peptide:HLA binding, antigen processing, cell-surface presentation, T-cell recognition, vaccine immunogenicity, tumour-cell recognition, and clinical efficacy are related but different biological states.

A prediction or measurement at one stage must not silently become evidence for a later stage.

For personalised neoantigen design, a target is more specific than:

```text
mutant peptide
```

It requires at least:

```text
exact peptide
+
exact HLA context
+
defined prediction or measurement
```

and the claim must state which biological step is actually supported.

## Core rules

- Preserve peptide sequence and HLA identity together when presentation is predicted or measured.
- Preserve HLA nomenclature at the resolution supplied by the assay and required by the prediction model.
- Do not discard additional HLA fields or expression suffixes when they can change sequence identity or biological interpretation.
- Record the HLA database or nomenclature release when exact reproducibility depends on it.
- For HLA class II predictions, preserve the complete molecule used by the model. In particular, HLA-DP and HLA-DQ predictions can depend on specific alpha and beta chain combinations.
- Do not collapse binding affinity, binding rank, eluted-ligand score, presentation score, or immunogenicity score into one generic `HLA score`.
- Interpret each model output according to the target on which that model and version were trained.
- A percentile rank is not automatically a probability.
- A predicted HLA binder is not automatically an endogenously generated peptide.
- A model trained on eluted ligands or presentation-related data still produces a prediction, not direct evidence that the peptide:HLA complex occurs on the relevant tumour cells.
- Detection of an HLA-associated peptide does not by itself establish productive T-cell recognition.
- T-cell recognition does not automatically establish clinically useful tumour control.
- A vaccine-induced response to a synthetic or vaccine-derived antigen does not by itself prove that the tumour naturally generates and displays the same target at a biologically relevant level.
- Germline HLA genotype does not establish the presentation state of every tumour clone. Somatic HLA loss, copy-number alteration, expression change, or defects elsewhere in antigen presentation can alter tumour presentation.
- Absence from immunopeptidomic detection is not proof of biological absence. Measurement sensitivity, sample amount, HLA abundance, peptide chemistry, and mass-spectrometric detectability affect observability.
- Preserve experimental validation according to what was actually measured rather than reducing heterogeneous assays to `validated`.
- When comparing HLA-prediction results, preserve model version, mode, peptide length, HLA molecule, raw output, rank, threshold, and any material input context.

## Required context

Preserve as applicable:

- exact peptide sequence
- peptide length
- patient HLA genotype
- HLA allele resolution
- HLA expression suffixes when relevant
- HLA reference-database release
- alpha-chain and beta-chain identity for class II heterodimers where required
- HLA class and locus
- prediction model
- complete model or package version
- prediction mode or model target
- raw prediction score
- percentile rank where produced
- threshold and threshold source
- tumour HLA copy-number state when relevant
- tumour HLA expression when relevant
- antigen-processing or presentation evidence
- immunopeptidomic assay details where used
- T-cell assay type
- responding T-cell population where resolved
- target cells used in functional testing
- whether tumour-cell recognition was tested directly
- whether evidence was measured before or after vaccination

## Evidence states

Use explicit language for the supported stage.

```text
sequence-derived candidate
```

The peptide was generated computationally from a defined source sequence.

```text
predicted HLA binder
```

A defined model predicts binding under its documented output semantics.

```text
predicted presentation / EL likelihood
```

A model designed for presentation-related or eluted-ligand behaviour assigns the corresponding prediction.

```text
HLA-associated peptide detected
```

The peptide was experimentally detected under a specified HLA-ligand or immunopeptidomic assay.

```text
T-cell reactive
```

A specified assay detected a T-cell response to the candidate.

```text
tumour-cell recognised
```

Relevant effector cells recognised tumour cells or an adequately representative tumour system in the stated experiment.

These labels are not interchangeable.

## AI behaviour

- State whether an HLA result concerns binding, processing, presentation-related prediction, HLA-ligand detection, recognition, or another defined target.
- Do not translate a percentile rank into a probability of presentation or immunogenicity.
- Do not describe a peptide as experimentally presented when the evidence is only computational.
- Do not describe a target as immunogenic when the evidence is only computational.
- Do not describe a vaccine-responsive peptide as proven to be naturally displayed by the tumour unless tumour-side presentation or recognition evidence supports that claim.
- Do not infer that all HLA alleles detected in germline material remain functionally available in the tumour.
- For class II molecules, do not omit a chain required to reconstruct the molecule used by the model or experiment.
- Do not silently truncate HLA allele nomenclature merely to simplify display.
- Do not use one model's default threshold as a universal biological boundary.
- When a prediction tool changes version, do not assume scores, ranks, binding cores, or classifications are interchangeable without checking the documentation.
- Treat a negative immunopeptidomics result as an observation under the assay's sensitivity, not an absolute proof that the peptide can never be presented.
- Keep pre-vaccination tumour evidence separate from post-vaccination immune-response evidence.

## Common failure modes

### Percentile interpreted as probability

```text
EL %Rank = 0.2
```

does not mean:

```text
99.8% probability of presentation
```

A percentile rank describes relative model output under the model's defined reference distribution.

### Binding treated as presentation

```text
strong predicted HLA binding
→ tumour presents peptide
```

skips antigen generation, processing, transport, HLA availability, and cell-surface presentation.

### Presentation-related prediction treated as observation

A model trained using eluted-ligand data predicts high ligand likelihood.

That is stronger than a pure binding-affinity statement but remains a model output rather than direct detection in the patient's tumour.

### Presentation treated as T-cell recognition

A peptide:HLA complex can exist without an available T-cell repertoire that recognises it productively.

### Vaccine response treated as tumour presentation

A patient develops T cells responsive to an encoded vaccine antigen.

This demonstrates an immune response in the vaccine context.

It does not by itself prove that the tumour generates and displays the same peptide:HLA complex at sufficient abundance for recognition.

### Germline HLA treated as immutable tumour state

```text
patient carries HLA-A*02:01
```

and:

```text
all tumour cells preserve functional presentation through HLA-A*02:01
```

are different propositions.

### Class II molecule incompletely identified

A result is stored as:

```text
HLA-DQ prediction
```

without preserving the DQA and DQB alleles used by the model.

The predicted molecule is not fully recoverable.

### `Validated neoantigen` without assay semantics

The word `validated` can conceal very different observations:

```text
synthetic peptide binding
HLA-ligand detection
ELISpot response
tetramer-positive cells
cytokine production
tumour-cell killing
```

Report the actual observation.

## Authoritative standards

Use IPD-IMGT/HLA and the WHO HLA nomenclature system for exact HLA allele names and maintained sequence identity.

Use the documentation of the actual prediction model for score definitions, rank calculations, thresholds, supported HLA molecules, and version-specific behaviour.

For experimental evidence, report the assay and observed quantity rather than translating heterogeneous assays into a locally invented universal validation scale.

## Examples

### Prediction with recoverable semantics

```text
peptide: <sequence>
HLA: HLA-A*02:01
model: NetMHCpan
version: 4.1
mode: EL
score: <raw value>
percentile_rank: <rank>
thresholds:
  source: <documented configuration>
```

Then state:

```text
predicted EL likelihood / presentation-related score under the stated model
```

rather than:

```text
confirmed immunogenic neoantigen
```

### Class II identity

For a DQ prediction, preserve both chains when the model is defined for that heterodimer:

```text
HLA class: II
locus: DQ
alpha allele: HLA-DQA1*<allele>
beta allele: HLA-DQB1*<allele>
model: NetMHCIIpan
version: <complete version>
```

### Evidence ladder

```text
1. patient-specific mutant sequence reconstructed
2. peptide:HLA interaction predicted
3. HLA-associated peptide experimentally detected
4. peptide-specific T-cell recognition detected
5. relevant tumour cells recognised
6. clinical outcome assessed
```

This is a provenance ladder, not a requirement that every useful candidate have all six measurements before design.

Missing downstream evidence should remain missing rather than being inferred from an upstream prediction.

## Sources

- IPD-IMGT/HLA Database: https://www.ebi.ac.uk/ipd/imgt/hla/
- HLA nomenclature: https://hla.alleles.org/pages/nomenclature/naming_alleles/
- NetMHCpan 4.1 documentation: https://services.healthtech.dtu.dk/services/NetMHCpan-4.1/
- NetMHCIIpan 4.3 documentation: https://services.healthtech.dtu.dk/services/NetMHCIIpan-4.3/
- Wells DK et al. Key Parameters of Tumor Epitope Immunogenicity Revealed Through a Consortium Approach Improve Neoantigen Prediction. Cell. 2020. https://doi.org/10.1016/j.cell.2020.09.015
- Zaghla BKQ et al. Systematic evaluation of neoepitope predictions challenges clinically observed T-cell responses and their impact on immune evasion. Journal for ImmunoTherapy of Cancer. 2026. https://doi.org/10.1136/jitc-2025-013271
- McGranahan N et al. Allele-Specific HLA Loss and Immune Escape in Lung Cancer Evolution. Cell. 2017. https://doi.org/10.1016/j.cell.2017.10.001
