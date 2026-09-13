# Contributing

Contributions are welcome from biology, medicine, bioinformatics, statistics, computer science, and AI communities.

## Before opening a pull request

1. Read [`STYLE_GUIDE.md`](STYLE_GUIDE.md).
2. Read [`SOURCE_POLICY.md`](SOURCE_POLICY.md).
3. Keep the change focused on one biological concept where possible.
4. Prefer authoritative sources over secondary summaries.
5. Add or update an evaluation when the change affects expected AI behaviour.
6. Run the checks locally.

```bash
python scripts/validate.py
python scripts/export.py
python -m unittest discover -s tests
```

## Add a reference topic

Copy [`TOPIC_TEMPLATE.md`](TOPIC_TEMPLATE.md) into the relevant `skills/<domain>/references/` directory.

Use a stable identifier such as:

```text
genomics.reference-genomes
```

New topics start as `draft`.

## Add a domain skill

A new top-level domain should be broad enough to trigger reliably and substantial enough to justify its own context. Avoid making every concept a separate skill.

A domain requires:

- `skills/<domain>/SKILL.md`
- coherent reference topics
- a clear description of when the skill should activate
- at least one behaviour evaluation

## Pull request checklist

- [ ] Biological claims are precise.
- [ ] Required context is explicit.
- [ ] Formal standards are cited rather than reimplemented.
- [ ] Sources directly support the claims made.
- [ ] Examples do not introduce unsupported assumptions.
- [ ] Review status is accurate.
- [ ] An evaluation was added or updated when behaviour changed.
- [ ] Validation and tests pass.
