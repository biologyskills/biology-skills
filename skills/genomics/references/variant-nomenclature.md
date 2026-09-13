---
id: genomics.variant-nomenclature
title: Variant nomenclature (HGVS)
domain: genomics
status: draft
---

# Variant nomenclature (HGVS)

## Summary

Use HGVS Nomenclature for precise sequence-variant descriptions in genomics and clinical genetics. An HGVS description is defined relative to an explicit reference sequence and coordinate system; the same biological allele may have different valid descriptions at genomic, coding-DNA, RNA, and protein levels.

Biology Skills defines the minimum context and behaviour an AI should preserve. It does not reproduce the full HGVS specification. For exact syntax, complex variants, uncertainty, repeats, allele descriptions, or edge cases, use the current stable HGVS Nomenclature recommendations and validate the result with an appropriate HGVS-aware tool.

## Core rules

- Describe sequence variants relative to an accepted, stable reference sequence. When the reference source uses versioning, preserve the accession and version.
- A genome-build label such as `GRCh38` is not, by itself, an HGVS reference sequence. Prefer an accessioned sequence such as an appropriate versioned `NC_`, `NG_`, `NM_`, `NR_`, `NP_`, `ENST`, or `ENSP` record when reporting HGVS nomenclature.
- Describe variants at the DNA level. RNA and protein descriptions may be added when relevant.
- Distinguish experimentally observed RNA or protein changes from predicted consequences. HGVS uses parentheses for predicted consequences, for example `p.(Ser42Cys)`.
- Use the prefix appropriate to the reference and molecular level: `g.` linear genomic DNA, `m.` mitochondrial DNA, `o.` circular genomic DNA, `c.` coding DNA, `n.` non-coding transcript DNA, `r.` RNA, or `p.` protein.
- For human transcript-based reporting, prefer an appropriate MANE transcript where available. Prefer MANE Select when it is a suitable reference; use MANE Plus Clinical or another justified transcript when clinically important variation is not adequately represented by MANE Select.
- Keep the reference-sequence identifier, transcript or protein accession, and gene symbol conceptually separate. A gene symbol does not replace a reference sequence.
- Apply HGVS numbering and positioning rules, including the HGVS 3′ rule, using the orientation of the reference sequence being described.
- Do not assume a transcript accession alone is sufficient for an intronic `c.` description. Current HGVS reference-sequence guidance requires genomic sequence context for intronic sequence when the intron is not contained in the transcript reference sequence.
- Do not assume a VCF representation can be converted to HGVS by changing punctuation or coordinates. Variant representation and HGVS nomenclature use different conventions and require sequence-aware normalization and mapping.
- Prefer three-letter amino-acid codes for protein descriptions.
- Do not put spaces inside an HGVS variant description.
- Use approved gene symbols when genes are named, but do not insert a gene symbol into an HGVS description as a substitute for the required reference sequence.
- Do not improvise syntax for complex or uncertain variants. Consult the current stable HGVS recommendation for the specific variant type.

## Required context

Before generating or validating an HGVS description, establish as applicable:

- species
- exact reference sequence identifier and version
- reference assembly when a genomic sequence is involved
- genomic allele and reference sequence used to derive it
- transcript accession and version for `c.` or `r.` descriptions
- protein accession and version when needed for an unambiguous `p.` description
- whether the transcript is MANE Select, MANE Plus Clinical, or another justified transcript
- molecular level being described
- whether RNA or protein consequences were experimentally observed or computationally predicted
- phase or allele configuration when multiple variants are being described together
- uncertainty in positions or consequences
- HGVS Nomenclature version when an auditable or reproducible report requires it

## AI behaviour

- Do not output a precise HGVS description when the reference sequence required to define it is unknown.
- Do not omit a reference-sequence version when the source database versions its sequences.
- Do not infer a transcript solely from a gene symbol. Determine the transcript used by the analysis or select an appropriate MANE transcript when the task requires a standard transcript and no study-specific transcript has been specified.
- Do not silently replace a supplied transcript with MANE. Preserve the transcript actually used by the source analysis and, when useful, provide a MANE-mapped description separately.
- When reporting a predicted protein consequence, use HGVS prediction notation rather than presenting the consequence as experimentally demonstrated.
- Keep genomic, coding-DNA, RNA, and protein descriptions distinct. A description at one level is not a substitute for evidence at another level.
- When multiple descriptions are useful, report the genomic description and the relevant transcript/protein description rather than returning only an isolated protein change.
- Before converting between VCF and HGVS, verify the reference sequence and allele, normalize using a sequence-aware method, and validate the resulting HGVS description.
- For deletions, duplications, insertions, delins, repeats, uncertain positions, complex alleles, mosaicism, chimerism, or structural events, consult the current stable HGVS recommendation for that variant class instead of extrapolating from simple substitutions.
- When exact nomenclature matters for publication, clinical reporting, or a database submission, validate the description with an HGVS-aware validator. Treat validator output as an implementation of the standard, not as a replacement for biological review.

