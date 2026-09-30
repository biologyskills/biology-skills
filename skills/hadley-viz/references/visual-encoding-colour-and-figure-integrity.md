---
id: hadley-viz.visual-encoding-colour-and-figure-integrity
title: Visual encoding, colour, and figure integrity
domain: hadley-viz
status: draft
---

# Visual encoding, colour, and figure integrity

## Summary

Colour and other visual encodings carry information. They must be chosen to reveal true signal, not distract. Always ensure sufficient contrast: colorblind-safe palettes (e.g. blue–orange). Never rely on colour alone to distinguish categories; add redundant markers (shape, line type). Keep fonts legible. Avoid chartjunk: gridlines and 3D effects that don’t encode data distort perception. Preserve data-ink ratio by minimizing unnecessary background. Each plot must stand alone: include annotations (e.g. “*” for significance only if explained; no decorative doodles).

## Core rules

- **Colour choice:** Use palettes where every category can be differentiated in grayscale. For sequential data, use a single-hue gradient; for diverging data, use two contrasting hues with a white midpoint.  
- **Contrast:** Ensure text and lines meet WCAG contrast ratios (≥4.5:1).  
- **Redundant encoding:** Encode categorical differences with shape or dashing in addition to colour.  
- **Minimal ornamentation:** Do not add 3D bars, “exploding” pie slices, or heavy shadows. Use simple lines, bars, etc.  
- **Direct labeling:** Label lines or bars directly when possible instead of a separate legend.

## Required context

- Audience’s needs (e.g. color-deficiency prevalence).  
- Whether figures will be printed (grayscale test) or displayed digitally.

## AI behaviour

- **Palette check:** If too many categories for distinct colors, raise a warning (or group categories).  
- **Convert to grayscale:** Validate that the plot conveys information when desaturated.  
- **Clutter removal:** Remove non-informative elements (excess ticks, backgrounds) to highlight data.  
- **Legible text:** Check point sizes and font sizes are readable at final figure resolution.

## Common failure modes

- **Low contrast:** Light grey text on white background or red/green on white without sufficient contrast.  
- **Overreliance on colour:** Color differences without shapes (red vs green lines) excludes ~10% viewers.  
- **Chartjunk:** 3D bar charts or unnecessary pictograms that do not map to data quantities.

## Authoritative standards

- **Accessible design:** Follow WCAG guidelines for charts (contrast, redundancy).  
- **Perception studies:** Cleveland & McGill’s hierarchy (position > length > angle > area > colour) suggests using position/length encodings over area or color for quantitative comparisons.

## Examples

### Example: Multi-category scatter
- **Data:** Expression by cell type (6 categories).  
- **Check:** Use a colorblind-friendly palette (e.g. `scale_color_viridis_d()` or blue/orange pair). Use different shapes for lineages as well.  
- **Good outcome:** Legend shows color and shape mapping, and the chart remains interpretable in grayscale.

### Example: Time-series lines
- **Data:** Trends for 3 conditions.  
- **Check:** Two conditions with similar color must differ in line type. Add data labels for key points if close.  
- **Good outcome:** One line solid blue, one dashed green, one dotted red; each labelled in-plot or via clear legend.
