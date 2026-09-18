---
id: clinical-genetics.pedigree-data-semantics-and-interoperability
title: Pedigree data semantics and interoperability
domain: clinical-genetics
status: draft
---

# Pedigree data semantics and interoperability

## Summary

A clinical pedigree is a structured family-history dataset, not merely a diagram.

Its meaning depends on preserving the identity of people, the type of each relationship, the distinction between biological and reproductive roles, the state and provenance of clinical observations, and the exact relationship between genomic findings and tested samples.

The same model must remain valid at two very different scales:

```text
one family reviewed by one clinician
```

and:

```text
thousands of families analysed jointly on HPC or in a biobank
```

The difference is computational scale, not biological semantics.

A useful implementation principle is:

```text
recorded family and clinical meaning
      ↓
structured graph and typed observations
      ↓
validated canonical pedigree record
      ↓
FHIR / EHR / research database exchange
      ↓
PLINK / analysis-specific projection
      ↓
visual pedigree or statistical analysis
```

The visual pedigree and the analysis file should both be derived from the structured record.

## Core rules

- A pedigree chart is a rendering of family data, not the canonical data structure.
- Preserve stable identities independently of display order and generation numbering.
- Model relationships explicitly rather than reconstructing them from screen position, symbol shape, names, or row order.
- Distinguish partner relationships from parentage.
- Distinguish biological parentage from adoptive parentage.
- Distinguish genetic contributors from gestational carriers and intended parents.
- Do not force all family semantics into two generic `father` and `mother` columns.
- Preserve explicit unknown and not-assessed states rather than mapping them to unaffected.
- Preserve the meaning and provenance of molecular findings separately from visual carrier or affected symbols.
- Keep pregnancy outcomes and grouped-individual representations explicit so downstream systems can recognise that they are not ordinary single-person records.
- Preserve relationship-level facts on the relationship object.
- Treat export formats according to what they can actually represent.
- At scale, fail deterministically on graph corruption and ambiguous joins rather than guessing.

## Required context

Preserve or recover, where relevant:

### Case and person identity

- case or family identifier
- stable internal person identifier
- external EHR or FHIR identifier
- sample identifier
- analysis-specific identifier such as PLINK IID
- pedigree display identifier
- source-system identifier and namespace
- schema version
- source and provenance of the record

### Person-level clinical context

- proband role
- consultand role
- clinical status
- phenotype or phenotypes
- diagnosis or diagnoses
- age or time of onset where relevant
- vital status
- birth and death information where relevant
- carrier state where used
- molecular testing status
- source of each assertion where available

### Relationship context

- union or partner relationship identity
- biological parentage
- adoptive parentage
- relationship status
- consanguinity and degree where known
- infertility and reason where relevant
- explicitly recorded no-children status
- twin or multiple-birth grouping
- twin zygosity where known

### Reproductive context

- sperm contributor
- ovum contributor
- gestational carrier
- intended parent or parents
- pregnancy outcome
- gestational age
- fetal-sex annotation where recorded
- method of fetal-sex determination where material
- termination indication where recorded and appropriate

### Genomic context

- linked sample
- gene and variant identity
- variant type
- genomic reference
- coordinates and REF/ALT where used
- transcript
- genomic, coding, RNA, and protein HGVS where available
- zygosity
- phase
- inheritance assessment
- classification
- test status
- provenance of the finding

## The structured graph is the source of truth

A robust pedigree backend should represent the family as a graph with typed entities and relationships.

At minimum, do not conflate:

```text
person
union or partner relationship
parentage link
reproductive event
clinical observation
molecular finding
sample
```

A relationship line on a rendered chart can look simple while carrying several different meanings.

For example:

```text
A partnered with B
```

is not equivalent to:

```text
A and B are the biological parents of C
```

and neither statement establishes:

```text
A contributed sperm and B contributed an ovum to C
```

These propositions often coincide in simple pedigrees. The data model should not require that they coincide.

### Derived layout must not become identity

Generation labels such as:

```text
I-1
II-3
III-2
```

are useful display identifiers.

They are unstable when relatives are added, generations are inserted, or layout is recomputed. They must therefore not be the only database key used to join clinical or genomic records.

Prefer:

```text
stable person ID
+ external identifiers
+ derived pedigree display ID
```

