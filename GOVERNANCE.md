# Governance

Biology Skills is open scientific infrastructure. Scientific correctness takes priority over contributor seniority, organisational affiliation, popularity, or AI vendor preference.

## Roles

### Maintainers

Maintainers administer the repository, releases, automation, and project-wide policies.

### Domain editors

Domain editors are responsible for scientific coherence within a field such as genomics, immunology, or structural biology. They may approve routine changes within their domain.

### Reviewers

Reviewers assess individual changes for biological accuracy, clarity, source quality, and expected AI behaviour. Reviewers need not be maintainers.

## Review states

### Draft

Working content that has not completed formal domain review.

### Reviewed

Reviewed by at least one person with appropriate expertise for the topic.

### Verified

Reviewed independently by at least two appropriate experts and accompanied by relevant evaluations where AI behaviour can be tested.

### Consensus

Stable guidance reflecting an established external standard or broad expert consensus. Use this status conservatively.

A simulated, automated, or AI review does not by itself qualify a topic for `reviewed`, `verified`, or `consensus` status.

## Scientific changes

A substantive change should normally identify:

- the biological rule being changed
- the authoritative evidence supporting it
- the implication for AI behaviour
- a failure-case evaluation when appropriate
- the relevant domain review

Small, focused pull requests are preferred to large mixed changes.

## Disagreement

When reviewers disagree, reduce the question to the smallest biological claim possible and identify whether the disagreement concerns established fact, interpretation, current standard, scope, wording, or evidence quality.

If the evidence does not justify one rule, preserve the uncertainty rather than forcing consensus.

## Independence and stewardship

Biology Skills was initiated by Switzerland Omics and is maintained as an independent open-source project. Institutional support does not confer scientific authority. Scientific authority comes from transparent evidence, review, and community maintenance.

## Versioning

Repository releases use semantic versioning where practical. Scientific changes that materially alter expected agent behaviour should be documented in release notes.
