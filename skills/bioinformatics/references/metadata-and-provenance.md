---
id: bioinformatics.metadata-and-provenance
title: Metadata and provenance
domain: bioinformatics
status: draft
---

# Metadata and provenance

## Summary

Biological data are not self-describing.

A sequence file, alignment, expression matrix, image, QC result, or derived analysis can remain computationally readable while becoming scientifically ambiguous if the metadata describing its biological source, experimental generation, or computational history are lost.

Preserve enough metadata to determine:

1. what biological material the data represent,
2. how that material was prepared and measured,
3. which experimental execution generated the data,
4. which files were produced,
5. which processes transformed those files,
6. which references, software, configurations, and QC measurements affect interpretation.

Metadata should remain connected to the entity or process they describe. Do not treat provenance as one flat collection of attributes attached to a final file.

## Core rules

- Treat scientifically material metadata as part of the data, not optional administrative decoration.
- Distinguish subject, specimen or sample, extract, library, assay, instrument, run, lane, file, analysis, and derived result when they represent different entities.
- Attach metadata to the entity or process it actually describes.
- Preserve lineage from derived data back to the source biological material and relevant processing steps.
- Do not assume one-to-one relationships between subject, sample, library, run, lane, file, or analysis.
- Distinguish intended, requested, or planned values from observed or measured values.
- Distinguish an assay from the instrument used to perform it and from the specific run in which it was executed.
- Distinguish a library from the process or kit used to prepare that library.
- Do not use a filename or filesystem path as the sole identity of an important scientific data object.
- Preserve content checksums or digests when file identity or transfer integrity matters.
- Attach QC metrics to the entity, process, unit, and calculation context they describe.
- Preserve software, workflow, reference-resource, and configuration versions when changes can alter the result.
- Do not infer missing experimental metadata from filenames, institutional habits, common protocols, or what would normally be expected.
- Distinguish unknown, unavailable, not measured, not provided, and not applicable when those states have different scientific meanings.
- Preserve scientific traceability without unnecessarily propagating directly identifying personal information.

## Metadata lineage

A useful conceptual model is:

```text
BIOLOGICAL SOURCE

subject
  ↓
specimen / sample

EXPERIMENT

sample
  ↓ sample preparation
extract / library
  ↓ assay
instrument + run + lane
  ↓
raw data files

COMPUTATION

raw data
  ↓ processing / analysis
derived data

QUALITY

QC metric
  ↓
explicitly associated with the sample, library,
run, file, assay, or analysis it describes
````

Not every workflow contains every level.

Preserve a level whenever losing it could change scientific interpretation, prevent troubleshooting, obscure technical variation, or make provenance impossible to reconstruct.

## Required context

### Biological source

Preserve as applicable:

* subject or organism identifier
* specimen or sample identifier
* identifier namespace
* sample type
* tissue, cell type, isolate, or other biological source
* collection time point
* clinically or experimentally relevant sample role
* relationships to other samples or subjects

A subject identifier and a specimen identifier are not interchangeable.

One subject can contribute multiple samples, tissues, time points, or biological states.

### Sample preparation and library

Preserve as applicable:

* source sample
* extract identifier
* library identifier
* preparation method
* preparation kit
* enrichment method
* barcode or index
* relevant batch information

A library is an entity produced by preparation.

The library-preparation method is the process used to create it.

Do not collapse these into one concept.

### Assay

Preserve as applicable:

* assay type
* assay identifier
* intended measurement
* intended read length
* intended depth or other planned target
* protocol or standard operating procedure

An assay describes what measurement is being performed.

It is not the same as the instrument or the individual run.

### Instrument and sequencing unit

Preserve as applicable:

* instrument or platform
* run identifier
* run date or time
* flow cell
* lane
* read group
* observed read count
* observed read length
* observed insert size
* other run-level measurements

Technical subdivision can remain important after files are merged.

Do not discard lane, run, or read-group provenance merely because downstream analysis operates on a combined file.

### Data files

For important scientific files, preserve as applicable:

* stable identifier
* file role
* format
* location
* size
* checksum or content digest
* source process
* relationship to upstream and downstream files

A path identifies a location, not necessarily the scientific object itself.

A file can move without changing its content, and a path can remain unchanged while its content is replaced.

### Computational analysis

Preserve as applicable:

* input files
* output files
* analysis identifier
* software and version
* workflow and version
* parameters or configuration
* reference resources
* annotation or database release
* execution time when relevant

The name of a software package alone is usually insufficient to reproduce a complete analysis.

### Quality control

A QC value requires scope.

For example:

```text
Q30 = 91.4%
```

is incomplete if it is unclear whether it describes:

```text
a lane
a sequencing run
a library
a sample
a merged FASTQ
or another processing unit
```

Likewise:

```text
mean coverage = 34.9×
```

may depend on what genomic regions, filters, reference sequence, and calculation method were used.

Preserve where relevant:

* metric name
* value
* unit
* entity or process measured
* calculation scope
* method or software
* timestamp or review state

## Planned versus observed values

Do not collapse experimental intent into experimental outcome.

For example:

```text
requested coverage: 30×
observed mean coverage: 22×
```

must not become:

```text
sequencing coverage: 30×
```

Similarly:

```text
intended read length: 150 bp
```

does not establish that every observed read was 150 bases long.

Use explicit semantics such as:

```text
intended
requested
target
observed
measured
delivered
```

when those distinctions matter.

## Cardinality

Do not assume:

```text
one sample
→ one library
→ one run
→ one lane
→ one file
```

Real workflows can contain:

```text
subject
├── sample A
└── sample B

