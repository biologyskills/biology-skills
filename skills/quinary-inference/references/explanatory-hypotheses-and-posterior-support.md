---
id: quinary-inference.explanatory-hypotheses-and-posterior-support
title: Explanatory hypotheses and posterior support
domain: quinary-inference
status: draft
---

# Explanatory hypotheses and posterior support

## Summary

Quinary inference asks how strongly the available evidence supports a specified causal explanation.

Its inferential target is not simply whether a variant is present, pathogenic, highly ranked, or reportable. The target is an **explanatory hypothesis**: a proposition about how a genetic event or configuration explains a defined phenotype or biological outcome.

A complete assessment must consider not only observed candidate findings, but also competing explanations, unresolved measurements, and plausible causal events that may not have been observed.

Posterior support therefore describes belief in an explanatory hypothesis **conditional on the available evidence and a defined reference model**. It is not biological ground truth and is not automatically equivalent to a report, diagnosis, or clinical action.

## Core rules

- Define the phenotype or biological outcome being explained before evaluating an explanation.
- State the explanatory hypothesis precisely enough that its causal scope is clear.
- Use the explanatory hypothesis or complete causal configuration as the unit of inference, not necessarily a single variant.
- Distinguish variant presence, variant pathogenicity, functional effect, phenotype relevance, and explanatory causality.
- Do not convert a pathogenicity classification, prioritisation rank, prediction score, or expert judgement directly into a posterior probability of explanation.
- Distinguish causal truth, evidence about causal truth, posterior belief, interpretation, and the final reported decision.
- Distinguish prior plausibility, likelihood of the observed evidence, and posterior support.
- Model relevant unobserved possibilities when technical or biological limitations leave them unresolved.
- Distinguish resolved negative evidence from unresolved evidence.
- Distinguish absence of supporting evidence from evidence against a hypothesis.
- Include credible competing or residual explanations rather than forcing all probability onto the best observed candidate.
- Do not normalise overlapping hypotheses as though they were mutually exclusive.
- Preserve the versioned assumptions and reference resources that define the inference.
- Do not report numerical posterior support unless a defensible probabilistic model actually produces it.
- Treat posterior support as conditional on the model and evidence. Numerical precision does not establish biological certainty.

## The inferential target

Let the phenotype or biological context being explained be `D`.

An explanatory hypothesis `H` should state what is proposed to explain `D` and at what causal scope.

Examples include:

```text
A heterozygous dominant allele explains the phenotype.
````

```text
Two pathogenic alleles in trans form the recessive genotype
explaining the phenotype.
```

```text
A copy-number loss affecting this gene explains the phenotype.
```

```text
This genetic event contributes to, but does not completely explain,
a multifactorial phenotype.
```

These are different hypotheses.

The phrase **explains the phenotype** must therefore not be used without specifying whether the hypothesis represents a complete explanation, a necessary component, a contributing cause, or another defined causal role.

The unit of inference can be:

* a single allele
* a homozygous genotype
* a compound-heterozygous pair
* a phased haplotype
* a copy-number or structural event
* a repeat expansion
* mosaicism
* a multilocus configuration
* another explicitly specified causal state

## Truth, evidence, belief, and decision

Keep these quantities separate:

```text
underlying causal truth
        ≠
available evidence
        ≠
posterior belief
        ≠
reported conclusion
        ≠
