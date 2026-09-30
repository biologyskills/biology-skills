---
id: hadley-viz.biological-identity-and-plot-labels
title: Biological identity and plot labels
domain: hadley-viz
status: draft
---

# Biological identity and plot labels

## Summary

Every data point in a biology plot represents a specific entity (e.g. a gene, transcript, variant, sample). Labels and annotations must preserve the full identity. For genetic variants, use exact HGVS notation tied to a reference sequence. Do not replace identifiers with shorthand or symbols that lack context. If the underlying analysis uses a specific transcript or isoform (e.g. MANE Select), mention it. Omitting these details can mislead or prevent reproducibility.

## Core rules

- **Exact naming:** Label points/lines with full identifiers (e.g. `NM_000546.6:c.524G>A (p.Arg175His)`), not ambiguous short forms. Preserve HGVS prefixes (`g.`, `c.`, `p.`) appropriately.
- **Reference context:** Include versioned accession and genome build when relevant. A gene symbol alone is not a substitute for a sequence reference.
- **Consistent symbols:** Use approved gene symbols only to supplement, not replace, precise labels. Do not embed symbols in HGVS strings (keep them separate).
- **Metadata annotation:** If plotting summary statistics, annotate axes or legends with sample source (e.g. tissue, donor ID) so the biological origin is clear.
- **Color/shape legends:** Legends encoding categories must clearly map to the exact categorical values (e.g. tissue type names, not index numbers).

## Required context

- Full accession/version of sequences (genome, transcript, protein) referenced by data.  
- Source of each data point (sample ID, cell line, patient, etc.).  
- If labels derive from pipeline (e.g. gene from differential analysis), know which reference was used (Ensembl or RefSeq ID, and version).

## AI behaviour

- **Preserve identifiers:** Do not truncate or generalize. If asked “What mutation is this?”, answer with complete HGVS description and reference accession (or state it is missing).  
- **Check consistency:** When summarizing groups (e.g. “genes upregulated”), ensure each name is uniquely defined (disambiguate synonyms).  
- **Report missing context:** If reference sequence or build is not known, note that labels may be incomplete.

## Common failure modes

- **Shorthand labels:** Plot uses “p.Arg132Leu” without transcript/coordinfo. Reader cannot tell which variant.  
- **Missing reference:** Using chromosome coordinates (chr1:123456) without specifying assembly (GRCh37 vs GRCh38) makes it non-reproducible.  
- **Inconsistent identifiers:** Mixing gene symbols and protein IDs in one figure, causing confusion about units.
- **Color-coded without legend:** Categories (e.g. cell types) shown only by colours; without a key, meaning is lost or misinterpreted.  

## Authoritative standards

- **HGVS Nomenclature:** Adopt the HGVS rules for variant descriptions (e.g. include “c.” or “p.” prefix, no spaces).  
- **MANE/Reference IDs:** Use MANE Select or RefSeq accession for transcripts; for proteins use UniProt or RefSeq when needed.  
- **Gene nomenclature:** Follow HUGO Gene Nomenclature (HGNC) for gene symbols if included, but never as sole label.

## Examples

### Example: Variant point plot
- **Data:** Variants on a gene vs. effect size.  
- **Check:** Label each point with full c.HGVS and p.HGVS or tooltip. Axis label “Amino acid change (HGVS p.)” plus caption “ref NM_XXX”.  
- **Good outcome:** X-axis tick labels are “p.(Arg175His)”, legend note “transcript NM_000546.6 (MANE)” (sources: HGVS standard).

### Example: Sample category colouring
- **Data:** Bars colored by tissue type.  
- **Check:** Legend entries are full tissue names (“Lung”, “Liver”), not codes; axis label “Sample ID” has prefix if needed (“Sample123_A”).  
- **Good outcome:** Legend says “Cell line origin: Lung, Liver, …”; each bar labeled with unique sample barcodes.

## Sources

- HGVS Nomenclature recommendations.  
- Biology Skills: variant nomenclature guidance (genomics).