## Common failure modes

### Reference omitted

```text
BRCA1:c.68_69del
```

A gene symbol does not uniquely define the reference sequence or numbering. A strict standalone HGVS description should identify the accessioned reference sequence used.

### Version omitted

```text
NM_004006:c.124A>T
```

If the sequence database uses versioned records, omitting the version leaves the reference sequence insufficiently specified.

### Genome build used as the HGVS reference

```text
GRCh38:chr17:43045700C>T
```

`GRCh38` identifies an assembly context, not the accessioned sequence required for a strict HGVS genomic description.

### Predicted consequence presented as observed

```text
p.Ser42Cys
```

If the protein consequence was inferred from sequence rather than demonstrated experimentally, prediction notation is required:

```text
p.(Ser42Cys)
```

### Transcript chosen silently

A variant may have different `c.` and `p.` consequences on different transcripts. Do not select a convenient transcript without identifying it.

### VCF normalization treated as HGVS normalization

Equivalent indels or repeat variants can be positioned differently under commonly used VCF normalization and the HGVS 3′ rule. Convert with sequence-aware tools rather than string manipulation.

## Authoritative standards

HGVS Nomenclature is the authority for sequence-variant nomenclature. Use its current stable recommendations rather than copying the complete syntax into Biology Skills.

The General recommendations define the cross-cutting rules. The Reference Sequences guidance defines acceptable reference sequences and identifiers. The Checklist captures frequent reporting errors. Variant-specific DNA, RNA, protein, uncertainty, allele, repeat, and complex-variant pages define exact syntax for those cases.

For human transcript selection, use MANE guidance from NCBI and Ensembl. MANE Select provides a standard transcript for clinical reporting and general display; MANE Plus Clinical provides additional transcripts where MANE Select alone is insufficient for reporting clinically important variants.

HGVS lists software that can assist with parsing, normalization, conversion, and validation, including Mutalyzer and VariantValidator. The HGVS software directory explicitly does not constitute endorsement of individual tools.

## Examples

### Genomic description

```text
NC_000023.11:g.32849790T>A
```

The accession and version identify the reference sequence; `g.` identifies genomic coordinates.

### Transcript-level description

```text
NM_004006.3:c.124A>T
```

The accession and version identify the coding transcript; `c.` uses coding-DNA numbering.

### Predicted protein consequence

```text
p.(Ser42Cys)
```

Parentheses indicate that the protein consequence is predicted rather than experimentally demonstrated. Where the protein reference is not otherwise unambiguous, preserve the relevant protein accession and version.

### Multi-level reporting

When useful, provide linked descriptions at more than one level rather than collapsing them into one label:

```text
genomic:    NC_000023.11:g.32849790T>A
transcript: NM_004006.3:c.124A>T
protein:    p.(Ser42Cys)
```

Each level answers a different question and must be interpreted relative to its reference sequence.

## Sources

- HGVS Nomenclature, stable home and current version: https://hgvs-nomenclature.org/stable/
- HGVS Nomenclature, stable General recommendations: https://hgvs-nomenclature.org/stable/recommendations/general/
- HGVS Nomenclature, Reference Sequences: https://hgvs-nomenclature.org/stable/background/refseq/
- HGVS Nomenclature, Checklist: https://hgvs-nomenclature.org/stable/recommendations/checklist/
- HGVS Nomenclature, Syntax Summary: https://hgvs-nomenclature.org/stable/recommendations/summary/
- HGVS Nomenclature, Software: https://hgvs-nomenclature.org/stable/software/
- NCBI MANE: https://www.ncbi.nlm.nih.gov/refseq/MANE/
- HGNC: https://www.genenames.org/
- den Dunnen et al. HGVS recommendations for the description of sequence variants: 2016 update. Human Mutation. https://doi.org/10.1002/humu.22981
- Hart et al. HGVS Nomenclature 2024: Improvements to community engagement, usability, and computability. Genome Medicine. https://doi.org/10.1186/s13073-024-01421-5
