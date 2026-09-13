---
id: genomics.sequencing-reads-and-quality
title: Sequencing reads and quality
domain: genomics
status: draft
---

# Sequencing reads and quality

## Summary

FASTQ represents sequencing reads together with per-base quality values. The sequence, read identifier, pairing information, quality encoding, and preprocessing history all affect downstream interpretation. Phred is a logarithmic scale that can be used for several different error probabilities, so the quantity being scored must always be identified.

## Core rules

- A FASTQ record contains a read identifier, sequence, separator, and quality string. In modern files this is usually written as four lines per read, although historical variants can wrap sequence and quality across multiple lines.
- After concatenating any wrapped lines, the number of quality characters must equal the number of sequence symbols.
- Modern sequencing data usually use Phred+33 quality encoding, but legacy FASTQ files can use incompatible historical encodings.
- A Phred score is defined by `Q = -10 log10(P_error)`. An increase of 10 corresponds to a tenfold decrease in the represented error probability.
- The word Phred describes a scale, not one universal measurement. Base quality, mapping quality, and genotype quality can all be Phred-scaled while referring to different events.
- Base quality estimates uncertainty in a base call. It is not the same as read mapping confidence and should not be substituted for MAPQ.
- Paired-end reads are biological or library pairs established by read identifiers and pipeline conventions, not merely by filenames containing `R1` and `R2`.
- Adapter trimming, quality trimming, UMI or barcode processing, read filtering, and read merging can change the FASTQ content. Preserve preprocessing provenance when it affects analysis.

## Required context

Preserve as applicable:

- sequencing platform and run or sample identity
- read identifier convention
- single-end or paired-end design
- read orientation and pairing convention
- quality encoding
- whether reads were trimmed, filtered, merged, deduplicated, or otherwise transformed
- adapter, barcode, UMI, or index-read handling when relevant
- compression and file integrity information

When interpreting a Phred-scaled quantity, identify what probability or error event the score represents.

## AI behaviour

- Do not interpret a quality character until the encoding is established or safely inferred from a modern workflow with supporting metadata.
- Do not say that Q30 means 30 percent quality. Under the standard Phred definition it corresponds to an error probability of 0.001 for the scored event.
- Do not average or compare Phred scores as if they were linear percentages without considering the underlying probabilities and the intended statistic.
- Keep base quality, mapping quality, variant quality, and genotype quality separate.
- Do not infer paired-read relationships solely from filenames when identifiers or pipeline metadata disagree.
- Do not treat FASTQ as an immutable representation of instrument output when trimming or other preprocessing has occurred.

## Common failure modes

### Base quality confused with mapping quality

A high base quality means the base call is estimated to be reliable. It does not establish that the read was placed at the correct genomic locus.

### Legacy quality encoding ignored

The same ASCII character can encode different scores under historical FASTQ conventions. This matters when processing older datasets.

### Q score treated as perfectly calibrated probability

The Phred transformation defines the scale, but empirical calibration can depend on instrument, software, cycle, chemistry, and post-processing. A reported Q value should not automatically be treated as a universally calibrated probability.

### Paired files assumed to be paired records

Two files named `sample_R1.fastq.gz` and `sample_R2.fastq.gz` are expected to contain corresponding mates, but pairing should remain consistent at the record and pipeline level.

## Authoritative standards

FASTQ has evolved through community conventions rather than one single current normative specification. Use platform documentation and established format references for encoding details. Use the mathematical Phred definition for the score transformation and the relevant tool documentation for the event represented by a Phred-scaled field.

## Examples

### Phred interpretation

```text
Q20 -> P(error) = 0.01
Q30 -> P(error) = 0.001
Q40 -> P(error) = 0.0001
```

These values apply to the event whose error probability is being encoded. They do not make base quality, MAPQ, and genotype quality interchangeable.

### FASTQ record

```text
@READ_001
ACCTGATCGT
+
IIHGFEDCBA
```

The sequence and quality strings must correspond position by position under the encoding used by the file.

## Sources

- Cock PJ et al. The Sanger FASTQ file format for sequences with quality scores, and the Solexa/Illumina FASTQ variants: https://doi.org/10.1093/nar/gkp1137
- NCBI Sequence Read Archive: https://www.ncbi.nlm.nih.gov/sra/
- SAM/BAM specifications for base and mapping quality context: https://samtools.github.io/hts-specs/
