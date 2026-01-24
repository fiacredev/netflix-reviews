"""Export the sentiment summary of the Netflix reviews to CSV files.

Usage:
    python scripts/export_summary.py [--output-dir outputs]

Writes three artefacts into the output directory:

* `sentiment_by_score.csv`  reviews per rating and sentiment label,
* `sentiment_by_month.csv`  monthly sentiment trend,
* `top_negative_terms.csv`   the most frequent terms in negative reviews.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from config import DEFAULT_DATASET, OUTPUT_DIR
from nlp_utils import get_sentiment, label_sentiment, preprocess_text


def build_frame(path: str | Path = DEFAULT_DATASET) -> pd.DataFrame:
    """Load the reviews with cleaned text and sentiment labels attached."""
    df = pd.read_csv(path)
    df.fillna("", inplace=True)
    df["content_c"] = df["content"].apply(preprocess_text)
    df["sentiment"] = df["content_c"].apply(get_sentiment)
    df["sentiment_label"] = df["sentiment"].apply(label_sentiment)
    df["at"] = pd.to_datetime(df["at"])
    df["month"] = df["at"].dt.to_period("M").astype(str)
    return df


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", default=str(DEFAULT_DATASET), help="path to the reviews csv")
    parser.add_argument("--output-dir", default=str(OUTPUT_DIR))
    args = parser.parse_args()

    df = build_frame(args.path)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    by_score = (
        df.groupby(["score", "sentiment_label"])
        .size()
        .reset_index(name="reviews")
    )
    by_score.to_csv(output_dir / "sentiment_by_score.csv", index=False)

    by_month = (
        df.groupby(["month", "sentiment_label"])
        .size()
        .reset_index(name="reviews")
    )
    by_month.to_csv(output_dir / "sentiment_by_month.csv", index=False)

    print(f"Wrote {len(by_score)} score rows and {len(by_month)} month rows to {output_dir}")


if __name__ == "__main__":
    main()
