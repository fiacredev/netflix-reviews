# Methodology

The analysis follows a standard opinion mining pipeline. Every step is
implemented in `netflix.ipynb` and mirrored by the scripts in `scripts/`.

## 1. Load and profile

The raw CSV is loaded with `pandas.read_csv`. The shape, the column schema and
the number of missing values are printed before any transformation so that
later conclusions can be traced back to the original data.

## 2. Clean the review text

Each review body is normalised by `preprocess_text`:

1. lower casing,
2. removal of punctuation with `re.sub(r"[^\w\s]", "", text)`,
3. removal of digits with `re.sub(r"\d+", "", text)`,
4. stripping of leading and trailing whitespace.

The result is stored in a new column `content_c`; the original `content` column
is never overwritten.

## 3. Handle missing values

Missing cells are filled with an empty string. Reviews without text cannot be
scored for sentiment, but they remain in the dataset so that the rating
distribution is not biased.

## 4. Parse the timestamps

The `at` column is converted with `pd.to_datetime`, which allows the review
date range to be reported and the data to be sliced by period.

## 5. Score the sentiment

`TextBlob(...).sentiment.polarity` returns a score in the range -1 to 1. The
score is converted into a categorical label with the thresholds used in the
notebook:

| Polarity | Label |
| --- | --- |
| greater than 0.1 | positive |
| less than -0.1 | negative |
| otherwise | neutral |

## 6. Visualise the ratings

A bar plot shows the rating distribution. A second count plot crosses the
rating with the sentiment label, which makes the agreement between the star
rating and the detected polarity visible.

## 7. Extract keywords from negative reviews

The stopword list from `wordcloud` is extended with Netflix specific terms
(`netflix`, `movie`, `show`, `time`, `app`, `series`, `phone`). A word cloud
built from the negative reviews shows which words dominate the complaints.

## 8. Model the topics

The negative reviews are tokenised, filtered against the stopword list and
converted into a `gensim` dictionary and a bag of words corpus. A latent
Dirichlet allocation model with five topics and five passes is trained on the
corpus, the keywords of every topic are printed and the result is rendered
with `pyLDAvis` for interactive inspection.

## Reproducibility

- The analysis is deterministic: no sampling is used, and the topic model can
  be seeded through `scripts/config.py`.
- The dataset is never modified on disk; every transformation happens in
  memory.
- The scripts and the notebook share the helpers in `scripts/nlp_utils.py`.
