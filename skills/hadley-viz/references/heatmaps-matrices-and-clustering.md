---
id: hadley-viz.heatmaps-matrices-and-clustering
title: Heatmaps, matrices and clustering
domain: hadley-viz
status: draft
---

# Heatmaps, matrices and clustering

## Summary

Heatmaps (matrix plots) often use clustering to order rows/columns. Clustering introduces subjective structure: dendrogram branches and order should be chosen carefully. If using hierarchical clustering, specify distance metric and linkage. Avoid implying ordered significance when rows are grouped by the algorithm. Always include scales/legends for color and note if data were scaled or normalized row-wise. Label axes with feature names. For multi-panel heatmaps, ensure alignment.

## Core rules

- **Data scaling:** Explicitly state if values are row- or column-normalized (Z-scores, percentile, etc.).  
- **Dendrogram keys:** If clustering is shown, include the dendrogram key or label clusters.  
- **Color legend:** Show mapping of values to colors with midpoint indicated (especially if diverging).  
- **Color order:** Use perceptually uniform color scales (e.g. viridis, or blue-white-red with neutral zero for divergent).  
- **Interpretation caution:** Warn that adjacency on heatmap is algorithmic, not necessarily biological co-regulation.

## Required context

- Clustering parameters (distance, method).  
- Whether data matrix was transformed (log, Z-score).  
- Meaning of matrix values (expression level, correlation).

## AI behaviour

- **Annotate clustering:** Mention any cut-off or cluster count if highlighting groups.  
- **Preserve labeling:** Do not omit row/column labels unless absolutely illegible. If too many, enable scrolling or summary view.  
- **Check continuity:** For time-series matrix, label columns in chronological order.

## Common failure modes

- **Unlabeled heatmap:** No color scale or missing legend, leaving colors uninterpretable.  
- **Reordered axes:** Presenting clustered heatmap as if original order (no indication of reordering).  
- **Misleading interpolation:** Using `geom_tile()` without accounting for missing cells (shows white gaps).

## Authoritative standards

- **Data viz guidelines:** Ensure color-breath is meaningful: Matplotlib’s fairness rules or similar guidelines on heatmap legibility.

## Examples

### Example: Gene expression matrix
- **Data:** Genes × samples expression.  
- **Check:** Annotate if rows are sorted by clustering; include a side color bar for sample groups. Legend shows color–expression mapping (red high, blue low).  
- **Good outcome:** Color key with labeled min/max, dendrogram branches annotated with cluster labels (Cluster 1, 2).

### Example: Distance matrix
- **Data:** Sequence similarity (0–100%) between genomes.  
- **Check:** Use grayscale or sequential palette; label each axis with strain names.  
- **Good outcome:** Darker diagonal for self-similarity, legend “Sequence identity (%)”.
