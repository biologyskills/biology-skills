---
id: hadley-viz.longitudinal-paired-and-repeated-measures
title: Longitudinal, paired and repeated measures
domain: hadley-viz
status: draft
---

# Longitudinal, paired and repeated measures

## Summary

Data collected over time or repeated under different conditions on the same subjects require special plotting. **Time-course plots** should preserve time order and mark missing time points. For paired data (same subject before/after), use connected line segments for each subject or plot the difference. Facetting by subject can reveal consistent patterns. Do not treat repeated measures as independent replicate counts: annotate them as repeated (e.g. with subject ID as color or facet).

## Core rules

- **Time plots:** Plot time on the x-axis and connect points chronologically. If data are irregularly spaced, mark axis carefully.  
- **Paired connectivity:** Use lines to connect measurements from the same subject across categories (e.g. pre/post) to show within-subject changes.  
- **Faceting:** For clarity with few subjects, create small multiples per subject. Large numbers of subjects may require summarizing with mean±error over time.  
- **Variance captioning:** When showing time-series, indicate if lines are individuals or means.

## Required context

- Subject or unit identifier for repeats.  
- Measurement times or condition labels (ordered categories).  
- Number of repeated measures per subject and intervals.

## AI behaviour

- **Check structure:** If `aes(group=subject)` is applicable, ensure lines are drawn or facets used.  
- **Identify trends:** If asked about time trends, verify that plotting style allows slope interpretation (e.g. use the same y-axis for all subjects).  
- **Handle missing repeats:** If some subjects miss time points, do not drop them without note; show gap or annotate “no measurement”.

## Common failure modes

- **Disconnected points:** Treating pre/post points as separate groups (e.g. two unlinked boxplots).  
- **Spaghetti plot overload:** Plotting hundreds of individual lines in one panel (becomes unreadable).  
- **Chronology lost:** Shuffling time points (plotting by category) incorrectly shows broken trend.

## Authoritative standards

- **Time-series visualization:** Standard practice is lines connecting repeated measures per subject (Long & Alcock guidelines).  

## Examples

### Example: Treatment over time
- **Data:** Blood sugar in patients at weeks 0, 4, 8.  
- **Check:** Plot each patient’s trajectory as a line. Add a bold line for population mean.  
- **Good outcome:** Thin lines (n=10) plus thick mean line, x-axis labeled weeks.

### Example: Pre/post intervention
- **Data:** Enzyme levels before/after in individuals.  
- **Check:** Scatter plot with arrows or lines linking each subject’s before and after points, or plot paired differences.  
- **Good outcome:** Each patient shown with different color; caption “lines connect paired measurements (n=8 patients)”.