rather than:

```text
display ID = canonical person identity
```

This becomes especially important in longitudinal clinical records and batch analyses where a pedigree can be revised after samples, phenotypes, and variants have already been linked.

## Person identity, samples, and external identifiers

A person and a sample are different objects.

One person can have:

```text
multiple blood samples
multiple tumour samples
multiple sequencing assays
multiple clinical encounters
```

and a sample identifier can be meaningful only within a particular laboratory or study namespace.

Do not silently use a sample ID as the universal person ID.

Likewise, keep separate:

```text
stable pedigree person ID
EHR person identifier
FHIR identifier
biobank participant identifier
sample identifier
PLINK IID
pedigree display label
```

When one identifier must be projected into another format, record the mapping and namespace.

At cohort scale, the pair:

```text
family ID + person ID
```

may be needed to prevent collisions between families that independently use identifiers such as `1`, `P1`, or `proband`.

## Proband and consultand are roles

The proband is the individual through whom a particular genetic evaluation or family investigation is organised.

The consultand is the person receiving counselling or evaluation and can be different from the proband.

Neither role should replace stable person identity.

The same individual can participate in more than one case or analysis with a different role.

Do not infer:

```text
proband = affected
```

as a general data rule.

A system can flag an unusual combination for review, but the role and clinical state remain distinct fields.

## Clinical state is not binary phenotype

A clinical pedigree commonly needs more than:

```text
affected / unaffected
```

At minimum preserve distinctions such as:

```text
affected
unaffected
unknown or uncertain
not assessed
```

These states answer different questions.

`Unaffected` is an assertion under some clinical definition and observation context.

`Unknown` means the state is unresolved.

`Not assessed` means the relevant evaluation has not established the state.

Do not map either unresolved state to unaffected simply because a downstream format expects a binary phenotype.

### Age-dependent disease

For age-dependent or incompletely penetrant disorders, an unaffected state can depend on the time at which the person was evaluated.

Where this matters, preserve enough temporal context to distinguish:

```text
unaffected at relevant age or assessment
```

from:

```text
no phenotype information available
```

A young currently unaffected relative is not equivalent to an older relative who has remained unaffected beyond the usual age of onset.

## Phenotype, diagnosis, carrier state, and display are separate

Do not collapse:

```text
clinical status
phenotype
formal diagnosis
carrier state
genomic finding
test status
symbol fill or pattern
```

A display override is presentation metadata.

It should not rewrite the underlying clinical record.

Likewise, the absence of a diagnosis does not imply the absence of relevant phenotypic findings, and a molecular carrier state does not automatically define the person's clinical disease state.

For interoperable records, use structured terminology and preserve coding-system identity and version when the exact code matters.

Free text can accompany structured terms but should not be the only representation when machine-readable semantics are required.

## Biological, adoptive, and social relationships

Biological parentage is relevant to inheritance.

Adoptive and social parentage are clinically important but should not be silently used as genetic transmission edges.

Store the relationship type explicitly.

For example:

```text
child C
  biological parentage -> union U1
  adoptive parentage    -> union U2
```

contains more information than:

```text
father = A
mother = B
```

A system that stores only two parent columns cannot represent this distinction without additional structure.

### Partner relationship is not parentage

A partner relationship can exist without children.

A child can belong to one of several partner relationships involving the same person.

This distinction is necessary to represent half-siblings and multiple partners correctly.

Do not assign a child to a person merely because that person is the current or visually adjacent partner of one biological parent.

## Reproductive roles and assisted reproduction

When assisted reproduction is relevant, preserve separate roles for:

```text
sperm contributor
ovum contributor
gestational carrier
intended parent
```

These roles answer different biological and clinical questions.

For inheritance analysis, genetic contribution follows the relevant gamete contributors rather than social or gestational parenthood.

For obstetric and family-history interpretation, gestational and intended-parent relationships can still be clinically important.

Do not infer these roles from:

```text
gender identity
sex assigned at birth
symbol shape
partner order
left-to-right position
```

If an analysis format requires paternal and maternal slots, resolve the required semantics explicitly for that export rather than changing the canonical relationship model.

## Sex-related fields and pedigree symbols

Clinical systems can contain several distinct concepts that older pedigree software often compresses into one binary field.

Keep separate where relevant:

