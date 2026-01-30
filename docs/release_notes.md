# Release notes

## 1.0.0 - 31 January 2026

First public release of the Netflix reviews analysis.

### Analysis

- Full pipeline over 113,068 Netflix app store reviews.
- Text cleaning with lower casing, punctuation removal and digit removal.
- Sentiment scoring with `TextBlob` and a three way label derived from the
  polarity thresholds of -0.1 and 0.1.
- Score distribution and sentiment crosstab visualisations.
- Word cloud over the negative reviews with an extended stopword list.
- LDA topic model with five topics over the negative review corpus.
- Interactive topic visualisation with `pyLDAvis`.

### Engineering

- `netflix.ipynb` is the reference implementation and stores its outputs.
- `scripts/` mirrors the notebook for terminal and continuous integration use.
- `tests/` covers the shared helpers with unit tests.
- Continuous integration runs the tests and validates the notebook structure.
- Documentation in `docs/` covers the dataset, the methodology, the findings,
  the complaint themes, the limitations and the reproducibility steps.
