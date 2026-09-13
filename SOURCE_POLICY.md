# Source policy

Biology Skills encodes biological correctness for AI systems. It should explain what an agent must preserve, distinguish, check, or avoid while relying on authoritative external resources for formal standards that already have a recognised owner.

## Describe locally

Explain:

- biological concepts required for correct reasoning
- minimum context required for a valid interpretation
- distinctions that software interfaces commonly collapse
- failure modes that produce biologically incorrect or incomplete output
- operational behaviour expected from an AI agent
- interpretation boundaries and uncertainty

Keep these explanations concise enough to load into an AI context without unnecessary background prose.

## Cite rather than reimplement

Do not create local substitutes for maintained standards when exact syntax, terminology, identifiers, or normative definitions belong to an external authority.

Examples include:

- HGVS variant nomenclature
- VCF specifications
- GA4GH standards
- NCBI assembly and sequence accessions
- HGNC gene nomenclature
- MANE transcript definitions
- ontology specifications
- assay-specific community standards

A Biology Skills topic can explain when and why one of these standards is required, how mistakes arise, and what information must be retained. Exact normative rules should point to the current authoritative source.

## Source hierarchy

Prefer, where applicable:

1. normative international or community standard
2. official specification or database documentation
3. professional or expert consensus guideline
4. primary literature establishing the relevant result
5. high-quality review for background or synthesis

Secondary educational material should not be the sole source for a rule when an authoritative primary source exists.

## Stable biology versus moving standards

Separate stable biological claims from version-sensitive implementation details.

Example:

- stable claim: a transcript-dependent coding consequence depends on the transcript used
- moving standard: the current syntax rules used to represent that consequence in HGVS notation

The first belongs directly in Biology Skills. The second should point to HGVS unless a specific compatibility requirement must be documented.

## Sources in topics

Every substantive reference topic must contain a `Sources` section. Use direct links to authoritative resources where practical and publication identifiers for literature.

A citation must support the rule or distinction being made. Do not add sources merely to make a topic appear authoritative.
