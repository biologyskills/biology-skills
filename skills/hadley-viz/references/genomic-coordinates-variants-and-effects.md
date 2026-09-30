---
id: hadley-viz.genomic-coordinates-variants-and-effects
title: Genomic coordinates, variants and effects
domain: hadley-viz
status: draft
---

# Genomic coordinates, variants and effects

## Summary

Plots involving genomic data must make clear the reference frame. If plotting variant locations, label axes with chromosome and coordinates (and assembly). If showing variant effects (e.g. protein domain plots), align coordinates to a reference sequence. Consistency is key: a genome browser track should match the same build. If multiple coordinate systems appear, distinguish them (e.g. chart for genomic vs. chart for protein domain). When comparing variants, preserve HGVS details so each point’s variant is traceable.

## Core rules

- **Reference genome:** Always specify reference assembly (GRCh38 etc.) when showing genomic positions.  
- **Transcript vs genome:** If plotting cDNA or protein positions, indicate transcript/protein ID and version. Align axes accordingly (e.g. amino acid position).  
- **Aligned views:** For multi-track plots (gene structure vs variant effects), synchronize genomic coordinates to avoid misinterpretation.  
- **Effect labeling:** When categorizing variant effects (synonymous, missense, etc.), use standard terms and, if colour-encoding, include legend with those terms.  
- **Overlap clarity:** In mutational landscape plots, ensure overlapping symbols (e.g. many variants at one site) are handled (stacking or jitter).

## Required context

- Assembly and gene/transcript identifiers used.  
- Variant annotation details (consequence, zygosity) if showing effect sizes.  
- Coordinate conversions used (e.g. genomic to protein index).

## AI behaviour

- **Axis annotation:** Always label axes with both coordinate number and context (e.g. “Position (nt from 5’ end of gene)”).  
- **Check consistency:** If merging data from different sources, ensure all variants are mapped to the same reference before plotting.  
- **Validate effects:** Do not infer a variant’s effect incorrectly; only encode consequences explicitly given.

## Common failure modes

- **Mixed assemblies:** Plotting GRCh37 coordinates on a GRCh38 reference, mixing up gene positions.  
- **Missing labels:** Omitting “Chr” or “bp” units on a genome-axis, leaving meaning unclear.  
- **Ambiguous variant points:** Using position-only labels for variants without alt allele info.

## Authoritative standards

- **Genome browser conventions:** Follow UCSC/Ensembl coordinate conventions (1-based vs 0-based) explicitly.  
- **Variant annotation databases:** If using ClinVar or gnomAD IDs, cite them in caption.

## Examples

### Example: Lollipop mutation plot
- **Data:** Protein domain schematic with mutations (positions 50, 150).  
- **Check:** X-axis in amino acid number (1–300), legend indicating protein name and transcript ID.  
- **Good outcome:** Caption “Protein NP_000469.2 (300 aa) with mutations at AA 50 (red) and 150 (blue)”.

### Example: Genomic interval plot
- **Data:** Region on chr7:50,000–100,000 showing gene exons and variants.  
- **Check:** X-axis “chr7 position (GRCh38)”. Variants plotted aligned to that scale; gene track labeled with gene name.  
- **Good outcome:** Axis ticks in Mb, subtitle “Region on chr7 (GRCh38) covering gene ABC1 (exons in green)”.