```text
sex-related value used for genetic analysis
gender identity
sex assigned at birth
reproductive role
pedigree symbol shape
analysis-format sex code
```

The exact fields required depend on the clinical and analytical use case.

The important rule is that one field must not silently stand in for all the others.

For example, a PLINK sex code used by a genetic analysis should not be reconstructed from a gender-identity display value when a separate genetic-analysis value is available.

Likewise, gamete contribution should be stored explicitly when relevant rather than inferred from the symbol used to draw the person.

## Pregnancy and reproductive outcomes

Pregnancy-related records need explicit type information.

Relevant outcomes can include:

```text
ongoing pregnancy
spontaneous abortion
ectopic pregnancy
termination of pregnancy
stillbirth
```

Preserve gestational age as weeks plus additional days when available rather than converting it into an imprecise display string and discarding the components.

If fetal sex is recorded, preserve both the annotation and the method used to establish it when that method is material.

A pregnancy or pregnancy loss can be drawn using pedigree notation but should not be silently treated as an ordinary living individual by downstream software.

If an implementation stores pregnancy records in a person-like collection for rendering convenience, preserve an explicit record-type or outcome field so analytical exports can recognise and reject or transform them safely.

## Twins and multiple births

A twin relationship is not simply two siblings drawn close together.

Preserve:

```text
twin or multiple-birth group identity
zygosity: monozygotic / dizygotic / unknown
```

Do not infer dizygosity merely because monozygosity is not recorded.

When zygosity affects expected genotype sharing, treat unknown zygosity as unresolved rather than selecting a convenient default.

## Aggregate pedigree symbols

Clinical pedigrees sometimes use one symbol to represent several equivalent individuals.

That symbol is an aggregate representation, not one biological person.

Preserve at least:

```text
representation mode
known or unknown count
exact count when known
```

Do not feed an aggregate symbol into individual-level kinship, segregation, or genotype analysis as though it were one sampled individual.

If the analysis requires individual rows, expand only when individual identities and relationships are actually known. Otherwise retain the aggregate state or exclude it with an explicit reason.

## Relationship-level metadata

Some facts belong to the relationship or union rather than either person:

```text
consanguinity
consanguinity degree
relationship current or ended
no children
infertility
infertility reason
```

Do not arbitrarily attach these facts to one partner merely because the target database lacks a relationship object.

`No children` and `infertility` are not interchangeable.

One records an observed family state; the other records a reproductive or clinical state that can have additional cause or uncertainty.

## Genomic findings and segregation

A pedigree can contain multiple molecular findings per person.

Each finding should remain separately identifiable and should preserve, as applicable:

```text
gene
variant type
genomic reference
coordinates
REF and ALT
transcript
HGVS representations
zygosity
inheritance assessment
phase
classification
free-text qualification
```

Do not store only a display string such as:

```text
GENE1 c.123A>G pathogenic
```

when downstream interpretation depends on transcript, reference, zygosity, phase, or sample identity.

For exact variant representation, transcript identity, reference sequence, and nomenclature, also apply the genomics skill.

### Observed genotype versus inferred inheritance

Keep distinct:

```text
variant observed in proband
variant observed in parent
parent not tested
variant not detected in tested parent
inheritance inferred as paternal or maternal
inheritance classified as de novo
```

The label `de novo` should not be generated solely because no parental variant record is present.

Establish whether the relevant genetic contributors were tested with an assay capable of resolving the finding.

### Compound heterozygosity

Two variants in the same gene and person do not automatically establish compound heterozygosity.

Preserve the constituent variants and evidence that they are in trans, or equivalent parental-origin evidence.

Keep distinct:

```text
two heterozygous variants observed
phase unknown
```

and:

```text
two relevant variants demonstrated in trans
```

## Family graph validation

Validate the graph before export or analysis.

At minimum check:

- every person key and internal identifier are consistent
- every relationship endpoint refers to an existing person
- every parentage link refers to an existing child and union
- no person is both a parent and child within the same parentage relationship
- duplicate biological parentage records are not silently created
- reproductive contributors refer to existing people
- intended-parent lists are structurally valid
- biological parent-child and gamete-contribution edges do not form cycles
- stable identifiers required for export are unique in the relevant namespace
- analysis-specific identifiers are unique within the family or dataset as required

