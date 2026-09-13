# Style guide

Biology Skills is written for AI agents and expert human reviewers. It is not a textbook.

## Length

Targets:

- `SKILL.md`: 200 to 600 words
- hard maximum for `SKILL.md`: 900 words
- `Core rules`: 60 to 200 words
- normal reference topic: 300 to 1,200 words
- split a topic before about 2,000 words unless the material is inseparable

Brevity is a correctness feature. Operational rules should be easy for an agent to find and apply.

## Required topic sections

Every reference topic contains:

1. `Summary`
2. `Core rules`
3. `Required context`
4. `AI behaviour`
5. `Common failure modes`
6. `Authoritative standards`
7. `Examples`
8. `Sources`

These headings also define generated short, standard, and complete views.

## Writing rules

- State rules directly.
- Prefer one biological claim per bullet.
- Distinguish requirements from recommendations.
- Do not hide important conditions in examples.
- Avoid universal claims unless they are genuinely universal.
- Name the biological object precisely: gene, transcript, protein isoform, allele, genotype, sample, cell type, assay, population, or other relevant unit.
- Preserve distinctions between observation, measurement, prediction, association, interpretation, mechanism, and causality.
- Explain why a standard matters locally, but cite its authority for exact normative syntax.
- Use concrete failure cases when they improve agent behaviour.
- Remove background detail that does not change what the agent should know or do.

## Skill versus reference

`SKILL.md` should answer:

- when the domain matters
- which checks the agent must perform
- which reference files to consult
- which assumptions must not be made silently

A reference topic should answer:

- what the biological distinction is
- why it matters
- what information must be preserved
- how an AI system should behave
- which authoritative source governs formal details

## Review language

Do not call content expert-reviewed, verified, consensus, authoritative, or definitive unless its review status and sources support that claim.