clinical action
```

A database classification or expert consensus is evidence about biological reality. It does not define that reality.

Likewise, a posterior such as:

```text
P(H | evidence, phenotype, reference model) = 0.82
```

means that the specified model assigns 0.82 posterior support to `H` under those conditions.

It does not mean:

```text
H is 82% true in an observer-independent sense
```

nor does it by itself specify what clinical action should follow.

## Prior, likelihood, and posterior

Three quantities answer different questions.

### Prior plausibility

```text
P(H | phenotype context, reference model)
```

How plausible was this explanation before considering the current case evidence?

Relevant information can include population frequency, inheritance, gene-disease knowledge, penetrance, biological mechanism, or other justified prior information.

### Likelihood

```text
P(evidence | H, phenotype context, reference model)
```

How compatible is the observed evidence with what would be expected if this hypothesis were the explanation?

The likelihood can depend on measurement properties such as coverage, sensitivity, specificity, genotype quality, phase, and assay scope.

### Posterior support

```text
P(H | evidence, phenotype context, reference model)
```

How strongly is the explanatory hypothesis supported after the evidence is considered?

Do not use these quantities interchangeably.

A rare event is not automatically causal. A damaging prediction is not an occurrence probability. A high prior is not a posterior. A high posterior is not ground truth.

## Measurement and resolution

Inference depends on what the assay was capable of resolving.

Consider a candidate site at which no alternate allele was called.

### Resolved negative

```text
adequate measurement
+
confident reference genotype
```

supports the conclusion that the candidate allele was not detected under an adequately resolved measurement.

### Unresolved

```text
insufficient coverage
```

or:

```text
assay unable to detect the relevant event class
```

or:

```text
phase not established
```

does not support the same conclusion.

Therefore:

```text
confidently absent
≠
not observed
≠
not measured adequately
```

An unresolved causal possibility must not silently become negative evidence.

## Observed and unobserved explanations

Quinary inference should not restrict causal reasoning to variants appearing in the final called-variant list.

A biologically plausible explanation can remain unobserved because of:

* insufficient coverage
* mapping failure
* genotype uncertainty
* incomplete phase
* assay blind spots
* unsupported structural-variant classes
* repeat expansions outside assay capability
* mosaicism below detection limits
* missing parental or segregation data
* incomplete annotation or reference knowledge

The relevance of these possibilities depends on the hypothesis and assay.

Do not invent arbitrary unseen variants. Consider unobserved explanations only when they belong to a justified candidate universe and remain plausible under the measurement process and reference model.

## Competing and residual hypotheses

A strong observed candidate does not eliminate alternatives.

For mutually exclusive model selection, the hypothesis space may conceptually contain:

```text
H1        candidate explanation 1
H2        candidate explanation 2
...
Hother    explanation outside the enumerated candidate set
Hnone     no explanation within the defined causal domain
```

Residual hypotheses prevent an enumerated candidate from receiving all posterior support merely because the model failed to represent another possibility.

If two explanations can coexist, they are not mutually exclusive alternatives.

For example:

```text
H1 = variant A contributes to disease
H2 = variant B contributes to disease
```

may both be true.

Do not place such overlapping hypotheses into a simple mutually exclusive normalisation. Instead define complete causal configurations or use a model that permits multiple simultaneous causes.

## Reference model

Every quinary inference is conditional on a reference model.

Preserve as applicable:

* phenotype definition
* causal scope
* transcript or genomic reference
* admissible event classes
* inheritance assumptions
* penetrance assumptions
* phase requirements
* population model
* assay scope and limitations
* evidence sources
* interpretation rules
* decision thresholds
* software and version
* database snapshots
* relevant standard operating procedures

Changing the reference model can change the posterior without changing the underlying biology.

Results from materially different reference-model versions should therefore not be treated as directly equivalent without reconciliation.

## AI behaviour

Before assigning support to a causal explanation:

1. Define the phenotype or biological outcome.
2. State the explanatory hypothesis and its causal scope.
3. Identify the genetic state that would have to be established for that hypothesis.
4. Determine which required evidence is resolved and which remains unresolved.
5. Distinguish resolved negative observations from missing or inadequate measurements.
6. Identify credible competing and residual explanations.
7. Establish whether competing hypotheses are mutually exclusive or can coexist.
8. Keep priors, likelihoods, scores, classifications, and posterior probabilities semantically separate.
9. Check that evidence sources are being used according to what they actually measure.
10. Preserve the reference model and its version.
11. Report posterior support only if a defined probabilistic model supports that quantity.
12. State the important unresolved evidence and, where possible, which additional observation would materially reduce uncertainty.

If the available information does not support quantitative inference, say so. Do not manufacture a probability from qualitative evidence.

## Common failure modes

### Pathogenicity treated as diagnostic certainty

```text
Variant A is pathogenic.
Therefore Variant A explains the patient's disease with near certainty.
```

This is invalid.

Pathogenicity concerns properties of the variant in an appropriate biological context. Explanatory attribution additionally depends on genotype, inheritance, phenotype, measurement, competing causes, penetrance, and other case-specific evidence.

### Best observed candidate absorbs all support

Only one plausible pathogenic variant appears in the VCF, so the system assigns it complete causal attribution.

This ignores causal events that the assay failed to resolve or that were outside the enumerated candidate space.

The best **observed** explanation is not necessarily the best **overall** explanation.

### Missing treated as absent

A pathogenic site has inadequate coverage and no alternate allele is called.

The system records:

```text
variant absent
```

The correct state is unresolved unless adequate evidence establishes absence.

### One pathogenic allele treated as a complete recessive diagnosis

A patient with a recessive disorder has one clearly pathogenic allele.

The allele may be genuinely pathogenic while the complete recessive explanation remains unresolved if the second required allele or phase is not established.

### Rank treated as probability

A prioritisation system ranks a variant first among 2,000 candidates.

This does not imply:

```text
P(causal) = 1 / rank
```

or any other posterior probability unless the ranking model has been explicitly calibrated to that quantity.

### Overlapping causes normalised as alternatives

Two contributing genetic effects can coexist, but the system forces them to compete for probability mass summing to one.

The hypothesis space is incorrectly specified.

### Posterior treated as truth

A model reports:

```text
P(H | X) = 0.95
```

and the result is rewritten as:

```text
H is proven true.
```

Posterior support remains conditional on the evidence, model, assumptions, and candidate space.

## Examples

### Observed pathogenic variant with an unresolved alternative

A dominant disease has one well-supported pathogenic variant detected in the patient.

A second known plausible causal site was not adequately sequenced.

Tertiary interpretation may correctly classify the observed variant as pathogenic.

Quinary inference must additionally preserve:

```text
observed explanation: supported
alternative explanation: unresolved
overall attribution: uncertain between them
```

If follow-up testing confidently establishes that the alternative event is absent, support can shift towards the observed explanation.

The new evidence changes belief about the explanation. It does not retroactively change the biological properties of the first variant.

### Recessive disease with unresolved phase

Two pathogenic variants are observed in the same recessive disease gene.

If the hypothesis requires the variants to be in trans but phase is unknown:

```text
variant interpretation: supportive
genetic configuration: unresolved
complete causal explanation: not yet established
```

Do not turn two pathogenic labels into a complete recessive diagnosis without resolving the required genotype configuration.

### Negative evidence versus unresolved evidence

For a candidate causal variant:

```text
Case A:
high-quality sequence establishes reference genotype
→ resolved negative evidence
```

```text
Case B:
region has inadequate coverage
→ unresolved evidence
```

Both cases lack an observed alternate allele.

They should not contribute identically to the inference.

## Expected output

A quinary inference result should make clear:

* the explanatory hypothesis
* the phenotype or outcome being explained
* posterior support, when quantitatively justified
* uncertainty in that support where applicable
* which required evidence was resolved
* which important evidence remains unresolved
* important competing or residual explanations
* the reference-model version and material assumptions
* the relationship between the inference and any downstream report or decision

The aim is not merely to nominate the strongest candidate.

The aim is to quantify, or explicitly delimit, **how defensible the complete causal explanation is given what is known, what is unresolved, and what alternatives remain possible**.

## Authoritative standards

Quinary inference is an inferential framework, not a replacement for maintained standards governing its input evidence.

Use the appropriate current authorities for exact variant nomenclature, genomic references, assay interpretation, variant classification, gene-disease validity, phenotype terminology, and other component evidence.

Do not reinterpret a classification framework, prediction score, database assertion, or clinical guideline as though it directly supplied posterior support for a complete causal explanation unless it was explicitly designed and validated to do so.

The exact method used to construct priors, likelihoods, hypothesis spaces, resolution thresholds, or posterior estimates is implementation-specific and should be documented and validated separately.

## Sources

* Lawless D. *Quinary inference, the fifth layer of genomics.* 2026.
* Lawless D. *A twelve-state notation for genotype-phenotype interpretation: Canonical semantics for evidence, inference, reporting, and audit.* Version 1.0, 2026.
* Lawless D. *Hardy-Weinberg a century later and new horizons in clinical genomics.* 2026.
* Quant Group et al. *Quantification of diagnostic probability in genomic interpretation.* 2026.


