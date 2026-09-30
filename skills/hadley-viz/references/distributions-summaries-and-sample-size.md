---
id: hadley-viz.distributions-summaries-and-sample-size
title: Distributions, summaries and sample size
domain: hadley-viz
status: draft
---

# Distributions, summaries and sample size

## Summary

Visualising distributions requires choosing methods suited to data scale and sample size. For small n, **plot raw observations** (e.g. jittered dots or stripcharts). For larger n, summarise with histograms, density plots, or boxplots. Explore multiple binwidths in histograms to reveal different patterns. Show variability: include individual points or error bars (with clear notation). Avoid plotting mean±SE when n is tiny, as it hides distribution. When data are skewed, consider log-transform or nonparametric summaries.

## Core rules

- **Show raw data if small:** If n<20, prefer dot plots (with jitter) or strip charts. Avoid smooth curves (density) unless annotated that n is small.  
- **Histogram binning:** Try several bin widths; a too-large bin can hide structure. Label axes (count/frequency) clearly.  
- **Bar vs histogram:** Do not use bar charts for continuous data or distribution summary (except binned frequency as histogram).  
- **Summary plots:** Boxplots/violin plots should be supplemented by raw data points if groups are small. Label what ‘whiskers’ represent.  
- **Scale awareness:** If using log scales, note that this compresses skewness.  
- **Sample size annotation:** Report the number of observations or replicates on the figure (e.g. “n = 8” in subtitle or caption).

## Required context

- Actual sample size in each group or category.  
- Nature of distribution (normality, skewness) if known.  
- Whether values represent counts, proportions, or continuous measurements.

## AI behaviour

- **Check n:** Before choosing a plot, examine sample size. If n is low, prioritize raw-data plots.  
- **Bin selection:** If using histograms, suggest at least two binning schemes.  
- **Label statistics:** When summarising, annotate precisely (e.g. “median ± IQR with all data overlaid”).  
- **Compare appropriately:** Do not overlay or compare distributions with vastly different n without adjusting scales or normalization.

## Common failure modes

- **Too few data:** Using a violin plot on n=3 yields a misleading continuous shape.  
- **Large bars instead of density:** Making a bar chart to show a single continuous variable’s spread.  
- **Hidden sample size:** Showing means with error bars but omitting “n=”.  
- **Assuming normality:** Using symmetric error bars on clearly skewed data without mention.

## Authoritative standards

- **R4DS guidance:** “Always explore a variety of binwidths when working with histograms”.  
- **Statistical best practices:** Align with recommendations to plot raw data points where possible (e.g. Weissgerber *et al.* on transparent reporting).

## Examples

### Example: Histogram binning
- **Data:** Enzyme activity levels (n=100).  
- **Check:** Create histograms with different binwidths (e.g. 5 vs 20). Label y-axis “Frequency” and describe in caption if needed.  
- **Good outcome:** Two side-by-side histograms showing fine vs coarse bins, illustrating stable unimodal shape.

### Example: Small group dot plot
- **Data:** Survival fractions for 5 mice per group.  
- **Check:** Use a dot-stripchart or beeswarm, not just group means. Add jitter to distinguish points.  
- **Good outcome:** A plot showing individual values for each mouse; group median lines optional, but raw points visible.

## Sources

- R4DS: recommendation to explore multiple binwidths in histograms.  
- Data visualization best practices (Cleveland/McGill).