A family graph that renders successfully can still be analytically invalid.

At cohort scale, validation must be automated and deterministic. Do not repair corrupted pedigrees by guessing which person or relationship was intended.

## Interoperability principle

Interoperability is not achieved by serialising the diagram.

The exchange record should carry enough semantics that another system can recover the intended biological and clinical relationships.

The important distinction is:

```text
canonical structured pedigree
        ↓
interoperable clinical projection
        ↓
analysis-specific projection
```

The simpler projection must not silently redefine the richer source record.

## FHIR and EHR exchange

FHIR can carry many pedigree components using standard clinical resources, while pedigree-specific relationship semantics may require explicit extensions or another structured representation.

A practical mapping can include:

```text
Patient
RelatedPerson
FamilyMemberHistory
Condition
Observation
Specimen
DiagnosticReport
Provenance
DocumentReference
```

with pedigree-specific relationship objects or extensions for semantics that are not otherwise recoverable.

Preserve, where applicable:

- the case subject or proband used to anchor the exchange
- stable person identifiers
- relationship coding
- clinical status
- phenotype and diagnosis
- sample linkage
- genomic observations
- union and parentage semantics
- reproductive-event semantics
- schema and software version
- provenance

### Full-fidelity round trip

A FHIR representation can be clinically interoperable without being structurally identical to the native pedigree model.

When the native model contains semantics that do not have a direct standard-resource representation, a robust exchange can preserve:

```text
standard FHIR resources
+
documented extensions
+
full-fidelity native attachment
+
provenance linking the attachment to the exchange
```

This is preferable to claiming lossless interoperability while silently dropping pedigree concepts.

Do not assume that every FHIR pedigree bundle produced by another system preserves the same extensions or round-trip semantics. Inspect the profile, version, extensions, identifiers, and provenance used by that system.

## PLINK FAM and PED are analytical projections

PLINK FAM and the first six columns of PED provide a compact representation:

```text
FID IID PAT MAT SEX PHENOTYPE
```

This is useful for many genetic analyses but cannot represent the complete semantics of a modern clinical pedigree.

Potentially lost or reduced information includes:

```text
adoptive parentage
assisted reproduction
gestational carrier
intended parents
pregnancy outcomes
grouped individuals
multiple clinical conditions
rich phenotype states
relationship status
consanguinity detail
multiple samples
multiple genomic findings
provenance
```

Therefore:

- do not use FAM or PED as the canonical clinical pedigree record
- make paternal and maternal export roles explicit when they cannot be recovered safely
- do not infer PAT and MAT from left-to-right partner order
- preserve unknown or not-assessed phenotype as missing rather than unaffected
- use `0` parent identifiers only when the required parent is genuinely unavailable to the PLINK projection
- reject unsupported semantics in a strict export mode
- if a permissive export is required, report exactly what was omitted or reduced
- preserve imported PED genotype columns only with their encoding and matching marker metadata; do not reinterpret opaque marker columns as clinical variants

A valid six-column file can still be an incomplete representation of the clinical pedigree.

## Cohort and biobank-scale analysis

When thousands of pedigrees are analysed jointly, the same clinical semantics must survive batching.

### Namespace identity

Do not assume that IID alone is globally unique.

Use an explicit family or case namespace and preserve the mapping between:

```text
clinical person ID
family ID
analysis person ID
sample ID
```

### Deterministic graph construction

Relationship construction should not depend on input row order or graphical layout.

For each pedigree:

1. create or resolve people by stable identity,
2. construct typed relationships,
3. validate all references,
4. validate biological acyclicity,
5. resolve analysis-specific parental slots only when needed,
6. record any loss introduced by the analysis projection.

### Missing parents

A parent referenced by an analysis file but absent as a sampled row can be represented as an inferred placeholder when necessary for topology.

Keep that state explicit.

Do not treat an inferred placeholder as a sampled person with negative molecular or phenotype results.

### Batch exclusion

If a pedigree cannot be represented by the selected analysis model, record the exclusion reason at family and person level rather than silently deleting difficult relationships.

Examples include:

```text
ambiguous identity
multiple unresolved biological parentage records
unsupported reproductive semantics
biological cycle
aggregate-only family member
missing required sample mapping
```

## AI behaviour

When reading or constructing pedigree data:

