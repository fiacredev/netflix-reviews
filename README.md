# Netflix Reviews Analysis

An exploratory analysis of Netflix mobile application reviews covering data
cleaning, sentiment scoring and topic modelling.

The project studies 113,068 reviews collected from the Google Play Store
between September 2018 and June 2024 and answers three questions: how do
ratings distribute, what language do unhappy customers use, and which product
themes dominate the complaints.

## Status

The analysis notebook and the helper scripts are complete. The documentation
is being finalised.

## Layout

- `netflix.ipynb` - the analysis notebook.
- `netflix_reviews.csv` - the raw review dataset.
- `scripts/` - helper scripts that mirror the notebook.
- `docs/` - written documentation for the analysis.

## Key findings

| Metric | Value |
| --- | --- |
| Reviews | 113,068 |
| Unique reviewers | 80,013 |
| Date range | 2018-09-12 to 2024-06-14 |
| Single star reviews | 44,343 (39.2%) |
| Five star reviews | 32,177 (28.4%) |
| Positive sentiment | 58,436 (51.7%) |
| Neutral sentiment | 35,126 (31.1%) |
| Negative sentiment | 19,506 (17.2%) |

The rating distribution is bimodal and the detected sentiment tracks the
rating closely: 85.9% of the five star reviews are positive, while three
quarters of the single star reviews are negative or neutral.
