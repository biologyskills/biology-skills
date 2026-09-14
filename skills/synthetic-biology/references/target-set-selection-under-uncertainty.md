---
id: synthetic-biology.target-set-selection-under-uncertainty
title: Target-set selection under uncertainty
domain: synthetic-biology
status: draft
---

# Target-set selection under uncertainty

## Summary

A multi-target therapeutic construct has finite capacity.

Selecting targets is therefore not necessarily equivalent to independently scoring candidates and taking the first `N` rows.

The candidate universe is produced by imperfect assays, variant calling, transcript reconstruction, HLA typing, peptide generation, model prediction, and filtering. Candidates can also be dependent or redundant because they arise from the same mutation, tumour clone, HLA molecule, source sequence, or biological mechanism.

A defensible design preserves:

```text
candidate universe
+
evidence and uncertainty
+
score semantics
+
dependencies
+
selection objective
+
constraints
+
selected set
```

rather than retaining only the final rank.

## Core rules

- Preserve the candidate universe from which selection occurred.
- Treat candidate-generation rules as part of the design specification when they determine which targets can ever be selected.
- Distinguish a candidate that was evaluated and rejected from one that was never generated, inadequately measured, filtered upstream, unscored, or otherwise unresolved.
- Missing evidence is not automatically negative evidence.
- A failed hard threshold does not establish that the underlying biological property is absent.
- Preserve the semantics of every quantity entering selection.
- Do not interpret a model score, weighted sum, rank, percentile, or heuristic utility as a probability unless it has been calibrated and validated as that probability.
- If a probability is reported, define the event whose probability is being estimated.
- Preserve uncertainty when evidence strength depends on finite read depth, assay sensitivity, inferred phase, tumour purity, model uncertainty, or another unresolved quantity.
- Do not discard denominators when they materially affect evidential strength.
- Distinguish tumour mutation burden or total candidate count from target quality.
- Treat overlapping peptide candidates from the same molecular event as potentially dependent rather than automatically counting them as independent biological opportunities.
- Treat candidates associated with the same HLA molecule, tumour clone, source event, or escape mechanism as potentially correlated when that dependence matters to the design objective.
- Do not assume that the individually highest-ranked `N` candidates form the best multi-target set.
- A set-level objective can consider individual evidence together with redundancy, tumour coverage, clonality, HLA breadth, class I or class II representation, construct compatibility, sequence length, and other declared constraints.
- Do not invent a universal target-set objective. The appropriate objective is product- and hypothesis-specific.
- Preserve the distinction between an individual candidate score and the utility assigned to a complete target set.
- When selected-set membership changes materially under plausible input uncertainty, model version, threshold, or candidate representation, report that instability rather than presenting the set as uniquely determined.
- Preserve the exact model, resource, configuration, criteria, candidate universe, and target-set version used for a design.
- Do not infer proprietary production rules from a published selected set.
- Treat patent embodiments as disclosed possibilities, not proof of a current production algorithm.

## Candidate universe

The final selected set is conditional on what was capable of becoming a candidate.

```text
tumour and normal observations
        ↓
eligible genomic events
        ↓
eligible transcripts / source sequences
        ↓
generated peptide windows
        ↓
eligible HLA contexts
        ↓
scored candidate combinations
        ↓
selection
```

A candidate missing from the final set can therefore mean:

```text
biologically absent
not observed
not callable
source transcript unavailable
excluded by candidate-generation rules
not scored
failed a threshold
redundant under set selection
construct-incompatible
lower utility than another candidate
```

Do not collapse these states into:

```text
bad neoantigen
```

## Required context

Preserve as applicable:

- design or product identifier
- candidate-universe definition
- genomic event classes considered
- transcript-selection rules
- peptide lengths or generation rules
- HLA molecules considered
- source-assay limitations
- upstream inclusion and exclusion criteria
- score name
- score target and units
- model and version
- prediction mode
- calibration method if a probability is claimed
- uncertainty measure where available
- missing-value behaviour
- read counts or other denominators when material
- clonality or tumour-coverage estimate and method
- dependency or redundancy definitions
- product capacity
- maximum sequence length where applicable
- set-level objective
- set-level constraints
- construct-compatibility criteria
- selected-set version
- software and resource versions

## AI behaviour

Before interpreting or constructing a selected target set:

1. determine which candidates were capable of entering the analysis,
2. identify candidates excluded before scoring and why,
3. determine what every score actually represents,
4. distinguish measured evidence from predicted features,
5. preserve unresolved evidence rather than replacing it with zero,
6. retain denominators and uncertainty when point estimates conceal large differences in evidence,
7. identify candidates that share a source event, sequence, tumour clone, HLA restriction, or other important dependency,
8. determine the actual finite-product constraints,
9. state whether selection was independent per candidate or optimised over a set,
10. preserve the objective and constraints used by any set-level optimisation,
11. test or report design instability when small plausible changes alter selected membership,
12. record the exact selected set and design version.