sample A
├── library 1
└── library 2

library 1
├── lane 1
└── lane 2
```

Several sequencing units may later be merged:

```text
lane 1 → FASTQ A ─┐
                  ├→ merged FASTQ
lane 2 → FASTQ B ─┘
```

The merged file represents the combined data, but its provenance should still permit recovery of both contributing sequencing units when that information is scientifically relevant.

## AI behaviour

* Before interpreting a biological data object, determine what biological entity it represents.
* Identify whether metadata describe the subject, sample, library, assay, instrument, run, file, analysis, or QC process.
* Do not move metadata between these levels merely because doing so produces a simpler table or schema.
* Before combining files, determine whether lower-level provenance such as lane, run, library, or batch must remain recoverable.
* Before reporting a quantitative property, determine whether it is intended, requested, observed, calculated, or delivered.
* Do not infer an instrument, lane, reference sequence, assay, sample type, or protocol because it is common for the laboratory or project.
* When metadata are missing, recover them from an authoritative source when possible or preserve them as unknown.
* When data are transformed, maintain links to the input objects and processing step that generated the output.
* Preserve exact external reference identities when changing the reference could change the result.
* Use explicit values and units rather than relying on humans to infer them from strings where ambiguity is possible.
* Use maintained identifiers, controlled vocabularies, and metadata standards where appropriate rather than inventing incompatible local meanings.
* Keep stable machine identifiers separate from human-readable labels.

## Common failure modes

### Subject treated as sample

A record says:

```text
subject: SUBJ001
```

and the same identifier is used for every file.

But the subject contributed:

```text
blood
fibroblasts
tumour tissue
```

These are different biological samples and may support different interpretations.

Preserve the subject-to-sample relationship explicitly.

### Assay, instrument, and run collapsed

These describe different things:

```text
assay: whole-genome sequencing
instrument: Illumina NovaSeq 6000
run: RUN001
```

`whole-genome sequencing` is not an instrument.

`NovaSeq 6000` is not a sequencing run.

`RUN001` is not the assay definition.

### Library confused with library preparation

```text
library_id: LIB001
```

identifies a prepared library.

```text
library_preparation: PCR-free genomic DNA
```

describes how that library was produced.

They are not interchangeable.

### Lane provenance lost after merging

```text
SAMPLE01_L001_R1.fastq.gz
SAMPLE01_L002_R1.fastq.gz
```

are merged into:

```text
SAMPLE01_R1.fastq.gz
```

The merged file is valid, but discarding the fact that it came from lanes L001 and L002 can prevent lane-specific QC, troubleshooting, batch assessment, or read-group reconstruction.

### Planned value reported as measurement

```text
requested depth: 30×
```

does not imply:

```text
observed depth: 30×
```

The first describes intent.

The second requires measurement.

### Path treated as file identity

A file moves from:

```text
/archive/run1/sample.fastq.gz
```

to:

```text
/vault/projectA/sample.fastq.gz
```

The location changed but the content may be identical.

Conversely, an overwritten file may keep the same path while becoming different data.

Preserve content identity separately from location when this matters.

### QC metric without scope

```text
Q30 = 91%
```

is stored without saying whether it describes a lane, run, library, or merged dataset.

The number survives, but its scientific meaning becomes ambiguous.

### Missing metadata silently inferred

The sequencing centre commonly uses one instrument, so an absent instrument field is automatically filled with that model.

This converts expectation into false provenance.

Unknown metadata must remain unknown unless recovered from an authoritative source.

## Examples

### Example 1: whole-genome sequencing lineage

```text
Subject SUBJ001
   ↓
