# Netflix Reviews: Sentiment Analysis and Topic Modeling

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/jupyter-notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Dataset](https://img.shields.io/badge/reviews-113%2C068-lightgrey.svg)](netflix_reviews.csv)
[![Topics](https://img.shields.io/badge/LDA%20topics-5-blue.svg)](docs/themes.md)
[![Last update](https://img.shields.io/badge/last%20update-January%202026-brightgreen.svg)](docs/release_notes.md)

An exploratory analysis of 113,068 Netflix mobile application reviews
covering data cleaning, sentiment scoring, keyword analysis and latent
Dirichlet allocation topic modelling.

The project studies reviews collected from the Google Play Store between
September 2018 and June 2024 and answers three questions: how do ratings
distribute, what language do unhappy customers use, and which product themes
dominate the complaints.

---

## Table of contents

- [Overview](#overview)
- [Key findings](#key-findings)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Results](#results)
- [Getting started](#getting-started)
- [Project structure](#project-structure)
- [Reproducibility](#reproducibility)
- [Limitations](#limitations)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Contact](#contact)

---

## Overview

The analysis lives in a single notebook that runs from top to bottom:

1. the raw reviews are loaded and profiled,
2. the review text is cleaned and the missing values are handled,
3. every review is scored for sentiment and labelled,
4. the ratings and the sentiment are visualised,
5. the negative reviews are summarised with a word cloud,
6. an LDA model extracts the recurring complaint themes.

The notebook stores its outputs, so the committed file shows the exact
results that were produced. The scripts in `scripts/` mirror the same logic
for terminal and continuous integration use, and the documentation in `docs/`
explains every step in detail.

### Notebook walkthrough

| Stage | Cells | Description |
| --- | --- | --- |
| Setup | 1 | Imports for data handling, NLP, topic modelling and visualisation. |
| Loading | 2 | Reads the CSV and prints the shape and the columns. |
| Cleaning | 3 to 8 | Text preprocessing, missing values, timestamps and column selection. |
| Ratings | 9 | Distribution of the star scores. |
| Sentiment | 10 to 13 | Polarity scoring, labelling, preview and the sentiment crosstab. |
| Keywords | 14 to 16 | Stopwords and the word cloud of the negative reviews. |
| Topics | 17 to 24 | Tokenisation, corpus, LDA model, topic keywords and the interactive view. |

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

## Dataset

The dataset holds one row per Google Play Store review with the reviewer
name, the review body, the star rating, the number of thumbs up, the app
version and the timestamp. Two reviews have no text, one reviewer is
anonymised, and the two version columns are missing on the 16,491 oldest
reviews. The full schema is documented in `docs/data_dictionary.md`.

| Column | Type | Description |
| --- | --- | --- |
| `reviewId` | string | Unique identifier of the review. |
| `userName` | string | Display name of the reviewer. |
| `content` | string | Body of the review. |
| `score` | integer | Star rating from 1 to 5. |
| `thumbsUpCount` | integer | Users that marked the review as helpful. |
| `reviewCreatedVersion` | string | App version used by the reviewer. |
| `at` | datetime | Timestamp of the review. |
| `appVersion` | string | Application version reported by the device. |

## Methodology

1. Load the raw CSV and profile the shape, the columns and the missing
   values.
2. Clean the review text: lower case, remove punctuation, remove digits,
   strip whitespace.
3. Fill the missing values with an empty string and parse the timestamps.
4. Keep the four columns required for the analysis.
5. Score the sentiment with `TextBlob` and label each review as positive,
   negative or neutral using the -0.1 and 0.1 polarity thresholds.
6. Visualise the rating distribution and the rating against sentiment
   crosstab.
7. Build a word cloud from the negative reviews with an extended stopword
   list.
8. Train an LDA model with five topics over the negative review corpus and
   inspect the result with `pyLDAvis`.

The full description lives in `docs/methodology.md`.

## Results

### The complaints fall into five recurring themes

| Topic | Theme | Representative keywords |
| --- | --- | --- |
| 0 | Account, payment and subscription access | payment, account, worst, cant, password, sign, money, bad, even, subscription |
| 1 | Playback, video quality and subtitles | screen, black, brightness, quality, video, subtitles, dark, watch, cant, see |
| 2 | App errors, updates and requested fixes | please, open, fix, unable, error, cant, try, update, play, keeps |
| 3 | Price, value and streaming complaints | cant, use, watch, even, now, expensive, streaming, pay, money, content |
| 4 | Content quality and catalogue complaints | movies, watch, shows, dont, bad, hate, want, new, watching, im |

### The vocabulary of complaints is repetitive

The most frequent terms in the negative reviews are `watch`, `cant`, `even`,
`please`, `movies`, `update`, `bad`, `shows`, `fix`, `worst`, `screen`,
`service`, `annoying`, `account` and `unable`. The same words repeat across
thousands of reviews, which is why a keyword view is informative on this
dataset.

### Product reliability drives the negative score

Playback failures, black screens and buffering appear in a large share of the
technical complaints, while pricing complaints dominate the words around
`money`, `pay` and `subscription`. The two groups dominate the negative
sentiment of the whole dataset.

Detailed numbers are in `docs/findings.md`, and the themes are discussed in
`docs/themes.md`.

## Getting started

```bash
git clone <repository-url>
cd netflix-reviews
python -m venv .venv
source .venv/bin/activate
make setup
```

Then open the notebook:

```bash
make notebook
```

Or run the pipeline from the terminal:

```bash
make check
make sentiment
make topics
```

## Project structure

```
netflix-reviews/
├── netflix.ipynb            the analysis notebook, executed top to bottom
├── netflix_reviews.csv      the raw review dataset
├── requirements.txt         pinned Python dependencies
├── environment.yml          conda environment specification
├── Makefile                 shortcuts for the common commands
├── docs/                    written documentation for the analysis
├── scripts/                 helper scripts that mirror the notebook
└── tests/                   unit tests for the helper modules
```

## Reproducibility

The dataset travels with the repository and is never modified on disk. All
cleaning happens in memory, no sampling is used and the topic model can be
seeded through `scripts/config.py`. The exact versions are pinned in
`requirements.txt`, and the continuous integration workflow runs the tests and
validates the notebook on every push. More details are in
`docs/reproducibility.md`.

## Limitations

`TextBlob` relies on a lexicon, so sarcasm and domain specific slang are
misread; the rating and the detected polarity disagree on roughly a quarter of
the single star reviews; and the dataset only covers the Google Play Store,
so it describes Android users of the Netflix application. The full list is in
`docs/limitations.md`.

## Documentation

| Document | Contents |
| --- | --- |
| `docs/data_dictionary.md` | Every column of the dataset, with types and missing values. |
| `docs/dataset_profile.md` | Volume, ratings and data quality of the collection. |
| `docs/methodology.md` | The eight steps of the analysis pipeline. |
| `docs/findings.md` | The numbers behind the key findings. |
| `docs/themes.md` | The five complaint themes in detail. |
| `docs/reproducibility.md` | Environment, determinism and verification steps. |
| `docs/limitations.md` | What the analysis cannot show. |
| `docs/usage.md` | Command line examples for every script. |
| `docs/glossary.md` | The terms used throughout the project. |
| `docs/faq.md` | Answers to the questions that come up most often. |

## Contributing

Contributions are welcome, in particular new visualisations, alternative
topic counts and documentation that clarifies a step of the pipeline. Please
read `CONTRIBUTING.md` first, create a branch for your change and run the
tests before opening a pull request.

```bash
python -m unittest discover -s tests -v
make check
```

## Contact

Maintainer: **fiacredev**

- Email: `fiacredeveloper@gmail.com`
- Repository issues: use the issue templates in `.github/ISSUE_TEMPLATE`.

Questions about the method, the results or the reproduction steps are welcome
by email or in an issue.
