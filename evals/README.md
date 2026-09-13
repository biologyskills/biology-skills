# Evaluations

Evaluations describe biological behaviours that a skill should change or preserve. They are intentionally vendor-neutral.

Each JSONL record contains:

- `id`: stable evaluation identifier
- `skill`: skill under evaluation
- `prompt`: test prompt
- `must_do`: behaviours required for a pass
- `must_not_do`: behaviours that constitute a failure

The initial repository stores the evaluation specification, not vendor-specific model scores. Automated runners can be added without changing the scientific meaning of the tests.
