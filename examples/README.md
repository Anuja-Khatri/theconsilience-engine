# Examples

Worked examples anyone can run.

## Determinism demo


```bash
cd determinism-demo
python run_demo.py
```

It grades one input twice in one process and compares the two hashes. It exercises the grading ladder only; the test suite in `../tests/` covers the rest of `judge/`.

Rejection and grading examples are not yet in this directory.
