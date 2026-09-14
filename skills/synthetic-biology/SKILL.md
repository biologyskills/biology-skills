---
name: synthetic-biology
description: Apply biological and computational correctness rules when biological observations, predictions, and selected targets are converted into engineered biological sequences or constructs. Use especially for personalised mRNA vaccines, neoantigen selection, peptide-HLA design, finite multi-target selection, polyepitope constructs, and tasks where source identity, host context, prediction semantics, uncertainty, sequence context, or design provenance can change whether an engineered construct represents the intended biology.
---

# Synthetic biology

Use this skill when biological evidence is being converted into an engineered sequence or construct and correctness depends on preserving the path from source biology to the designed product.

Personalised mRNA cancer vaccines are a central example:

```text
patient and tumour
      ↓
measured molecular state
      ↓
candidate targets
      ↓
predicted biological behaviour
      ↓
selected target set
      ↓
engineered construct
```

Each transition creates a new object and additional assumptions.

This skill focuses on computational design semantics and biological validity. It does not provide manufacturing protocols, dosing instructions, or proprietary production recipes.

## Core rules

- Keep the source biological observation, derived candidate, prediction, selected target, amino-acid construct, nucleotide construct, and physical product as distinct objects.
- Preserve end-to-end lineage from the biological source to every designed sequence when a change in source identity could change the product.
- Do not reduce a sequence-derived target to a gene name, mutation label, protein position, or other display label when the exact sequence depends on additional context.
- Preserve the reference sequence, transcript or isoform, phase or haplotype, patient-specific sequence context, and other upstream identity needed to reconstruct an engineered target.
- Treat nearby sequence variation as potentially relevant when it changes the source sequence from which a target is derived.
- Distinguish predicted binding, processing, presentation, receptor recognition, immunogenicity, tumour-cell recognition, and clinical efficacy. Evidence for one does not establish the next.
- Preserve the exact host or patient context required by a prediction, including HLA identity for peptide-presentation models.
- Interpret scores according to the model target and version. A score, rank, percentile, affinity estimate, or heuristic utility is not automatically a calibrated probability.
- Distinguish missing or unresolved evidence from evidence against a candidate.
- Preserve the candidate universe and material exclusion rules when interpreting why a target was or was not selected.
- Treat a finite multi-target product as a set-design problem when redundancy, dependence, biological coverage, construct length, or sequence compatibility can make independent top-ranked candidates an inappropriate selection rule.
- Do not assume that overlapping peptides, targets from the same molecular event, or targets using the same presentation route provide independent biological coverage.
- Evaluate the final construct in its engineered sequence context. Individually acceptable components can create different behaviour when concatenated, reordered, trimmed, linked, or sequence-engineered.
- Treat artificial junction sequence as novel sequence context that can require separate evaluation.
- Keep amino-acid sequence identity distinct from nucleotide sequence identity. Synonymous nucleotide designs can differ in RNA behaviour while encoding the same amino-acid sequence.
- Preserve the exact final digital design and its version when it is transferred into manufacturing or another physical production process.
- Distinguish peer-reviewed methods, research implementations, patent embodiments, inferred design principles, and confirmed production methods.
- When a design is regenerated after changes to input data, references, prediction models, thresholds, target order, or sequence engineering, treat it as a new design unless equivalence has been established.

## AI behaviour

Before recommending, interpreting, comparing, or reproducing an engineered biological design:

1. identify the biological source and relevant specimen or host context,
2. establish the exact molecular identity from which each candidate sequence was derived,
3. determine which quantities were measured and which were predicted,
4. establish the target and semantics of every material model output,
5. identify unresolved evidence rather than silently converting it into a negative result,
6. preserve the complete host-specific context required by the design,
7. establish the candidate universe and material inclusion or exclusion rules,
8. determine whether selection is performed per candidate or over the complete finite target set,
9. check material dependencies and redundancy between selected targets,
10. evaluate effects created by the final construct rather than reasoning only from isolated components,
11. preserve the exact amino-acid and nucleotide design objects and their provenance,
12. state when a method is illustrative, experimental, patent-described, or confirmed production practice.

For personalised cancer vaccines, do not collapse:

```text
somatic event
→ patient-specific altered sequence
→ candidate peptide
→ peptide:HLA prediction
→ presented peptide:HLA
→ T-cell-recognised target
→ selected vaccine target
→ encoded construct
```

into one generic label such as:

```text
neoantigen
```

when the distinction affects the claim.

If the exact source sequence, HLA context, model semantics, or construct identity required for a conclusion cannot be recovered, state that limitation rather than silently substituting a common default.

## References

Read the relevant reference when the task depends on it:

- [`references/neoantigen-identity-and-evidence.md`](references/neoantigen-identity-and-evidence.md) for patient-specific source identity, tumour-normal evidence, variants, transcripts, haplotypes, mutant versus self sequence, RNA evidence, and clonality
- [`references/hla-presentation-and-immunogenicity.md`](references/hla-presentation-and-immunogenicity.md) for HLA identity, peptide:HLA prediction, model-score semantics, processing, presentation, T-cell recognition, tumour presentation state, and experimental validation
- [`references/target-set-selection-under-uncertainty.md`](references/target-set-selection-under-uncertainty.md) for candidate universes, missing evidence, score calibration, dependence, redundancy, uncertainty, and finite multi-target selection
- [`references/mrna-polyepitope-construct-design.md`](references/mrna-polyepitope-construct-design.md) for target order, junction sequence, source context, amino-acid versus nucleotide design, mRNA sequence identity, and design-to-manufacturing provenance
