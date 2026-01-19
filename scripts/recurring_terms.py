"""Report the most frequent terms in the negative Netflix reviews.

Usage:
    python scripts/recurring_terms.py [--top 25]

The report highlights which vocabulary dominates the complaints, which is the
basis for the complaint themes documented in `docs/themes.md`.
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

import pandas as pd
from gensim.utils import simple_preprocess

from nlp_utils import build_stopwords, get_sentiment, label_sentiment, preprocess_text

DEFAULT_DATASET = "netflix_reviews.csv"


def count_terms(path: str | Path = DEFAULT_DATASET) -> Counter:
    """Return a counter of the tokens used in negative reviews."""
    df = pd.read_csv(path)
    df.fillna("", inplace=True)
    df["content_c"] = df["content"].apply(preprocess_text)
    df["sentiment"] = df["content_c"].apply(get_sentiment)
    df["sentiment_label"] = df["sentiment"].apply(label_sentiment)

    stopwords = build_stopwords()
    counter = Counter()
    for text in df.loc[df["sentiment_label"] == "negative", "content_c"]:
        counter.update(token for token in simple_preprocess(text) if token not in stopwords)
    return counter


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", default=DEFAULT_DATASET, help="path to the reviews csv")
    parser.add_argument("--top", type=int, default=25, help="number of terms to display")
    args = parser.parse_args()

    counter = count_terms(args.path)
    print(f"Distinct terms in negative reviews: {len(counter)}\n")
    for rank, (term, count) in enumerate(counter.most_common(args.top), start=1):
        print(f"{rank:>3}. {term:<14} {count:>7,}")


if __name__ == "__main__":
    main()
