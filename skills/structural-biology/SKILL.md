---
name: structural-biology
description: Apply structural-biology correctness rules for protein and residue identity, isoforms, experimental constructs, structure mappings, predicted structures, confidence metrics, molecular state, and biological assemblies. Use when residue coordinates, experimental or predicted structures, molecular interactions, or structural explanations affect interpretation.
---

# Structural biology

Use this skill when a structural claim depends on the exact molecular object, residue numbering system, experimental construct, assembly, conformation, or prediction target.

The central question is:

> Which exact molecular object and structural state does this coordinate or model represent?

## Core rules

- A residue coordinate belongs to a particular sequence and numbering system.
- A gene name or protein label alone is not sufficient identity for a residue-level claim when isoforms or sequence versions differ.
- Distinguish canonical or representative protein sequences from alternative isoforms.
- Distinguish precursor numbering from mature-chain or processed-protein numbering.
- Distinguish native biological sequence from an experimental construct.
- Preserve PDB entry, biological assembly where relevant, chain or entity identity, and residue numbering when interpreting a structure.
- Do not assume PDB author numbering, PDB-assigned numbering, UniProt numbering, transcript-derived protein numbering, and construct numbering are identical.
- Missing coordinates in a structure do not imply absence from the underlying sequence.
- Engineered substitutions, truncations, linkers, tags, mutations, and fusion partners can materially change what a structure represents.
- A crystallographic contact is not automatically a physiological interaction.
- A predicted structure is a model, not direct experimental observation.
- Interpret confidence metrics only according to the quantity they measure.
- High local structural confidence is not evidence of correct function, interaction, ligand state, oligomeric state, disease mechanism, or mutation effect.
- A single structure or predicted conformation does not necessarily represent the full biological conformational ensemble.
- Preserve relevant ligands, cofactors, ions, nucleic acids, membranes, post-translational modifications, pH, or other state variables when they affect interpretation.

## AI behaviour

Before making a residue-level statement, establish:

1. protein accession and relevant isoform,
2. sequence version or exact sequence where needed,
3. numbering system,
4. construct or processing state,
5. PDB entry and chain or structural entity when applicable,
6. an explicit sequence-to-structure mapping when numbering systems differ.

Before interpreting a predicted structure, establish what was predicted and which confidence metric is being used. Separate confidence in local geometry from confidence in relative domain placement, interfaces, complexes, function, or biological mechanism.

Do not infer that a residue is unimportant or a variant benign because the local predicted structure has high confidence.

Do not infer mutation effects by comparing predicted structures unless the method is validated for that quantity.

## References

Read the relevant reference when the task depends on it:

- [`references/residue-identity-isoforms-and-construct-mapping.md`](references/residue-identity-isoforms-and-construct-mapping.md) for protein sequence identity, isoforms, processed proteins, experimental constructs, PDB chains, residue numbering, unresolved residues, and sequence-to-structure mapping
- [`references/predicted-structure-confidence-and-biological-state.md`](references/predicted-structure-confidence-and-biological-state.md) for interpretation of predicted structures, pLDDT, PAE, local versus global confidence, conformational state, ligands, complexes, mutation effects, and prediction-versus-experiment boundaries
