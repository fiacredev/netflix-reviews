# Reproducibility

## Environment

```bash
python -m venv .venv
source .venv/bin/activate
make setup
```

The exact versions used for the recorded results are pinned in
`requirements.txt`. A conda alternative is provided in `environment.yml`.

## Data

The dataset `netflix_reviews.csv` is versioned in the repository, so a clone
already contains the input of the analysis. The file is never modified: all
cleaning happens in memory inside the notebook.

## Determinism

- No sampling is used anywhere in the pipeline.
- The LDA model accepts a fixed random seed, exposed as `RANDOM_SEED` in
  `scripts/config.py`.
- The notebook stores its outputs, so the committed file shows the exact
  results that were produced.

## Verification

```bash
python -m unittest discover -s tests -v
python scripts/inspect_dataset.py
python scripts/sentiment_summary.py
```

The continuous integration workflow in `.github/workflows/notebook-ci.yml`
runs the unit tests and validates the structure of the notebook on every push.

## Hardware notes

The full pipeline processes 113,068 reviews. The topic modelling step is the
most expensive one and takes a few minutes on a modern laptop. Running the
scripts with `--topics` and `--passes` allows a quicker, smaller model while
iterating.
