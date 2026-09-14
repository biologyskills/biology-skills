---
id: bioinformatics.qc-outputs-and-sample-identity
title: QC outputs and sample identity
domain: bioinformatics
status: draft
---

# QC outputs and sample identity

## Summary

Quality-control outputs should preserve stable biological and computational identity while remaining discoverable by downstream reporting and aggregation systems.

Biological samples, libraries, lanes, sequencing runs, processing stages, files, and report labels are related but distinct objects. Filenames can encode some of this information, but they should not be treated as authoritative biological identity unless the workflow explicitly defines them that way.

For instance, MultiQC is widely used to aggregate bioinformatics QC results. Compatibility is module-specific: supported tools can have different filename requirements, content signatures, supported commands, and sample-name derivation rules. Preserve native output conventions where possible and consult the current MultiQC module documentation before renaming or redesigning outputs.

## Core rules

- A biological sample identifier is not equivalent to a filename.
- Distinguish biological sample, library, lane or run, assay, processing stage, tool output, and report artifact when they represent different objects.
- File discovery and sample identification are separate operations.
- Do not assume that support for a tool means that every output produced by that tool is supported.
- Preserve native output naming and content conventions when an established downstream parser depends on them.
- Do not rename recognised outputs merely for cosmetic consistency if doing so can break automatic discovery.
- Ensure that distinct samples and processing states remain distinguishable after downstream filename cleaning or sample-name normalization.
- Do not assume the output filename determines the sample name. A parser may derive identity from file contents, an embedded input filename, directory context, or other metadata.
- Preserve processing-stage identity separately from biological sample identity.
- Prefer explicit structured data over loosely formatted human-readable logs when designing machine-consumable QC output.
- Keep source QC outputs and aggregated reports separate. Aggregation does not replace the underlying evidence or provenance.
- When exact compatibility matters, use the current documentation for the relevant producing tool and MultiQC module rather than a copied local list of filenames or search patterns.

## Identity model

When designing or interpreting QC output, distinguish at least four levels where relevant.

### Biological identity

The specimen or biological entity being studied.

Examples:

```text
patient_01
tumour_A
sample_143
````

### Data identity

A particular experimental or sequencing unit.

Examples:

```text
library_01
lane_2
run_2026_04
R1
```

### Processing identity

The computational state of the data.

Examples:

```text
raw
trimmed
aligned
deduplicated
recalibrated
```

### Artifact identity

The specific computational object.

Examples:

```text
FASTQ file
BAM file
alignment log
QC metrics table
MultiQC report
```

Do not collapse these dimensions merely to obtain unique filenames.

## Required context

For QC outputs intended for automated aggregation, preserve or establish as applicable:

* biological sample identifier
* library, lane, run, read, or assay identifier when distinct
* processing stage
* generating tool
* tool version when relevant
* command or subcommand
* output type
* source input identity
* relationship between filename and sample identifier
* whether the downstream parser identifies samples from filenames or contents
* expected downstream parser or reporting system
* transformation or renaming applied after tool execution
* configuration used by the aggregation system when it changes discovery or sample naming

## AI behaviour

* Before renaming a QC or log file, determine whether downstream discovery depends on its filename.
* Do not infer that changing a suffix or extension is harmless merely because the file contents are unchanged.
* Do not assume that a filename is the authoritative sample identifier.
* Do not impose one universal naming grammar across unrelated bioinformatics tools.
* When multiple files represent one biological sample at different processing stages, preserve the common sample identity and represent the processing stage separately.
* When a downstream tool cleans sample names, verify the resolved names for collisions rather than checking only whether the original filenames are unique.
* When MultiQC already supports a tool, use the corresponding current module documentation to determine supported output, search behaviour, and sample-name derivation.
* Do not assume that every output from a MultiQC-supported tool is parseable.
* For project-specific QC results without a dedicated MultiQC module, prefer documented MultiQC Custom Content conventions where appropriate.
* For a released reusable bioinformatics tool, prefer a proper MultiQC module or plugin when durable first-class integration is required.
* When sample counts in an aggregate report are lower than expected, inspect sample-name collisions and source-file discovery before concluding that source data are missing.
* Keep stable machine identifiers unchanged when possible. Treat human-readable display-name replacement as presentation unless the workflow explicitly defines a reversible mapping.
* Preserve the files and configuration needed to reproduce an aggregated QC report.

## MultiQC interoperability

MultiQC searches recursively for supported output files and delegates parsing to tool-specific modules.

There is no universal filename convention that guarantees MultiQC compatibility for every tool.

### Check support at the output level

Before designing or renaming output intended for MultiQC:

1. identify the producing tool,
2. identify the command or subcommand,
3. check whether MultiQC currently supports that tool,
4. open the corresponding MultiQC module documentation,
5. confirm that the specific output is supported,
6. determine how the module discovers the output,
7. determine how the module derives the sample name.

A statement such as:

```text
MultiQC supports samtools
```

does not imply:

```text
MultiQC can parse every samtools output.
```

Support can be limited to particular commands, outputs, filenames, versions, or content signatures.

### File discovery

MultiQC modules can search using filename patterns, content signatures, regular expressions, exclusions, or combinations of these.

Therefore:

```text
Can MultiQC discover this file?
```

and:

```text
Which sample will MultiQC assign this result to?
```

are different questions.

A file may be found by its filename while its sample name is extracted from its contents.

### Preserve native output conventions

When a supported tool already produces output recognised by MultiQC, preserve that convention unless the pipeline deliberately supplies matching custom configuration.

For example, the FastQC module recognises outputs such as:

```text
*_fastqc.zip
```

Renaming:

```text
SAMPLE01_fastqc.zip
```

to:

```text
SAMPLE01_qc.zip
```

can make the output undiscoverable by the default FastQC search pattern.

Do not rename recognised outputs solely to make filenames appear more uniform across a pipeline.

### Sample-name derivation

Do not assume that the basename of the report file becomes the sample name.

Different modules can derive sample identity from:

* the output filename
* the input filename recorded inside a log
* metadata inside the output
* directory or workflow context
* module-specific fields

For example, FastQC sample identity can be derived from the `Filename` field inside `fastqc_data.txt`.

This means that file naming and sample naming must be considered separately.

### Name cleaning and collisions

MultiQC can remove or transform common filename components when creating displayed sample names.

This is convenient, but two different input filenames can resolve to the same cleaned sample name.

Filename uniqueness is therefore not sufficient.

Check:

```text
original filename
        ↓