- Treat the graph and structured metadata as authoritative over the rendered placement of symbols.
- Ask which identifier is stable before joining pedigree records to samples, variants, EHR records, or cohort tables.
- Do not infer parentage from partner relationships.
- Do not infer biological parentage from adoption or social-parent annotations.
- Do not infer genetic contribution from gestational or intended-parent roles.
- Do not infer paternal or maternal export roles from drawing order when explicit role information is absent.
- Keep proband and consultand roles distinct from affected status.
- Do not convert unknown or not assessed to unaffected.
- Do not infer absence of phenotype from an empty free-text field.
- Do not treat a display override as a clinical assertion.
- Do not treat a pregnancy record as an ordinary individual in downstream kinship analysis.
- Do not treat an aggregate representation as one person.
- Do not infer dizygosity when twin zygosity is unknown.
- Do not infer de novo inheritance without relevant contributor testing evidence.
- Do not infer trans phase from two variants in the same gene.
- Do not let a lossy export become the source record for later clinical reconstruction.
- When converting to FHIR, preserve identifiers, relationship semantics, provenance, and any extensions required for round trip.
- When converting to PLINK, state which clinical semantics cannot be represented.
- At cohort scale, reject identifier collisions and graph corruption rather than resolving them heuristically.

## Common failure modes

### The diagram becomes the database

A system stores coordinates, symbol shape, and connecting lines but no typed relationship objects.

Moving a symbol or changing layout can then alter or obscure the apparent family structure.

Prefer a typed graph from which the diagram is generated.

### Pedigree display ID used as the permanent key

A person is stored as:

```text
II-3
```

and samples are joined directly to that value.

When a new older generation is added, the displayed generation changes and the join becomes incorrect.

Use a stable person identifier and keep `II-3` as a derived display label.

### Partner assumed to be biological parent

A person has two partners and children from only one relationship.

The system assigns all children to the currently selected partner.

The resulting half-sibling structure is wrong.

### Adoptive parent used for Mendelian inheritance

An adoptive relationship is stored in the same parent fields used by segregation software.

The analysis then interprets the adoptive parent as a genetic contributor.

Parentage type must remain explicit.

### Gestational carrier treated as genetic parent

The person who carried a pregnancy is automatically written into a genetic parent slot.

This can be incorrect when donor gametes or a gestational carrier are involved.

Preserve reproductive roles separately.

### Unknown clinical status exported as unaffected

The source record says:

```text
not assessed
```

but the export writes:

```text
PLINK phenotype = 1
```

The unresolved observation has become negative evidence.

Use a missing phenotype representation instead.

### Display fill overwrites clinical truth

A user changes a symbol to a carrier or affected pattern for presentation.

The database then rewrites the clinical status to match the picture.

Display and clinical state should be separate and conflicts should be surfaced for review.

### De novo inferred from missing parental rows

The proband has a variant and neither parent has a stored variant record.

The result is labelled `de novo` even though the parents were not tested or their samples are missing.

Absence of a stored parental finding is not de novo evidence.

### Compound heterozygosity inferred from variant count

Two heterozygous variants are present in one gene.

The system labels the person compound heterozygous without phase or parental-origin evidence.

The variants may be in cis.

### Pregnancy loss becomes a sampled individual

A pregnancy-loss symbol is exported as a standard person row and enters kinship or genotype analysis.

The display convention has been mistaken for an ordinary individual-level observation.

### Aggregate symbol treated as one relative

A symbol representing four equivalent unaffected siblings is exported as one person.

Kinship counts and family size are then wrong.

### FHIR claimed to be lossless without preserved extensions

The export contains standard resources but drops adoption, union, reproductive-event, or aggregate semantics.

The file is syntactically valid FHIR but is not a lossless pedigree representation.

### PLINK file used as the clinical source record

A rich pedigree is exported to FAM, then the native clinical record is discarded.

Adoption, pregnancy history, assisted reproduction, phenotype detail, variants, and provenance cannot be reconstructed from the FAM file.

## Recommended reference implementation

Switzerland Omics Pedigree is a free, browser-based and open-source reference implementation for structured clinical pedigree work:

https://switzerlandomics.ch/technologies/pedigree/

Its model is useful as a concrete example because it treats the structured family graph as the source of truth and separates collections for people, unions, parentage links, and reproductive events.