Do not rewrite:

```text
model score = 0.87
```

as:

```text
87% probability of being a useful vaccine target
```

unless that is exactly the event the model was trained, calibrated, and validated to estimate.

Do not reconstruct missing probabilities by rescaling ranks.

Do not assume that an unselected target was biologically negative.

## Common failure modes

### Top N treated as automatically optimal

```text
sort by score
take first N
```

can be a valid declared heuristic.

It is not guaranteed to maximise a set-level objective when candidates differ in redundancy, tumour coverage, HLA restriction, evidence certainty, or construct compatibility.

### Candidate denominator lost

The final report retains:

```text
34 selected targets
```

but loses:

```text
how many source events were callable
how many generated candidate sequences
how many peptide:HLA combinations were evaluated
which classes were excluded
```

The selected set can no longer be interpreted relative to its search space.

For intismeran autogene, public descriptions state that up to 34 neoantigen sequences are encoded into one mRNA. That is a product-specific design capacity, not a universal mRNA-vaccine rule.

### Missing RNA treated as zero expression

A candidate has no usable RNA evidence.

The pipeline assigns:

```text
expression = 0
```

without distinguishing:

```text
measured low or zero
no informative reads
assay failure
insufficient coverage
transcript not quantified
```

An unresolved measurement has been converted into biological evidence against the candidate.

### Equal VAF treated as equal certainty

```text
10 / 20 = 0.50
500 / 1000 = 0.50
```

The point estimate is identical.

The amount of information supporting it is not.

### Rank treated as calibrated probability

Candidate A is ranked first and candidate B second.

That ordering does not identify:

```text
P(A useful)
P(B useful)
```

or the difference between those probabilities.

### Redundant candidates counted as independent coverage

Several highly ranked peptides are overlapping windows around the same mutation and use the same HLA restriction.

Counting each as an independent tumour target can exaggerate the biological diversity of the set.

### Mutation burden treated as target quality

A tumour with many somatic variants can generate a larger candidate search space.

That does not imply that every additional variant has strong expression, presentation, recognition, clonality, or therapeutic value.

### Patent options treated as production rules

A patent describes candidate features, thresholds, or possible selection strategies.

The analysis reports those embodiments as the exact current production algorithm.

The evidence does not justify that conclusion.

## Authoritative standards

There is no universal standard that defines the correct objective function for personalised neoantigen selection.

Use the authoritative documentation for each component model and preserve its semantics rather than inventing a common score interpretation.

For a specific product or programme, keep these evidence categories distinct:

```text
peer-reviewed clinical description
patent disclosure
research implementation
inferred design principle
undisclosed production method
```

## Examples

### Independent rank versus set diversity

Suppose:

```text
A1  source mutation A  HLA-A*02:01  score 0.95
A2  source mutation A  HLA-A*02:01  score 0.94
A3  source mutation A  HLA-A*02:01  score 0.93
B1  source mutation B  HLA-B*07:02  score 0.90
```

Selecting:

```text
A1, A2, A3
```

maximises the three highest individual scores.

Selecting:

```text
A1, A2, B1
```

could have higher utility under a declared objective that values coverage of different source events or presentation routes.

Neither set is universally correct.

The objective must be stated.

### Missing evidence

```text
Candidate A:
RNA evidence = measured and low

Candidate B:
RNA evidence = unavailable because coverage was insufficient
```

These states should not automatically receive the same contribution.

One contains negative or weak evidence under a defined measurement.

The other remains unresolved.

### Selection provenance

```text
design_id: <identifier>
candidate_generator: <software and version>
annotation_release: <release>
hla_prediction_model: <name and version>
selection_model: <name and version>
selection_objective: <identifier or specification>
constraints: <declared constraints>
candidate_universe: <recoverable object>
selected_set: <recoverable object>
design_version: <version>
```

The selected peptide list alone is not complete computational provenance.

## Sources

- Ojalvo LS et al. Intismeran Autogene Therapy: An End-to-End Pathway From Tumor Tissue to Individualized Neoantigen Treatment for Patients With Cancer. JCO Oncology Advances. 2026. https://doi.org/10.1200/OA-25-00206
- ModernaTX, Inc. Personalized cancer vaccine epitope selection. US20210268086A1. https://patents.google.com/patent/US20210268086A1/en
- Wells DK et al. Key Parameters of Tumor Epitope Immunogenicity Revealed Through a Consortium Approach Improve Neoantigen Prediction. Cell. 2020. https://doi.org/10.1016/j.cell.2020.09.015
- McGranahan N et al. Clonal neoantigens elicit T cell immunoreactivity and sensitivity to immune checkpoint blockade. Science. 2016. https://doi.org/10.1126/science.aaf1490