module-specific sample extraction
        ↓
MultiQC sample-name cleaning
        ↓
resolved sample identifier
```

Distinct samples, libraries, runs, or intentionally separate analyses must remain distinguishable at the final stage.

A lower-than-expected number of samples in a report can indicate name collisions rather than missing source files.

### Processing stages

Raw and processed data from one biological sample represent different computational states, not necessarily different biological samples.

Prefer the conceptual model:

```text
sample: SAMPLE01
stage: raw
```

and:

```text
sample: SAMPLE01
stage: trimmed
```

rather than redefining the biological sample as:

```text
SAMPLE01_raw
SAMPLE01_trimmed
```

solely to force report separation.

When the same module must be shown for multiple stages, use workflow structure, paths, module configuration, anchors, or other documented mechanisms to distinguish the analyses while preserving stable biological identity.

### Existing supported tools

If MultiQC already provides a module for the producing tool:

* preserve the native output expected by that module
* check which commands and report types are supported
* check whether filenames are significant
* check how sample names are obtained
* check whether version-specific behaviour is documented
* use current module documentation rather than assuming historical behaviour

Do not recreate an existing supported module using Custom Content merely to obtain a different filename convention.

### Custom project-specific QC

When an internal pipeline or project-specific script produces QC metrics and no dedicated MultiQC module exists, MultiQC Custom Content can provide a lightweight integration route.

MultiQC recognises custom-content files using documented `_mqc` naming conventions, including structured formats such as:

```text
coverage_qc_mqc.tsv
alignment_qc_mqc.csv
contamination_qc_mqc.json
sample_metrics_mqc.yaml
```

Prefer structured machine-readable output containing explicit sample identifiers and metric names.

Do not encode all sample and metric meaning solely in the filename.

For example, prefer:

```text
coverage_metrics_mqc.tsv
```

containing:

```text
sample_id    mean_coverage    pct_20x
SAMPLE01     37.2             0.984
SAMPLE02     31.9             0.971
```

over a collection of loosely formatted files such as:

```text
SAMPLE01_good_coverage_final.txt
SAMPLE02_good_coverage_final.txt
```

### Released reusable tools

For a generally released bioinformatics tool that should integrate durably with MultiQC, a proper MultiQC module or plugin is preferable to treating project-specific Custom Content as the permanent interface.

A maintained module can explicitly define:

* supported commands
* expected outputs
* file-search patterns
* parsing behaviour
* sample-name derivation
* configuration
* tests

## Common failure modes

### Renaming a recognised output

Changing:

```text
SAMPLE01_fastqc.zip
```

to:

```text
SAMPLE01_qc.zip
```

can break default MultiQC discovery even though the contents have not changed.

### Tool support treated as universal output support

A pipeline sees that MultiQC supports a tool and assumes that an arbitrary log from that tool will be parsed.

Support must be checked for the actual command and output.

### Filename treated as biological identity

A file called:

```text
patient01_L002_R1_trimmed.fastq.gz
```

contains information about sample, lane, read orientation, and processing stage.

The entire basename should not automatically become the biological sample identifier.

### Generic log filename treated as the sample

A file called:

```text
tool.log
```

does not establish that the biological sample is named `tool`.

The parser may obtain sample identity from the contents of the file.

### Collision after name cleaning

Two distinct source filenames can resolve to the same cleaned sample name.

One result can then overwrite or obscure another in the aggregate report.

Reason about the resolved sample identifiers, not only the source filenames.

### Processing stage confused with biological sample

Raw and trimmed reads from the same specimen are different processing states.

Changing the sample identifier merely to represent workflow stage weakens traceability between the outputs and the underlying biological sample.

### Custom human-readable output

A new in-house script produces:

```text
qc_results.txt
```

containing prose and visually aligned values.

This may be convenient for a human but unnecessarily difficult for automated aggregation.

Prefer explicit structured output when downstream machine consumption is intended.

### Aggregate report treated as source evidence

A `multiqc_report.html` summarises parsed source outputs.

It does not replace those source files, their tool versions, workflow configuration, or provenance.

## Authoritative standards

Use the current MultiQC documentation for exact file-search behaviour, supported modules, configuration options, sample-name cleaning, and Custom Content conventions.

Biology Skills should not maintain a static copy of the complete supported-tool list or every module-specific search pattern because these can change between MultiQC releases.

When compatibility matters:

1. consult the current Supported Tools catalogue,
2. open the relevant module page,
3. confirm the specific output is supported,
4. inspect the producing tool's own documentation where necessary.

Use the producing tool's documentation as the authority for the meaning of its native outputs. Use MultiQC documentation as the authority for how those outputs are currently discovered and aggregated by MultiQC.

## Examples

### Stable identity across workflow stages

Prefer:

```text
sample: SAMPLE01
stage: raw
tool: fastqc
```

and:

```text
sample: SAMPLE01
stage: trimmed
tool: fastqc
```

The sample remains stable while the processing state changes.

### Existing supported output

If the producing tool already emits output expected by its MultiQC module, preserve that native output rather than inventing a project-wide replacement filename.

### Custom QC summary

For project-specific QC:

```text
coverage_qc_mqc.tsv
```

with explicit sample identifiers and metric columns is preferable to:

```text
SAMPLE01_good_results_final.txt
```

whose identity and semantics must be inferred from the filename.

### MultiQC compatibility check

Before generating output for an established tool:

```text
producing tool
      ↓
command / subcommand
      ↓
current MultiQC supported-tool catalogue
      ↓
specific MultiQC module
      ↓
supported output?
      ↓
file-discovery rule
      ↓
sample-name derivation
      ↓
collision check
```

## Sources

* MultiQC configuration:
  https://docs.seqera.io/multiqc/getting_started/config
* MultiQC supported tools and modules:
  https://docs.seqera.io/multiqc/modules/
* MultiQC configuration schema:
  https://docs.seqera.io/multiqc/config_schema
* MultiQC Custom Content:
  https://docs.seqera.io/multiqc/custom_content
* MultiQC module development:
  https://docs.seqera.io/multiqc/development/modules/
* MultiQC pipeline integration:
  https://docs.seqera.io/multiqc/usage/pipelines
* MultiQC troubleshooting and provenance:
  https://docs.seqera.io/multiqc/usage/troubleshooting
* MultiQC FastQC module:
  https://docs.seqera.io/multiqc/modules/fastqc
* MultiQC samtools module:
  https://docs.seqera.io/multiqc/modules/samtools


