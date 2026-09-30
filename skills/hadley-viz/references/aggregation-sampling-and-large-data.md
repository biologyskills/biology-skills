---
id: hadley-viz.aggregation-sampling-and-large-data
title: Aggregation, sampling and large data
domain: hadley-viz
status: draft
---

# Aggregation, sampling and large data

## Summary

When plotting very large datasets (millions of points or high-dimensional matrices), raw plotting may be impossible or misleading. Instead, the agent should consider data reduction: aggregate by binning (hexagonal or 2D density), sample randomly/subset, or use summary plots (e.g. average trends). Any reduction must still reflect the biology (e.g. sample evenly from all groups). In heatmaps or feature embeddings, clustering should be done carefully (e.g. use k-means or subsampling for speed). The plot should note if sampling/aggregation was applied.

## Core rules

- **Avoid overplot:** If point density is too high, use `geom_hex()` or opacity. Alternatively, plot a representative random subset.  
- **Summaries vs raw:** For group trends (e.g. thousands of cells), consider showing median and spread per time-point rather than all points.  
- **Batch sampling:** If systematic sampling (e.g. every nth point), ensure it does not bias group proportions.  
- **High-D data:** For PCA/UMAP of huge gene sets, use only top principal components or a subset of cells for clarity.

## Required context

- Total data volume and memory constraints.  
- Whether the analysis requires full resolution or just patterns (trends vs detail).  
- If subsampling, record method (random seed, fraction).

## AI behaviour

- **Assess scale:** If data >10k points, automatically consider subsample or binning.  
- **Document reduction:** Add note in caption “points downsampled by N%” or “density estimates used”.  
- **Verify representativeness:** After sampling, ensure each condition/group is still present.

## Common failure modes

- **Sampling bias:** Subsetting without stratification (only sampling one condition) misrepresents the data.  
- **Garbled plot:** Too many overplotted points all appear black (no insight).  
- **False precision:** Aggregating into too few bins, oversmoothing the data.

## Authoritative standards

- **Scalable visualization:** Follow data visualization best practices to handle big data (Wickham recommends aggregation functions or sampling).  

## Examples

### Example: Scatter with 1M points
- **Data:** Genomic read counts for 10^6 variants.  
- **Check:** Use `geom_hex()` to show density of points, or randomly plot a fraction (e.g. 5%) with semi-transparency.  
- **Good outcome:** Heatmap-style scatter with hexagon cells colored by count; legend “hex bin counts”.

### Example: Heatmap of gene expression
- **Data:** 500 samples × 20,000 genes.  
- **Check:** Cluster only a subset of genes or use dimension reduction to show a heatmap of principal components.  
- **Good outcome:** Heatmap shows clustered PCs, not raw 20k genes, with annotation “based on top 1000 variable genes”.