Fibroblast sample SMP001
   ↓
Library LIB001
   ↓
Whole-genome sequencing assay
   ├── intended depth: 30×
   └── intended read length: 150 bp
         ↓
Instrument: NovaSeq 6000
Sequencing run RUN001
   ├── observed mean depth: 34.9×
   ├── average read length: 150 bp
   └── Q30: 91.4%
         ↓
FASTQ
   ├── file identifier
   └── checksum
         ↓
Variant analysis
   ├── software + version
   ├── workflow/configuration
   └── reference sequence
         ↓
VCF
   └── checksum
```

Each value belongs to a particular biological entity, experimental process, data object, or computational process.

### Example 2: one library sequenced across two lanes

```text
Sample SMP001
   ↓
Library LIB001
   ├── RUN001 / lane 1 → FASTQ A
   └── RUN001 / lane 2 → FASTQ B
                           ↓
                        merged FASTQ
```

The merged file may be the object used for downstream analysis.

The lane-level provenance should remain recoverable when it is needed to understand technical variation or reconstruct processing.

### Example 3: intended and observed sequencing depth

```text
assay target:
  requested depth = 30×

run result:
  observed mean depth = 22×
```

An AI should report both values with their meanings intact.

It should not summarize them as:

```text
sequencing depth = 30×
```

### Example 4: raw-to-derived data lineage

```text
FASTQ
  ↓ alignment
BAM
  ↓ variant calling
VCF
```

The VCF should remain traceable to the source alignment and, through it, to the upstream sequencing data and biological sample.

Relevant processing metadata such as software versions, workflow configuration, and reference resources should remain recoverable.

## Authoritative standards

Biology Skills defines the distinctions that computational systems should preserve. It does not prescribe one storage format, database structure, or serialization.

Use maintained domain metadata models, repository requirements, controlled vocabularies, and interoperability standards where appropriate.

The exact metadata required depends on the assay, biological domain, downstream use, and regulatory or repository context.

When a maintained standard defines the current representation of a concept, use that standard rather than copying its complete definition into Biology Skills.

## Sources

* van der Horst E et al. *Bridging Clinical and Genomic Knowledge: An Extension of the SPHN RDF Schema for Seamless Integration and FAIRification of Omics Data.*
  https://www.preprints.org/manuscript/202312.0373
* Wilkinson MD et al. *The FAIR Guiding Principles for scientific data management and stewardship.*
  https://doi.org/10.1038/sdata.2016.18
* FAIR Genomes metadata schema:
  https://fairgenomes.org/
* EDAM Ontology:
  https://edamontology.org/
* Ontology for Biomedical Investigations:
  https://obi-ontology.org/