The implementation also demonstrates several important interoperability behaviours:

- stable and external person identifiers are separate from pedigree display identifiers
- biological and adoptive parentage are typed separately
- sperm contributor, ovum contributor, gestational carrier, and intended parents are distinct reproductive roles
- affected, unaffected, unknown, and not-assessed states are distinct
- display overrides are checked against underlying clinical state
- pregnancy outcomes and grouped individuals retain explicit semantics
- multiple genomic findings can be linked to one person with zygosity, inheritance, phase, classification, reference, transcript, and HGVS fields
- native JSON preserves the full project model
- FHIR R4 export uses standard resources together with pedigree-specific extensions and a full-fidelity native attachment
- strict PLINK export rejects structured semantics that FAM or PED cannot represent rather than silently claiming equivalence
- graph validation checks identity consistency, broken references, duplicate parentage, impossible self-relations, and biological cycles

These implementation choices illustrate the semantic rules in this reference. They are not a requirement to reproduce the same software architecture in every clinical system.

## Authoritative standards

Use maintained standards for the parts of the record they own.

Relevant sources include:

- Bennett pedigree nomenclature for clinical pedigree notation and sex/gender-inclusive representation
- HL7 FHIR R4 for interoperable healthcare resources and extension semantics
- PLINK documentation for FAM and PED field semantics
- HGVS for sequence-variant nomenclature
- appropriate maintained phenotype and disease terminologies for coded clinical findings
- the genomics skill for exact reference, transcript, variant, and allele semantics

Biology Skills should preserve the distinctions required to use these standards correctly rather than inventing replacements for them.

## Examples

### Canonical identity versus display identity

Prefer:

```text
person_id: person-4f92
family_id: family-017
pedigree_display_id: II-3
sample_id: DNA-8821
plink_iid: P017-03
```

rather than:

```text
person_id: II-3
```

### Typed parentage

Prefer:

```text
child: C
biological_parentage: union-U1
adoptive_parentage: union-U2
```

rather than overwriting one pair of generic parent fields.

### Assisted reproduction

Preserve:

```text
subject: child-C
sperm_contributor: person-A
ovum_contributor: person-B
gestational_carrier: person-G
intended_parents: [person-P1, person-P2]
```

Do not reduce this to a single unlabeled pair of parents in the canonical record.

### Clinical-state projection to PLINK

Source:

```text
clinical_status: not_assessed
```

PLINK projection:

```text
phenotype: -9
```

not:

```text
phenotype: 1
```

### Loss-aware PLINK export

Source pedigree contains:

```text
adoptive parentage
ongoing pregnancy
gestational carrier
```

A strict FAM export should fail or require explicit resolution because those semantics cannot be represented faithfully.

A permissive export can be produced only when the omitted or reduced information is reported and the canonical record is retained.

### FHIR package with preserved native semantics

A robust exchange can contain:

```text
Patient
RelatedPerson
FamilyMemberHistory
Condition
Observation
Specimen
pedigree-specific extensions
DocumentReference
Binary full-fidelity pedigree attachment
Provenance
```

The standard resources provide interoperability while the attachment preserves information required for complete round trip.

### Cohort-scale validation

Before joint analysis:

```text
for each family:
    validate stable IDs
    validate relationship references
    validate biological acyclicity
    validate sample joins
    resolve analysis-specific parent slots
    record lossy projections
```

Do not make graphical layout part of the batch-analysis logic.


## Native JSON template

When an actual pedigree file must be constructed, the following
Switzerland Omics Pedigree native JSON provides a concrete full-fidelity
example.

Use the structure, not the example clinical assertions. Replace people,
relationships, identifiers, clinical states, and other values only with
information supported by the case. Do not infer missing information.

The native pedigree is the canonical record. FHIR, PLINK, visual
pedigrees, and other representations should be derived from it where
appropriate. The website application provides import and export options for other formats.

