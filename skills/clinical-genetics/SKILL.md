---
name: clinical-genetics
description: Apply clinical-genetics correctness rules when family history, pedigree relationships, phenotypes, diagnoses, reproductive history, samples, and genomic findings are represented, exchanged, or analysed. Use for individual clinical pedigrees, EHR and FHIR exchange, rare-disease and segregation analysis, and cohort or biobank-scale pedigree processing where identity, relationship semantics, clinical-state semantics, reproductive roles, or lossy analytical formats can change the genetic interpretation.
---

# Clinical genetics

Use this skill when family structure and clinical or genomic information are being represented together and correctness depends on preserving what each person, relationship, observation, and genetic finding actually means.

The same semantic rules apply whether the task concerns one family in clinic or thousands of pedigrees processed jointly on a cluster:

```text
person and family history
      ↓
structured clinical pedigree
      ↓
clinical and genomic observations
      ↓
interoperable health record
      ↓
analysis-specific projection
      ↓
segregation or cohort analysis
```

A pedigree diagram is a view of the record. It is not the record itself.

This skill focuses on clinical pedigree semantics, family-graph integrity, interoperability, and valid genetic interpretation. It does not replace clinical genetics practice guidelines, genomic variant standards, EHR specifications, or analysis-tool documentation.

## Core rules

- Treat the structured family graph as the source of truth and derive visual layout from it.
- Keep stable person identity separate from pedigree display identifiers, sample identifiers, external EHR identifiers, and analysis-specific identifiers.
- Do not use generation number, left-to-right position, or a rendered pedigree label as the only persistent key for a person.
- Keep people, partner or parental unions, parentage links, reproductive events, pregnancies or reproductive outcomes, samples, phenotypes, diagnoses, and genomic findings as distinct semantic objects when their distinctions affect interpretation.
- Distinguish biological parentage from adoptive, legal, social, gestational, donor, and intended-parent relationships.
- Do not infer genetic inheritance from a partner relationship or from visual proximity in a pedigree.
- Preserve sperm contributor, ovum contributor, gestational carrier, and intended-parent roles separately when assisted reproduction is relevant.
- Do not infer reproductive contribution solely from gender identity, symbol shape, partner order, or left-to-right layout.
- Keep sex-related data used for genetic analysis, sex assigned at birth, gender identity, reproductive role, and display-symbol semantics separate when more than one is represented.
- Treat proband and consultand as case roles, not immutable biological properties of a person.
- Distinguish affected, unaffected, unknown or uncertain, and not assessed. Missing status is not automatically unaffected.
- Keep phenotype, diagnosis, clinical status, carrier state, test status, and display fill separate.
- Preserve age or time context when a negative phenotype or apparently unaffected status depends on age-related penetrance or the time of assessment.
- Treat pregnancy and reproductive-outcome records explicitly. Do not allow a pregnancy loss, ongoing pregnancy, or stillbirth record to be silently interpreted as an ordinary living individual.
- Preserve gestational age, outcome, fetal-sex annotation where appropriate, and how fetal sex was determined when these are material.
- Preserve twin or multiple-birth grouping and zygosity separately. Unknown zygosity is not dizygosity.
- Distinguish one individual from an aggregate symbol representing several equivalent individuals.
- Keep union-level facts such as consanguinity, relationship status, infertility, and no-children status attached to the relationship rather than arbitrarily to one partner.
- Preserve exact genomic finding identity, zygosity, phase, inheritance assessment, classification, testing status, and sample linkage when these affect segregation.
- Do not call a finding de novo solely because it was not observed in stored parental results. Establish whether the relevant genetic contributors were adequately tested.
- Do not call two variants compound heterozygous merely because both occur in one person. Preserve constituent variants and phase or equivalent parental-origin evidence.
- Keep observed genotype, inferred inheritance, and clinical interpretation as separate evidence layers.
- Preserve the source and provenance of manually entered, imported, clinically reported, inferred, and computationally derived pedigree information.
- Version the pedigree schema and preserve migration provenance when historical records are upgraded.
- Validate referential integrity, duplicate identifiers, impossible self-relations, and biological cycles before analysis or exchange.
- At cohort scale, keep family identity and person identity namespaced so unrelated families cannot be joined accidentally.
- Treat FHIR, PLINK, and other exchange formats as projections with different expressive power rather than interchangeable serialisations of the same semantics.
- Do not use PLINK FAM or PED as the canonical clinical pedigree when the source record contains semantics that those formats cannot represent.
- Prefer explicit export failure or a documented lossy mode over silently dropping adoption, reproductive, pregnancy, aggregate, or uncertain-state semantics.
- Preserve round-trip information when an interoperable format cannot natively express every pedigree concept, using documented extensions or an attached full-fidelity representation where appropriate.

## AI behaviour

Before constructing, interpreting, converting, comparing, or analysing a pedigree:

1. identify the case or family namespace and the stable identity of each person,
2. determine which relationships are biological and which are adoptive, social, gestational, donor, or intended-parent relationships,
3. identify the genetic contributors relevant to inheritance rather than inferring them from presentation or partner order,
4. distinguish clinical status from phenotype, diagnosis, carrier state, molecular findings, and display conventions,
5. distinguish unknown, not assessed, unavailable, and explicitly negative observations,
6. establish whether pregnancy, fetal, twin, grouped-individual, adoption, or assisted-reproduction semantics are present,
7. preserve sample and genomic-finding identity separately from the person record,
8. determine which segregation statements are observed and which are inferred,
9. check phase and contributor testing before asserting compound heterozygosity or de novo inheritance,
10. validate the family graph for broken references, duplicate identifiers, impossible self-relations, and biological cycles,
11. identify which semantics the requested export or analysis format cannot represent,
12. state or preserve any information loss rather than silently coercing the pedigree into a simpler model.

Do not collapse:

```text
person
+ biological parentage
+ adoptive or social relationships
+ reproductive contributors
+ pregnancy history
+ phenotype and diagnosis
+ genomic findings
+ samples and testing
+ provenance
```

into:

```text
pedigree symbol + father ID + mother ID + affected yes/no
```

when the richer semantics affect the clinical or genetic claim.

If a requested transformation cannot preserve the meaning required for the intended analysis, keep the richer source record and describe the simpler output as a lossy projection.

## References

Read the relevant reference when the task depends on it:

- [`references/pedigree-data-semantics-and-interoperability.md`](references/pedigree-data-semantics-and-interoperability.md) for clinical pedigree data modelling, family-graph semantics, identity, phenotype state, reproductive relationships, pregnancies, twins, genomic findings, FHIR and EHR exchange, PLINK projection, validation, and cohort-scale analysis

