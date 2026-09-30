---
id: hadley-viz
name: HadleyViz
description: Augmented data-visualisation rules combining ggplot2 grammar (Hadley R4DS) with biology-specific constraints.
---
# Data visualisation (HadleyViz)

## Summary

HadleyViz ensures ggplot2 plots remain biologically valid. Before plotting or interpreting any chart, an agent must apply domain rules: identify the biological question, confirm the true experimental unit (e.g. donor vs. cell) and independence, and preserve exact identities and denominators. Plots must not imply unsupported precision or causality. The agent should check data transformations, sample size, and appropriate uncertainties. For example, label genetic variants with full HGVS names (not shorthand) and include reference context. Use logarithmic scales only if zeros/detect limits are handled. Colour encodings must be accessible (colorblind-friendly) and, if used, accompanied by redundant markers or labels. In summary: *stop and verify context before visualisation, then apply the grammar of graphics without losing biological meaning*.

## Core rules

- **Identify the question and units:** Determine the exact biological question, experimental unit (e.g. sample, cell, clone), and observation unit. Check for nesting or pairing of observations.
- **Preserve identity:** Always encode true identities in labels (e.g. use full HGVS or accession numbers, not shorthand).
- **Represent scale and transformation:** Note any data transformation (log, normalisation, fold-change). Do not plot on log axes if zeros or negatives are present without a defined treatment.
- **Show uncertainty appropriately:** Choose error bars or CI only when sample size and distribution support inference. Label what uncertainty is shown.
- **Use meaningful encodings:** Colour, shape, size, facets must each match data type. Use high-contrast, colourblind-safe palettes and add redundant encodings (lines, patterns) for clarity.
- **Avoid misleading cues:** Do not imply continuity or causality where none exists. Do not extrapolate beyond data. Maintain consistent axis scales and aspect ratio unless justified by context.
- **Check denominators:** For compositional plots (percentages, proportions), ensure a common denominator is defined (e.g. use relative frequency bar with `position="fill"` and label axes accordingly).
- **Prevent overplotting:** If plotting large datasets, choose aggregation (hexbin, 2D density) or random sampling so points remain interpretable.
- **Annotate figure metadata:** Include necessary context in caption or labels (e.g. reference genome build, transcript ID, assay conditions) to make visualisation self-contained.

## Required context

The agent must collect before plotting:
- **Biological question type:** (distribution, group comparison, correlation, temporal pattern, classification, high-dimensional analysis, etc.)
- **Experimental design:** what are independent and repeated factors; the true replicate unit vs. pseudoreplicates.
- **Data types:** variable types (categorical, continuous, ordinal), measurement scales, and any censoring/detection limits.
- **Data processing:** any transforms, normalisation, filtering applied.
- **Scientific identity references:** genome assembly (e.g. GRCh38), transcript or protein reference (e.g. MANE IDs), sample/donor metadata.
- **Visualization context:** publication or presentation needs (colour scheme, output format, audience accessibility requirements).

## AI behaviour

When the skill is active, the agent must:
- **Stop and check** before plotting: do not automatically map all variables to aesthetics. Instead, verify units and question alignment first.
- **Preserve labels:** never truncate or replace precise variant or gene identifiers; keep reference accession and version if available.
- **Validate assumptions:** do not assume independence or linearity without data support. If data violate assumptions (e.g. log zero), report and adjust plan.
- **Apply redundancy:** if using colour to encode categories, ensure a secondary encoding (patterns, line type) is present.
- **Explicitly document:** always output figure captions or metadata strings that include key details (e.g. “Variant p.(Arg132His) on transcript NM_000546.6 (MANE Select)…”).
- **Correct failures:** if a chosen plot is inappropriate (e.g. violin on n<10, log on zeros), the agent should flag the issue and propose alternatives (e.g. raw dotplot, pseudo-count addition).

## Common failure modes

- **Ambiguous identity:** Labeling variants with gene symbols or truncated names (e.g. “TP53 R132” without reference) makes interpretation impossible.  
- **Overplotting:** Plotting millions of points with `geom_point()` without summarization leads to black blobs; a density or hexbin should be considered.  
- **Misleading transformations:** Using log scale on data containing 0 or missing values without handling them can hide data (should report and treat appropriately).  
- **Violin/box misuse:** Showing violin shapes for very small sample sizes (n<10) can be misleading; the agent should switch to dotplots or indicate the limited n.  
- **Paired data errors:** Comparing paired samples (e.g. before/after treatments in same subject) with separate boxplots ignores pairing. The agent should connect points or compute within-subject changes.  
- **Clustering artifacts:** Applying hierarchical clustering heatmaps without biological rationale can suggest patterns that are methodological. The agent should verify if clustering makes sense for the data context.  
- **Colour dependence:** Relying on red/green or low contrast schemes excludes colorblind viewers. The agent should use tested palettes or add labels.  

## Authoritative standards

- **HGVS Variant Nomenclature:** Use the Human Genome Variation Society standards for naming sequence variants.  
- **MANE Transcripts:** For human gene plots, prefer MANE Select or Plus clinical transcripts for consistency.  
- **R4DS/ggplot2 Guidelines:** Follow ggplot2 grammar (layers, geoms, aesthetics) as in *R for Data Science*, but augment with domain constraints.  
- **Statistical graphics lore:** Incorporate general best practices (e.g. Tufte’s data-ink ratio, Cleveland’s perception hierarchy) to ensure clarity.  
- **Accessibility:** Conform to WCAG contrast and redundancy guidelines.  

## Examples

### Example: Variant frequency bar plot
- **Data:** Allele counts per population.  
- **Check:** Use population denominators; plot relative frequencies if sample sizes differ. Label bars with exact values. Use HGVS (g., c., or p. notations) including transcript context.  
- **Good outcome:** Stacked bar (position="fill") of allele fractions per population, with legend specifying population and a caption stating reference genome and transcript.

### Example: Single-cell UMAP scatter
- **Data:** Thousands of cells per patient.  
- **Check:** Color by metadata only if category is small number; do not infer distance meaning. Add +/- shape or label for key clusters.  
- **Good outcome:** UMAP with cells colored by cell type (blue vs orange palette) and shapes for patient ID. Caption notes UMAP axes have no units.

## Sources

- Wickham *R for Data Science (2e)* – grammar of graphics and ggplot2 usage.  
- HGVS Nomenclature official guidelines – variant naming standards.  
- Biology Skills – experimental design and identity standards.  
- Accessibility guidelines (color contrast, redundant encoding).
