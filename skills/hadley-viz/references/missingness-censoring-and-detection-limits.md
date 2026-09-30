---
id: hadley-viz.missingness-censoring-and-detection-limits
title: Missingness, censoring and detection limits
domain: hadley-viz
status: draft
---

# Missingness, censoring and detection limits

## Summary

Data below detection limit or missing values must be displayed appropriately. Do not treat “no measurement” as zero. If points are censored (e.g. “<LOD”), indicate with special symbols or limit line. Missing values should not create gaps without note: either impute (with caveats) or annotate “no data”. When plotting summary statistics, ensure missing data are handled (e.g. exclude NA explicitly, document approach). For time series or longitudinal plots, show gaps or dashed lines where data are absent.

## Core rules

- **Detection limits:** Represent censored values with open symbols or arrows. Mention detection limit threshold on the axis or caption.  
- **Missing data:** Do not connect lines across a missing point. If unavoidable, break the line and mark it.  
- **Non-detects:** If plotting log-transformed data, non-detects cannot be log(0) – handle separately.  
- **Explain imputation:** If imputation is used (mean, half-LOD), note it in caption or legend.

## Required context

- Information on how missingness was handled in data collection/analysis (MCAR, MAR, LOD, etc.).  
- Threshold values for detection limits.

## AI behaviour

- **Flag zeros:** If a zero is biologically impossible (e.g. cannot have negative concentration), check if it indicates <LOD.  
- **Plot markers:** Use different marker or color to flag missing/censored points.  
- **Describe in caption:** When data are missing or censored, explicitly state it (e.g. “* indicates below detection limit”).

## Common failure modes

- **Zero misrepresentation:** Plotting non-detected as zero value (implies existence at zero).  
- **Hidden missingness:** Line plot fills missing values without break, suggesting continuous measurement.  
- **Misleading axis:** Using linear scale on log-norm data with missing, causing misalignment.

## Authoritative standards

- **Data reporting guidelines:** Follow analytical chemistry conventions for censoring (e.g. “half-LOD imputation” disclosure).  

## Examples

### Example: ELISA concentration
- **Data:** Cytokine levels in pg/mL, some below assay LOD (0.5 pg/mL).  
- **Check:** Plot undetectable values as “<LOD” labels or open circles at LOD line.  
- **Good outcome:** Y-axis starts at 0, an arrow or open symbol at y=0.5 with caption “open circles = below LOD”.

### Example: Line chart with missing day
- **Data:** Weekly measurement for 6 weeks, missing week 3.  
- **Check:** Omit the line segment for week 3; place gap or dashed line.  
- **Good outcome:** Dashed line between week 2 and 4 with break at 3, label “No data in week 3”.
