---
id: structural-biology.predicted-structure-confidence-and-biological-state
title: Predicted structure confidence and biological state
domain: structural-biology
status: draft
---

# Predicted structure confidence and biological state

## Summary

Confidence in a predicted structure is confidence in a defined structural quantity under a particular model. It is not automatically confidence in biological function, interaction, conformational state, ligand occupancy, disease mechanism, or variant effect.

A high-confidence local structure can coexist with uncertainty in domain orientation, complex assembly, alternative conformations, disorder, binding state, environmental context, or functional consequence.

## Core rules

- Identify the exact sequence and model that produced the prediction.
- Interpret each confidence metric according to the quantity it measures.
- Local structural confidence is not functional confidence.
- High local confidence does not establish high confidence in relative domain orientation.
- A monomer prediction does not establish a physiological oligomer or interaction.
- A predicted interface is not direct evidence of binding in vivo.
- A predicted structure does not establish that one conformation is the dominant functional state.
- A single structure is not the complete conformational ensemble of a dynamic molecule.
- Check whether relevant ligands, cofactors, ions, nucleic acids, membranes, post-translational modifications, or partner molecules are represented.
- Separate predicted structure from experimentally determined structure.
- Do not infer pathogenicity or mutation effect from structural confidence alone.
- Do not use structural similarity or difference between independently predicted mutant and wild-type models as quantitative mutation-effect evidence unless the method is validated for that purpose.
- Preserve uncertainty in low-confidence, flexible, disordered, or relatively unconstrained regions rather than forcing a precise mechanistic story.

## Required context

For interpretation of a predicted structure, establish where relevant:

- sequence accession and isoform
- exact sequence or model input
- prediction method and version
- monomer or complex prediction
- local confidence metric
- relative-domain or pairwise confidence metric
- predicted assembly or partner context
- ligand, cofactor, ion, nucleic-acid, membrane, or modification context
- whether the relevant biological state is represented
- experimental structural evidence
- whether the claimed quantity has been validated for this use

## AI behaviour

Before using a structural prediction to support a biological claim:

1. identify what structural quantity was predicted,
2. identify the confidence metric and what it measures,
3. determine whether the claim concerns local geometry, domain arrangement, interface, complex, dynamics, function, or disease mechanism,
4. check whether required biological partners and state variables are present,
5. separate prediction from experimental observation.

For AlphaFold-style models, do not treat high pLDDT as evidence that relative domain positions are certain. Use the appropriate model confidence information, including PAE when relative placement is the question.

Do not describe a predicted conformation as the biological conformation without supporting evidence.

Do not claim a substitution is benign or pathogenic merely because a predicted local structure appears unchanged or well structured.

## Common failure modes

### High pLDDT escalated into functional certainty

```text
pLDDT = 95 around residue 117
```

supports high confidence in the predicted local structure for that region.

It does not by itself establish:

```text
the domain orientation is correct
the residue has no functional role
the interface exists in vivo
a substitution is benign
```

### One predicted state treated as an ensemble

Proteins can occupy several functional conformations. A single high-confidence model can represent one structurally plausible state without describing state populations or transitions.

### Missing biological partner ignored

A structure predicted without a ligand, membrane, cofactor, nucleic acid, or partner can be inadequate for a claim that depends on that component.

### Predicted mutant versus wild type overinterpreted

Two independently predicted models can look similar even when a mutation changes stability, kinetics, interaction affinity, expression, or conformational populations. Conversely, apparent structural differences can reflect prediction uncertainty.

## Authoritative standards

Use the documentation for the specific prediction system and version. For AlphaFold DB, interpret pLDDT, PAE, and other confidence outputs according to AlphaFold documentation.

Use PDB/PDBe for experimental structures and SIFTS for mapping them to reference protein sequences. Biology Skills does not convert structural confidence into functional or clinical evidence.

## Examples

### Local confidence versus relative placement

```text
domain A: high pLDDT
domain B: high pLDDT
between-domain PAE: high
```

Interpretation:

```text
each domain may have confident local geometry
relative orientation of the domains is uncertain
```

## Sources

- AlphaFold Protein Structure Database: https://alphafold.ebi.ac.uk/
- AlphaFold DB FAQ: https://www.alphafold.ebi.ac.uk/faq
- EMBL-EBI AlphaFold training, PAE: https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/pae-a-measure-of-global-confidence-in-alphafold-predictions/
- Jumper J et al. Highly accurate protein structure prediction with AlphaFold: https://doi.org/10.1038/s41586-021-03819-2
- PDBe: https://www.ebi.ac.uk/pdbe/
- PDBe SIFTS: https://www.ebi.ac.uk/pdbe/docs/sifts/
