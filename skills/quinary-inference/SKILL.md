---
name: quinary-inference
description: Apply quinary inference rules to assess how strongly biological evidence supports a complete causal explanation. Use when moving beyond observed or interpreted findings to reason about genotype-phenotype hypotheses, posterior support, competing explanations, unresolved measurement, missing causal possibilities, evidence availability, or the distinction between causal truth, inference, and reported decisions.
---

# Quinary inference

Use this skill when the question is not merely what was observed or what a candidate finding means, but **how strongly the available evidence supports the overall causal explanation**.

Quinary inference operates above individual variant calling and interpretation. Its unit of inference is a sufficiently specified explanatory hypothesis, which may involve one variant, a genotype, phased alleles, a structural event, mosaicism, a multilocus configuration, or another complete causal account.

## The fifth layer

| **Layer** | **Core question** | **Main output** |
| --- | --- | --- |
| Primary | How do we measure DNA? | Sequence reads |
| Secondary | What genomic events are present? | Called variants |
| Tertiary | What do those variants mean? | Interpreted candidate findings |
| Quaternary | What should be done with that understanding? | Reports, decisions, and care actions |
| Quinary inference | How strong is the overall explanation? | Posterior support for the full causal account |

These layers are conceptually distinct rather than necessarily executed in a strict temporal sequence. Quinary inference can inform whether a downstream report or action is justified.

## Core rules

- Infer over the **causal explanation**, not merely the most interesting observed variant.
- Do not equate variant pathogenicity, prioritisation rank, classification, or model score with the probability that the finding explains the case.
- Distinguish causal truth, evidence about that truth, posterior belief, and the final reported decision.
- Keep prior plausibility, likelihood of the observed evidence, and posterior support separate.
- Model what could have been missed. An unobserved causal event can remain plausible because of insufficient coverage, assay limitations, mapping failure, incomplete phase, missing relatives, or other unresolved evidence.
- Distinguish **resolved negative evidence** from **unresolved evidence**. “Confidently absent” is not the same as “not determined”.
- Distinguish absence of supporting evidence from evidence against a hypothesis.
- Define the phenotype or outcome being explained and the causal scope of each hypothesis.
- Consider competing and residual explanations rather than assigning all support to the best enumerated candidate.
- When posterior probabilities are normalised across alternatives, ensure the hypotheses are mutually exclusive and collectively appropriate for that calculation. If causes can coexist, model complete causal configurations or use a model that permits coexistence.
- Make inference conditional on a versioned reference model containing the assumptions needed to define the problem, such as inheritance, phase requirements, assay scope, reference resources, evidence sources, thresholds, software, and database versions.
- Treat posterior support as conditional on the available evidence and model. It is not biological ground truth.

## AI behaviour

Before claiming that a genomic finding explains a phenotype:

1. Define the phenotype or biological outcome being explained.
2. State the explanatory hypothesis precisely.
3. Determine whether the required genetic state has actually been resolved.
4. Identify evidence that is missing, unavailable, technically inaccessible, or otherwise unresolved.
5. Consider credible competing explanations, including explanations outside the currently observed candidate set.
6. Distinguish prior plausibility from evidence likelihood and posterior support.
7. Check whether the hypothesis space is appropriate for any probability normalisation.
8. Preserve the reference model and assumptions under which the inference was made.
9. Report uncertainty in the explanation separately from any downstream classification, report, or clinical action.

Do not manufacture certainty by restricting inference to what happened to be observed.

## Example

Suppose a recessive disorder requires two pathogenic alleles in trans.

Sequencing identifies one well-supported pathogenic variant. No second variant is called.

Tertiary interpretation can correctly conclude that the observed variant is pathogenic.

Quinary inference asks a different question:

> How strongly does the available evidence support this genotype as the complete explanation for the patient's phenotype?

If the second allele was adequately interrogated and confidently absent, that is resolved negative evidence. If the relevant region had poor coverage, structural variation was not adequately assessed, phase is unknown, or parental evidence is missing, the causal state remains partly unresolved.

The absence of a second called variant must therefore not automatically become evidence that no second causal event exists.

Likewise, the observed pathogenic variant must not automatically receive complete causal attribution merely because it is the strongest observed candidate.

## Output

The characteristic output of quinary inference is **quantified support for a specified causal explanation**, together with the uncertainty and assumptions required to interpret that support.

A useful posterior quantity can be written conceptually as:

`P(explanatory hypothesis | evidence, phenotype context, reference model)`

This quantity should remain distinct from:

`what is biologically true`

and from:

`what is ultimately reported or done`.

The purpose of quinary inference is to make uncertainty in the **full explanation** explicit rather than leaving it hidden inside expert judgement.


## References

- [`references/explanatory-hypotheses-and-posterior-support.md`](references/explanatory-hypotheses-and-posterior-support.md) for causal hypothesis definition, measurement resolution, observed and unobserved explanations, competing hypothesis spaces, and interpretation of posterior support
