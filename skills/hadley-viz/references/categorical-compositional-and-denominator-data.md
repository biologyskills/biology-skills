---
id: hadley-viz.categorical-compositional-and-denominator-data
title: Categorical, compositional and denominator data
domain: hadley-viz
status: draft
---

# Categorical, compositional and denominator data

## Summary

Plots of categorical or compositional data (pie charts, stacked bars, etc.) must reflect the underlying totals. When comparing composition, use the same denominator or show relative frequencies. For instance, if group sizes differ, a **100% stacked bar** (`position="fill"`) highlights proportions, whereas a raw stacked bar might hide that. Also be wary of pie charts for small category counts (they can obscure small differences). Always indicate the base: either plot raw counts side-by-side or proportions with appropriate labeling.

## Core rules

- **Common denominator:** When comparing categories across groups, ensure each bar is scaled comparably (use equal total height for relative frequency plots).  
- **Denominator labeling:** If plotting counts, label axes “count”; if proportions, label “percentage” or “proportion”. Correct the default y-label accordingly.  
- **Pie charts:** Rarely recommended; if used, include data labels or a caption to compare proportions precisely.  
- **Directional data:** For compositional (e.g. genome regions percentages), consider a bar or stacked bar rather than misleading 3D or radial charts.

## Required context

- Total counts or sums for each group/category.  
- Whether categories are parts of a whole (compositional) or independent variables.  
- If data represent a ratio (e.g. prevalence per population), include the base population.

## AI behaviour

- **Choose plot type:** For two categorical variables, prefer side-by-side or faceted bars over 100%-stacked unless proportions are the focus.  
- **Check labels:** Do not let ggplot’s default “count” label stand when plotting percentages; override with `labs(y="Proportion")`.  
- **Normalize explicitly:** If proportions are needed, perform the normalization step rather than expecting the agent to infer it from position="fill".

## Common failure modes

- **Unequal denominators:** Stacked bars of different group sizes appear different in area but convey raw counts rather than proportion.  
- **Missing context:** Showing a pie chart of species composition in one sample without indicating the sample size or context.  
- **Bar mislabel:** Leaving y-axis as “count” on a relative bar plot, confusing interpretation.

## Authoritative standards

- **ggplot2 stacked bars:** Use `position="fill"` for relative frequencies, as illustrated in R4DS.  

## Examples

### Example: Population frequency by continent
- **Data:** Cases in continents, sample sizes differ.  
- **Check:** Plot relative frequencies per continent (100% stacked bars) with y-axis “Percentage”.  
- **Good outcome:** Two panels: one showing absolute counts (y="count") and one showing normalized (y="proportion"), labeled as such.

### Example: HLA allele composition
- **Data:** Allele counts for samples from different populations.  
- **Check:** Use clustered bar chart or separate plots for each population. If plotting all in one, stack by population with legend. Include sample sizes in caption.
