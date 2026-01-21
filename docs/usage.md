# Usage examples

## Inspect the dataset

```bash
python scripts/inspect_dataset.py
```

Prints the shape, the column schema, the missing values, the score
distribution and the review date range.

## Report the sentiment distribution

```bash
python scripts/sentiment_summary.py
```

Scores every review, prints the overall sentiment split and the crosstab of
rating against sentiment label, and writes `outputs/sentiment_summary.csv`.

## Train the topic model

```bash
python scripts/topic_modeling.py --topics 5 --passes 5
```

Builds the corpus from the negative reviews and prints the ten most relevant
keywords for every topic.

## List the recurring complaint terms

```bash
python scripts/recurring_terms.py --top 25
```

Shows the most frequent tokens in the negative reviews.

## Export the summary tables

```bash
python scripts/export_summary.py --output-dir outputs
```

Writes `sentiment_by_score.csv` and `sentiment_by_month.csv`.

## Run the notebook

```bash
make notebook
```

JupyterLab opens with `netflix.ipynb` ready to run from the first cell.

## Run the checks

```bash
make check
python -m unittest discover -s tests -v
```
