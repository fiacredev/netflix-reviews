"""Summarise the sentiment distribution of the Netflix reviews.

Usage:
    python scripts/sentiment_summary.py [--path netflix_reviews.csv]
                                       [--output outputs/sentiment_summary.csv]

Scores every review with TextBlob, labels it as positive, negative or neutral
and prints the distribution per rating. Optionally writes a CSV summary to the
output directory.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from config import DEFAULT_DATASET, OUTPUT_DIR
from nlp_utils import get_sentiment, label_sentiment, preprocess_text

REVIEW_COLUMNS = ["content_c", "score", "reviewId", "at"]


def build_frame(path: str | Path = DEFAULT_DATASET) -> pd.DataFrame:
    """Load the reviews and attach cleaned text plus a sentiment label."""
    df = pd.read_csv(path)
    df.fillna("", inplace=True)
    df["content_c"] = df["content"].apply(preprocess_text)
    df["sentiment"] = df["content_c"].apply(get_sentiment)
    df["sentiment_label"] = df["sentiment"].apply(label_sentiment)
    df["at"] = pd.to_datetime(df["at"])
    return df[REVIEW_COLUMNS + ["sentiment", "sentiment_label"]]


def summarize(df: pd.DataFrame) -> str:
    """Return a printable summary of the sentiment distribution."""
    counts = df["sentiment_label"].value_counts()
    share = (counts / len(df) * 100).round(2)
    lines = ["Overall sentiment distribution:", ""]
    lines.extend(f"{label:<10} {counts[label]:>8,}  {share[label]:>6}%" for label in counts.index)
    lines.append("")
    lines.append("Sentiment per star rating:")
    lines.append(pd.crosstab(df["score"], df["sentiment_label"]).to_string())
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", default=str(DEFAULT_DATASET), help="path to the reviews csv")
    parser.add_argument("--output", default=str(OUTPUT_DIR / "sentiment_summary.csv"))
    args = parser.parse_args()

    df = build_frame(args.path)
    print(summarize(df))

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    summary = (
        df.groupby(["score", "sentiment_label"])
        .size()
        .reset_index(name="reviews")
    )
    summary.to_csv(output, index=False)
    print(f"\nWritten {output}")


if __name__ == "__main__":
    main()
