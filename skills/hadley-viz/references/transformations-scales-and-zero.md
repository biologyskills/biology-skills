---
id: hadley-viz.transformations-scales-and-zero
title: Transformations, scales and zero values
domain: hadley-viz
status: draft
---

# Transformations, scales and zero values

## Summary

Axis transformations must respect data semantics. Logarithmic (and other) scales cannot accommodate zero or negative values: such points must be handled (e.g. offset or omitted with note). Indicate transforms clearly in axis labels (e.g. “log10(x)”). Zero values on log scales give misleading gaps; instead, either transform data (with pseudocount) or use a broken axis, explaining the gap. Uniform linear scales should start at zero for count/proportion data to avoid exaggerating differences, unless space demands (then clearly indicate break).

## Core rules

- **Zero handling:** On log scales, remove or specially mark zero measurements (e.g. “below detection”). Don’t plot zero as log(infinite).  
- **Broken axes:** If omitting zero (for visual focus), use a visible break or annotation. Always note it in the caption.  
- **Consistent baselines:** Bar charts and area charts should start at zero to avoid misinterpretation of area.  
- **Axis labels:** When transforming, include the transformation in the label (e.g. “Concentration (log10 ng/ml)”).  
- **Proportions/ratios:** If data are fractions, an appropriate scale (e.g. 0–1) or logit transform may be needed, with explanation.

## Required context

- Minimum data value and whether zeros are true values or censored (detection limit).  
- Reason for any transformation applied (e.g. normality, visualization).  
- If using log scale, the base of the log.

## AI behaviour

- **Detect invalid log:** If data contain zeros, flag before choosing log scale. Suggest alternative (like log(x+1) or no log).  
- **Axis conversion:** Automatically include “log” in axis labels when transform is applied.  
- **Check continuity:** If data nominally include zero, prefer linear scale or clearly mark the omission.

## Common failure modes

- **Log on zero:** Plot with `scale_y_log10()` without noting that some bars at zero actually had measurable value = 0 (misleads viewer).  
- **Unmarked break:** Cutting the y-axis to ignore outlier (starting axis at >0) without indicating it, inflating apparent differences.  
- **Mixed units:** Using linear for some plots and log for others in same figure without explanation.

## Authoritative standards

- **ggplot2 usage:** The grammar allows axis transforms, but documentation emphasizes user must handle zeros.  
- **Data visualization norms:** Bars/areas must start at 0 for integrity.

## Examples

### Example: Cell count bar chart
- **Data:** Counts per million. One category has 0 cells.  
- **Check:** If log scale is needed for others, represent zero as missing or small number and note it.  
- **Good outcome:** Y-axis label “log10(Cell count + 1)” with caption “Zero values shown as 0 on plot (log scale)”.

### Example: Fold-change scatter
- **Data:** Gene expression fold-change (can be <1).  
- **Check:** Use log2 fold-change to symmetrize up/down regulation. Label as “log2(fold-change)”.  
- **Good outcome:** The axis is centered at 0 for no change, with explicit unit labeling.

## Sources

- R4DS/ggplot2 guide (implied: user ensures data are within domain for chosen scale).
