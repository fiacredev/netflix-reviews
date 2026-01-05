# Dataset profile

Statistics recorded for `netflix_reviews.csv` on 5 January 2026.

## Volume

| Metric | Value |
| --- | --- |
| Reviews | 113,068 |
| Columns | 8 |
| Unique reviewers | 80,013 |
| Total thumbs up | 1,185,386 |
| Highest thumbs up on a single review | 8,032 |
| Date range | 2018-09-12 to 2024-06-14 |

## Ratings

| Score | Reviews | Share |
| --- | --- | --- |
| 1 | 44,343 | 39.2% |
| 2 | 10,762 | 9.5% |
| 3 | 11,933 | 10.5% |
| 4 | 13,853 | 12.2% |
| 5 | 32,177 | 28.4% |

## Data quality

- `content` is missing on two rows and `userName` on one row.
- `reviewCreatedVersion` and `appVersion` are missing on 16,491 rows, which are
  the oldest reviews in the collection.
- 30.8% of the reviews have an empty body after cleaning, mostly one word
  reviews that carry a rating but no explanation.
- No duplicate `reviewId` values are present.

## Handling decisions

- Missing values are filled with an empty string.
- The `at` column is parsed into a pandas datetime.
- Only `content_c`, `score`, `reviewId` and `at` are kept for the analysis,
  which reduces the working set from eight columns to four.
