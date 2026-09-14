---
name: bioinformatics
description: Apply computational correctness rules for biological data as they move between files, tools, workflows, evidence systems, and reports. Use when biological identity, metadata, provenance, input/output conventions, file discovery, evidence availability, interoperability, or computational transformations can change the meaning or traceability of a result.
---

# Bioinformatics

Use this skill when biological data or results pass between computational files, tools, workflow stages, evidence systems, or reporting systems.

Bioinformatics should preserve four things across these boundaries:

1. **identity** — what biological or computational object is represented,
2. **lineage** — where it came from and what produced it,
3. **semantics** — what the data, file, field, or evidence value means,
4. **interoperability** — whether the next system can interpret it correctly.

## Core rules

- Preserve biological identity separately from subject, specimen, library, lane, run, file, processing stage, and derived result when these represent distinct entities.
- Do not infer biological identity solely from filenames, directory names, or naming conventions when authoritative metadata exist elsewhere.
- Preserve lineage from derived results back to their relevant biological source, experimental inputs, computational inputs, and transformations.
- Attach metadata to the entity or process it actually describes. Do not flatten sample-, assay-, run-, file-, analysis-, and QC-level properties into one ambiguous record.
- Do not assume one-to-one relationships between subjects, samples, libraries, runs, lanes, files, or analyses.
- Treat filenames, paths, extensions, directory structures, and output conventions as computational interfaces when downstream systems depend on them.
- Do not rename, reformat, merge, split, or relocate data without considering whether identity, discovery, parsing, provenance, or downstream interpretation depends on the original representation.
- Distinguish file location from file identity. Preserve checksums or content digests when exact file identity or transfer integrity matters.
- Distinguish planned, requested, or intended values from observed, measured, or delivered values.
- Preserve software, workflow, configuration, reference-resource, and database versions when changes can alter the result.
- Keep stable machine identifiers separate from human-readable display labels.
- Preserve units, scopes, and calculation contexts for quantitative values when they are required for unambiguous interpretation.
- Distinguish support for a software tool from support for a particular command, output type, version, file representation, or parser.
- Prefer established interoperable conventions over project-specific alternatives when a maintained ecosystem interface or standard already exists.
- Separate evidence availability from evidence interpretation, statistical support, pathogenicity, causality, ranking, and downstream decisions.
- Preserve explicit rule semantics, stable rule identifiers, versions, raw outcomes, and provenance when rule-based evidence is exchanged between systems.
- Do not treat missing, unavailable, or unevaluable information as though it were successfully established evidence.
- Treat aggregate reports, binary evidence matrices, summaries, and other reduced representations as derived outputs rather than replacements for their source information.
- When exact semantics or compatibility matter, consult the current maintained specification for the producing and consuming systems.

## AI behaviour

Before designing, changing, combining, or interpreting a computational biological object, establish:

1. what biological entity or process it represents,
2. what computational object is being handled,
3. what produced it,
4. which processing stage it belongs to,
5. what downstream system will consume it,
6. how identity is established,
7. which provenance must remain recoverable,
8. which conventions or standards govern its interpretation.

Do not invent a universal naming convention across unrelated bioinformatics tools.

Before renaming or restructuring an established tool output, determine whether downstream discovery or parsing depends on its filename, path, contents, or directory structure.

Do not assume that a filename used to discover a file is also the authoritative sample identifier.

When data are transformed or combined, preserve links to the source objects and retain lower-level provenance when it can affect interpretation, QC, troubleshooting, or reproducibility.

When quantitative metadata are reported, establish what entity they describe, their units, and whether they represent intended or observed values.

When metadata are missing, recover them from an authoritative source where possible. Otherwise preserve the missing state rather than inferring what is common for the laboratory, platform, or workflow.

When working with rule-based evidence, preserve the distinction between:

- the evidence rule,
- the raw evaluation result,
- any reduced interoperable representation,
- any downstream statistical or biological interpretation.

Do not convert evidence availability directly into pathogenicity, causality, diagnostic probability, or another stronger claim.

## References

Read the relevant reference when the task depends on it:

- [`references/qc-outputs-and-sample-identity.md`](references/qc-outputs-and-sample-identity.md) for QC output discovery, sample naming, processing-stage identity, MultiQC compatibility, supported outputs, custom QC content, and aggregation provenance
- [`references/metadata-and-provenance.md`](references/metadata-and-provenance.md) for biological sample lineage, experimental and computational provenance, metadata propagation, identifier scope, file identity, and traceability of derived data
- [`references/qualifying-evidence.md`](references/qualifying-evidence.md) for verifiable rule-based evidence, evidence availability, raw rule outcomes, QEM semantics, versioned rule sets, and separation of qualifying evidence from downstream interpretation or inference

