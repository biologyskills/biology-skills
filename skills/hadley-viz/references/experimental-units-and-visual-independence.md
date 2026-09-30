---
id: hadley-viz.experimental-units-and-visual-independence
title: Experimental units and visual independence
domain: hadley-viz
status: draft
---

# Experimental units and visual independence

## Summary

Biological data often have complex structure (e.g. samples nested within donors or repeated measures). A plot should not treat all observations as independent if they are not. The **experimental unit** (the entity randomized or independently sampled) and **observation unit** (measured item) must be identified. For example, multiple cells from the same patient are correlated: plotting them as independent points can exaggerate power. Always encode grouping or pairing: use separate panels for subjects, or connect paired points. The plot must preserve correct unit context to avoid pseudoreplication.

## Core rules

- **Identify true replicates:** Determine what was independently sampled (e.g. individual donors, litters, cultures).  
- **Map group structure:** If observations are nested (e.g. cells within a donor), use jittered points colored by donor or faceted by donor to indicate grouping.  
- **Paired data:** For matched samples (pre/post, mother/child), connect paired points or plot differences, not separate group means.  
- **Random effects:** If batch or plate is a factor, consider facet or random jitter to reveal batch effects.  
- **Sample size notes:** Always show n at appropriate level (e.g. n=5 donors, n=100 cells). Do not confuse “points” count with true independent replicates.

## Required context

- Knowledge of the study design: which level was randomized, what constitutes a replicate vs subsample.  
- Any blocking or batch variables (date, plate ID) that induce non-independence.  
- Subject identifiers if data are paired or longitudinal.

## AI behaviour

- **Check independence:** Before aggregating or testing, confirm if observations share an experimental unit. If unsure, ask or infer from metadata (e.g. same patient ID).  
- **Annotate plots:** Indicate paired lines or color-code grouping by replicate source.  
- **Flag pseudoreplication:** If an analysis or plot assumes independence incorrectly, raise an alert.  
- **Preserve design:** Don’t average replicates unless asked; instead, show variability at the replicate level.

## Common failure modes

- **Unmarked repeats:** Plotting all cell-level points without marking which donor they came from, and treating them as independent replicates.  
- **Disconnected pairs:** Showing pre/post means in separate boxplots without linking subjects hides within-subject trends.  
- **Ignoring batch:** Overlooking plate effects that cause clustering in a scatterplot.  
- **Overaggregation:** Aggregating data at donor level when the question targets cell-level distribution, losing granularity.

## Authoritative standards

- **Experimental design principles:** Follow ARRIVE/SIMRO guidelines: replicate = independent unit.  
- **Biology Skills experimental-design:** Validate independence as in the experimental-design skill. 

## Examples

### Example: Cell vs donor plot
- **Data:** Gene expression of single cells from multiple donors.  
- **Check:** Color points by donor ID or facet by donor; do not calculate one mean per donor without indicating variety.  
- **Good outcome:** UMAP scatter where each donor has a distinct color legend (legend labels = Donor IDs), or separate panels per donor showing distribution.

### Example: Paired measurements
- **Data:** Blood pressure before and after treatment in same patients.  
- **Check:** Use paired scatter/line plot or connected dot plot.  
- **Good outcome:** Each patient is a line connecting “before” to “after” point, rather than two unconnected boxplots labeled “Before/After”.

## Sources

- Biology Skills: experimental unit and replication rules.  
- Foundational stats/design (ARRIVE, etc.) – e.g. “Experimental unit is the biological entity independently assigned” (ARRIVE guidelines).
