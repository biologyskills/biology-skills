---
id: biology-core.evidence-and-claims
title: Evidence and claims
domain: biology-core
status: draft
---

# Evidence and claims

## Summary

Biological analysis moves through different levels of evidence and inference. A measurement, statistical association, model prediction, mechanistic hypothesis, and causal conclusion are different objects and should not be collapsed into one another.

## Core rules

- A prediction is not a measurement.
- Statistical association does not by itself establish molecular mechanism or causality.
- Enrichment of signal in a set does not prove the predicted effect of every member of that set.
- A model score must be interpreted according to its defined target, scale, and calibration.
- Experimental validation should measure the quantity relevant to the claim being validated whenever practical.

## Required context

For an evidence-based claim, identify where relevant:

- what was directly measured
- what was predicted or inferred
- the unit and scale
- the comparison being made
- the model or statistical target
- the experimental or observational design
- uncertainty or confidence
- whether the claim is associative, mechanistic, or causal

## AI behaviour

- Name the evidence type before escalating the interpretation.
- Do not describe an association as a mechanism unless mechanistic evidence is available.
- Do not describe a ranking score as a probability unless it is defined and calibrated as one.
- Match validation evidence to the predicted quantity.

## Common failure modes

### Association presented as mechanism

A variant set that improves a burden-test association may contain more biologically relevant variants, but the association alone does not establish how an individual variant changes transcription, splicing, binding, or another molecular process.

### Rank presented as probability

A percentile or PHRED-like rank can describe relative position among scored variants without representing the probability that a variant is pathogenic or functionally active.

## Authoritative standards

Use the statistical, experimental, or clinical framework appropriate to the claim. Where a field has formal evidence criteria, cite that framework rather than translating it into an improvised local scale.

## Examples

### Model output

Prefer: "The model ranks this variant in the top 1% under its defined impact score."

Avoid: "The variant has a 99% probability of being pathogenic" unless that probability is the validated quantity produced by the model.

## Sources

- Hernán MA, Robins JM. *Causal Inference: What If.* https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/
- National Academies. *Reproducibility and Replicability in Science.* https://doi.org/10.17226/25303
