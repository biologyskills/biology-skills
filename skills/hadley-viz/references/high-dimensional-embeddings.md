---
id: hadley-viz.high-dimensional-embeddings
title: High-dimensional embeddings (PCA, UMAP, etc.)
domain: hadley-viz
status: draft
---

# High-dimensional embeddings (PCA, UMAP, etc.)

## Summary

Dimension-reduction plots (PCA, t-SNE, UMAP) compress many variables into 2D. **Axes have no direct unit**: interpret them as abstract components. Do not infer scales or absolute distances literally. Emphasize clusters or gradients qualitatively. Use colour/shape to encode known metadata (cell types, batch). Avoid overinterpreting spacing between clusters: embedding algorithms can distort distances. Always specify the algorithm and parameters in caption.

## Core rules

- **Axis meaning:** Do not label axes with original variable names; use generic terms (“Component 1”) and mention variance explained if PCA.  
- **No absolute scales:** Do not mark axes in data units (e.g. gene counts); they are algorithmic axes.  
- **Cluster caution:** Clusters seen are suggestive; don’t read quantitative gene expression values directly from these plots.  
- **Color encoding:** If coloring points, add a legend or labels, and include redundant cues if many categories.  
- **Reproducibility:** Record the random seed or parameters used, as different runs can produce different layouts.

## Required context

- Dimensionality reduction method and parameters used.  
- The proportion of variance explained by plotted dimensions (if PCA).  
- Metadata categories (labels) to encode in the plot.

## AI behaviour

- **Explain axes:** In captions or alt text, clarify axes (e.g. “PC1 and PC2 from PCA of log(expr)” or “UMAP1, UMAP2 from 30 PCs”).  
- **Avoid false precision:** Do not assign numeric interpretation to point positions beyond the relative clustering.  
- **Check coloring:** Ensure distinct categories use clearly separate colors/shapes.

## Common failure modes

- **Interpreting axes as variables:** Saying “higher PC1 means more gene X” (unsupported without loading information).  
- **Neglecting batch:** Plot looks clustered by batch but that context is hidden (should color by batch to reveal artifact).  
- **Comparing layouts:** Using UMAP as if distances are linear (they are not guaranteed meaningful in absolute terms).

## Authoritative standards

- **Dimension reduction norms:** Texts by Butcher & Fowlkes on PCA interpretability. Emphasize semantics: axes are mathematical constructs, not real measures.

## Examples

### Example: PCA scatter
- **Data:** Gene expression PCA colored by treatment.  
- **Check:** Axes labeled “PC1 (40% var)”, “PC2 (15% var)”. Legend with treatment names (blue, orange) and possibly shapes.  
- **Good outcome:** Caption “PCA of scaled expression (batch-corrected); shapes= timepoint, colors= treatment, two PCs explaining 55% total variance.”

### Example: UMAP clustering
- **Data:** scRNA-seq of immune cells.  
- **Check:** Color by cell type (distinct colors); caption notes “UMAP of first 30 PCs (Seurat default)”.  
- **Good outcome:** Legend lists cell types, each with distinct color. X/Y axes labeled “UMAP1”, “UMAP2”.