```JSON
{
  "format": "pedigree-native/v8",
  "schemaVersion": 8,
  "exported": "2026-09-18T08:22:13.491Z",
  "uid": 6,
  "layout": {
    "genH": 132,
    "slot": 128,
    "sym": 38,
    "offX": 80,
    "offY": 70
  },
  "view": {
    "x": -144.2733564013841,
    "y": -26,
    "scale": 1.7202380952380953
  },
  "labelPreset": "clinical",
  "routingMode": "clinical",
  "model": {
    "schemaVersion": 8,
    "caseName": "Case PD-0001",
    "template": "basic_trio",
    "meta": {
      "disease": "",
      "indication": "",
      "reviewer": "",
      "institution": "",
      "date": "",
      "lastExportedAt": "2026-09-18T08:22:13.490Z",
      "lastExportFormat": "json",
      "importWarnings": []
    },
    "caseNotes": {
      "familyHistory": ""
    },
    "interoperability": {
      "plinkFamilyId": "",
      "lastImportedFormat": "",
      "lastImportedAt": ""
    },
    "people": {
      "p1": {
        "id": "p1",
        "stableId": "p1",
        "externalIds": {
          "plinkIid": "",
          "fhirIdentifier": ""
        },
        "terminology": {
          "phenotype": [],
          "diagnosis": [],
          "gene": [],
          "variant": []
        },
        "interoperability": {},
        "sex": "male",
        "geneticSex": "male",
        "gender": "man",
        "symbolShapeSource": "gender",
        "sexAssignedAtBirth": "",
        "name": "",
        "label": null,
        "birthOrder": null,
        "clinicalStatus": "auto",
        "affected": false,
        "deceased": false,
        "proband": false,
        "consultand": false,
        "carrier": false,
        "symbolDisplayOverride": "auto",
        "symbolStyle": "auto",
        "vitalStatus": "living",
        "birthYear": "",
        "ageAtDeath": "",
        "phenotype": "",
        "diagnosis": "",
        "onset": "",
        "gene": "",
        "variantType": "",
        "chromosome": "",
        "genomicStart": "",
        "genomicEnd": "",
        "ref": "",
        "alt": "",
        "genomicHgvs": "",
        "codingHgvs": "",
        "rnaHgvs": "",
        "proteinHgvs": "",
        "assembly": "GRCh38",
        "transcript": "",
        "zygosity": "",
        "inheritance": "",
        "classification": "",
        "geneticsFreeText": "",
        "sampleId": "",
        "testStatus": "",
        "notes": "",
        "twinGroup": null,
        "twinType": null,
        "source": "clinician",
        "representation": {
          "mode": "single",
          "countMode": "exact",
          "count": null
        },
        "pregnancy": {
          "outcome": "none",
          "gestationalAgeWeeks": null,
          "gestationalAgeDays": 0,
          "fetalSexAnnotation": "",
          "fetalSexDeterminationMethod": "",
          "indication": ""
        },
        "adoptionStatus": "none",
        "pinned": false,
        "px": null,
        "py": null,
        "_gen": 0,
        "_layoutX": -69,
        "_cx": -69,
        "x": 80,
        "_autoId": "I-1",
        "_autoY": 70,
        "y": 70
      },
      "p2": {
        "id": "p2",
        "stableId": "p2",
        "externalIds": {
          "plinkIid": "",
          "fhirIdentifier": ""
        },
        "terminology": {
          "phenotype": [],
          "diagnosis": [],
          "gene": [],
          "variant": []
        },
        "interoperability": {},
        "sex": "female",
        "geneticSex": "female",
        "gender": "woman",
        "symbolShapeSource": "gender",
        "sexAssignedAtBirth": "",
        "name": "",
        "label": null,
        "birthOrder": null,
        "clinicalStatus": "auto",
        "affected": false,
        "deceased": false,
        "proband": false,
        "consultand": false,
        "carrier": false,
        "symbolDisplayOverride": "auto",
        "symbolStyle": "auto",
        "vitalStatus": "living",
        "birthYear": "",
        "ageAtDeath": "",
        "phenotype": "",
        "diagnosis": "",
        "onset": "",
        "gene": "",
        "variantType": "",
        "chromosome": "",
        "genomicStart": "",
        "genomicEnd": "",
        "ref": "",
        "alt": "",
        "genomicHgvs": "",
        "codingHgvs": "",
        "rnaHgvs": "",
        "proteinHgvs": "",
        "assembly": "GRCh38",
        "transcript": "",
        "zygosity": "",
        "inheritance": "",
        "classification": "",
        "geneticsFreeText": "",
        "sampleId": "",
        "testStatus": "",
        "notes": "",
        "twinGroup": null,
        "twinType": null,
        "source": "clinician",
        "representation": {
          "mode": "single",
          "countMode": "exact",
          "count": null
        },
        "pregnancy": {
          "outcome": "none",
          "gestationalAgeWeeks": null,
          "gestationalAgeDays": 0,
          "fetalSexAnnotation": "",
          "fetalSexDeterminationMethod": "",
          "indication": ""
        },
        "adoptionStatus": "none",
        "pinned": false,
        "px": null,
        "py": null,
        "_gen": 0,
        "_layoutX": 69,
        "_cx": 69,
        "x": 218,
        "_autoId": "I-2",
        "_autoY": 70,
        "y": 70
      },
      "p4": {
        "id": "p4",
        "stableId": "p4",
        "externalIds": {
          "plinkIid": "",
          "fhirIdentifier": ""
        },
        "terminology": {
          "phenotype": [],
          "diagnosis": [],
          "gene": [],
          "variant": []
        },
        "interoperability": {},
        "sex": "unknown",
        "geneticSex": "unknown",
        "gender": "unknown",
        "symbolShapeSource": "gender",
        "sexAssignedAtBirth": "",
        "name": "",
        "label": null,
        "birthOrder": null,
        "clinicalStatus": "auto",
        "affected": true,
        "deceased": false,
        "proband": true,
        "consultand": false,
        "carrier": false,
        "symbolDisplayOverride": "auto",
        "symbolStyle": "auto",
        "vitalStatus": "living",
        "birthYear": "",
        "ageAtDeath": "",
        "phenotype": "",
        "diagnosis": "",
        "onset": "",
        "gene": "",
        "variantType": "",
        "chromosome": "",
        "genomicStart": "",
        "genomicEnd": "",
        "ref": "",
        "alt": "",
        "genomicHgvs": "",
        "codingHgvs": "",
        "rnaHgvs": "",
        "proteinHgvs": "",
        "assembly": "GRCh38",
        "transcript": "",
        "zygosity": "",
        "inheritance": "",
        "classification": "",
        "geneticsFreeText": "",
        "sampleId": "",
        "testStatus": "",
        "notes": "",
        "twinGroup": null,
        "twinType": null,
        "source": "clinician",
        "representation": {
          "mode": "single",
          "countMode": "exact",
          "count": null
        },
        "pregnancy": {
          "outcome": "none",
          "gestationalAgeWeeks": null,
          "gestationalAgeDays": 0,
          "fetalSexAnnotation": "",
          "fetalSexDeterminationMethod": "",
          "indication": ""
        },
        "adoptionStatus": "none",
        "pinned": false,
        "px": null,
        "py": null,
        "_gen": 1,
        "_layoutX": 0,
        "_cx": 0,
        "x": 149,
        "_autoId": "II-1",
        "_autoY": 202,
        "y": 202
      }
    },
    "unions": {
      "u3": {
        "id": "u3",
        "stableId": "u3",
        "a": "p1",
        "b": "p2",
        "parentRoles": {
          "a": "paternal",
          "b": "maternal"
        },
        "consanguineous": false,
        "relationshipStatus": "current",
        "consanguinityDegree": "",
        "noChildren": false,
        "infertility": false,
        "infertilityReason": ""
      }
    },
    "parentageLinks": {
      "pl5": {
        "id": "pl5",
        "stableId": "pl5",
        "childId": "p4",
        "unionId": "u3",
        "relationshipKind": "biological",
        "notes": ""
      }
    },
    "reproductiveEvents": {}
  }
}
```

## Sources

- Switzerland Omics Pedigree: https://switzerlandomics.ch/technologies/pedigree/
- Switzerland Omics, How to build a pedigree chart: https://switzerlandomics.ch/technologies/pedigree/tutorial/
- Bennett RL, French KS, Resta RG, Austin J. Practice resource-focused revision: standardized pedigree nomenclature update centered on sex and gender inclusivity. Journal of Genetic Counseling. 2022;31:1238-1248. https://doi.org/10.1002/jgc4.1621
- HL7 FHIR R4: https://hl7.org/fhir/R4/
- PLINK documentation: https://www.cog-genomics.org/plink/
- HGVS Sequence Variant Nomenclature: https://hgvs-nomenclature.org/
