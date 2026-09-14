---
id: experimental-design.experimental-unit-replication-and-pseudoreplication
title: Experimental unit, replication and pseudoreplication
domain: experimental-design
status: draft
---

# Experimental unit, replication and pseudoreplication

## Summary

The number of measured observations is not necessarily the number of independent experimental units.

Cells from one donor, technical wells from one culture, reads from one sequencing library, repeated images from one animal, and repeated time points from one participant can provide many measurements while sharing the same biological or experimental source. Treating such measurements as independent replication can underestimate variability and overstate evidence.

## Core rules

- Identify the unit independently assigned to or exposed to the condition of interest.
- Distinguish the experimental unit from the observation or measurement unit.
- Distinguish independent biological replication from technical replication.
- Treat repeated measurements from the same experimental unit as dependent unless the design justifies otherwise.
- Treat subsamples from one experimental unit as subsamples rather than new independent units.
- Do not infer sample size from row count.
- Preserve nesting such as subject -> specimen -> aliquot -> library -> lane -> measurement when relevant.
- If treatment is assigned at a cluster level, the cluster can be the experimental unit even when many members are measured.
- Technical replication can improve precision about a measurement process without increasing the number of independent biological units.
- Pooling can change the unit represented by a measurement and can remove information about between-unit variability.
- The statistical model should represent material clustering, repeated measures, or hierarchical structure rather than pretending that observations are exchangeable.
- Report `n` with the entity it counts.

## Required context

Establish where relevant:

- independent sampling unit
- unit of treatment or exposure assignment
- biological source
- number of independent biological units
- number of technical replicates
- number of subsamples per unit
- repeated-measure structure
- nested or clustered structure
- pooling
- randomisation level
- batch or block structure
- analytical model used for dependence

## AI behaviour

Before reporting a sample size:

1. ask what was independently sampled or assigned,
2. identify repeated, nested, technical, or subsampled observations,
3. report biological and technical counts separately when useful,
4. avoid calling measurements independent when they share the same experimental unit.

Do not transform:

```text
3 donors
100 cells per donor
```

into:

```text
n = 300 independent biological replicates
```

unless the experimental question and design genuinely make individual cells the independently assigned units.

When the design is ambiguous, describe the hierarchy and state that the effective independent sample size cannot be inferred from measurement count alone.

## Common failure modes

### Cells mistaken for donors

```text
3 donors
100 cells measured from each donor
300 cells total
```

The 300 cells can support cell-level modelling, but they do not automatically provide 300 independent donor-level biological replicates.

### Technical wells mistaken for biological replication

Multiple wells from the same preparation can estimate technical variation. They do not create new independent biological specimens.

### Sequencing lanes counted as biological samples

Sequencing the same library across several lanes can improve data quantity and reveal lane-specific QC issues. It does not increase the number of biological individuals.

### Repeated time points treated as independent people

Measurements from the same participant over time are correlated and should retain participant identity and temporal structure.

## Authoritative standards

Use reporting and design standards appropriate to the experimental system. ARRIVE 2.0 provides an explicit experimental-unit concept and distinguishes experimental units from repeated or subsampled observations in animal research. The same reasoning generalises to other biological systems.

Biology Skills does not prescribe one statistical model; it requires the dependence structure to be recognised before analysis.

## Examples

### Donor and cell hierarchy

```text
donor_1 -> 100 cells
donor_2 -> 100 cells
donor_3 -> 100 cells
```

Possible counts:

```text
biological donors = 3
observed cells = 300
```

Which count defines independent `n` depends on the intervention and estimand.

## Sources

- ARRIVE Guidelines 2.0: https://arriveguidelines.org/
- ARRIVE study design and experimental unit guidance: https://arriveguidelines.org/arrive-guidelines/study-design/1b/explanation
- ARRIVE sample-size guidance: https://arriveguidelines.org/arrive-guidelines/sample-size/2a/explanation
- Percie du Sert N et al. The ARRIVE guidelines 2.0: https://doi.org/10.1371/journal.pbio.3000410
