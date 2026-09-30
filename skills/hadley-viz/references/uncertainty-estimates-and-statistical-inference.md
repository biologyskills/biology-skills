---
id: hadley-viz.uncertainty-estimates-and-statistical-inference
title: Uncertainty estimates and statistical inference
domain: hadley-viz
status: draft
---

# Uncertainty estimates and statistical inference

## Summary

Error bars, confidence intervals, and other uncertainty depictions must be chosen to match the analysis. The plot’s annotations should state what the uncertainty represents (SD, SEM, 95% CI, credible interval, etc.). If n is small (<10), prefer showing raw data or IQR over misleading “standard error” bars. Avoid implying statistical significance: e.g., overlapping error bars do not always mean non-significance. For model-based inference plots (regression lines, ROC curves), annotate uncertainty (shading or error ribbons) only if sample size and model assumptions are appropriate.

## Core rules

- **Annotation:** Label error bars/intervals clearly (e.g. “mean ± SD” or “95% CI”) in caption or legend.  
- **Match data:** Use SD bars for sample variability, SE/CI when making inference. Don’t use SE bars for describing distribution with small n.  
- **Sample size:** With small n, emphasize raw data or use bootstrapped CI.  
- **Statistical lines:** When adding fitted lines (e.g. trend lines), also add a shaded CI or bootstrap band if claiming predictive power.  
- **Avoid inferential claims:** In plots, do not use “*” to denote significance unless a statistical test was done and described. Instead, describe differences in text or use annotated p-values separately.

## Required context

- Clarify if visual is exploratory or inferential.  
- Know the number of replicates and data distribution (to choose parametric vs nonparametric error estimates).  
- If a statistical model is implied, know its assumptions.

## AI behaviour

- **Pick proper bars:** Suggest SD bars for experimental variability or 95% CIs for treatment effects, depending on use-case.  
- **Explain error:** Always include notes on what error bars mean in the caption.  
- **Check interpretation:** Do not allow error bars to be interpreted as significance markers; add clarifying text if needed.

## Common failure modes

- **Ambiguous bars:** Plot with error bars unlabeled; reader cannot tell if they are SD, SE, or CI.  
- **Small-n overconfidence:** Showing SE bars for n=3 gives false precision.  
- **Misleading intervals:** Plotting mean±CI to judge individual data spread (CI narrows as n grows, not a measure of variability).

## Authoritative standards

- **Statistical visualization:** Recommend labeling and transparency (American Statistician guidelines on effect sizes and CIs).  

## Examples

### Example: Group mean comparison
- **Data:** Two group means, n=5 each.  
- **Check:** Prefer show individual points or boxplot + points instead of only mean±SE. If bars used, caption “mean ± SD (n=5)”.  
- **Good outcome:** Plot shows points and error bars labeled “SD” in legend.

### Example: Regression line
- **Data:** Scatter of x vs y (n=100).  
- **Check:** Fit linear regression with shaded 95% confidence band. Label line “best-fit ± 95% CI”.  
- **Good outcome:** Plot includes dashed line for fit and shaded region for confidence (caption notes CI).
