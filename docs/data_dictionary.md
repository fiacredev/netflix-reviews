# Data dictionary

The source dataset `netflix_reviews.csv` contains one row per Google Play
Store review of the Netflix mobile application. It holds 113,068 rows and
8 columns.

| Column | Type | Description |
| --- | --- | --- |
| `reviewId` | string | UUID that uniquely identifies the review. |
| `userName` | string | Display name of the reviewer. Unique for 80,013 accounts. |
| `content` | string | Free text body of the review. Two rows are empty. |
| `score` | integer | Star rating from 1 to 5. |
| `thumbsUpCount` | integer | Number of other users that marked the review as helpful. |
| `reviewCreatedVersion` | string | Version of the app in use when the review was written. Missing on 16,491 rows. |
| `at` | datetime | Timestamp of the review. Ranges from 2018-09-12 to 2024-06-14. |
| `appVersion` | string | Application version reported by the device. Missing on 16,491 rows. |

## Score distribution

| Score | Reviews | Share |
| --- | --- | --- |
| 1 | 44,343 | 39.2% |
| 2 | 10,762 | 9.5% |
| 3 | 11,933 | 10.5% |
| 4 | 13,853 | 12.2% |
| 5 | 32,177 | 28.4% |

The distribution is strongly bimodal. More than one third of all reviews are
single star complaints, while the two extremes together account for roughly
68% of the dataset.

## Missing values

| Column | Missing | Notes |
| --- | --- | --- |
| `userName` | 1 | Single anonymised account. |
| `content` | 2 | Reviews without a text body. |
| `reviewCreatedVersion` | 16,491 | Older reviews predate the field. |
| `appVersion` | 16,491 | Same rows as above. |

Missing values are replaced with an empty string before the text pipeline runs,
which keeps the sentiment and tokenisation steps free of null handling.
