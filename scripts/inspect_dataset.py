"""Inspect the raw Netflix reviews dataset.

Usage:
    python scripts/inspect_dataset.py [--path netflix_reviews.csv]

Prints the dataset shape, the column schema, missing value counts, the score
distribution and the review date range. The script is read-only: it never
writes to the source CSV.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

DEFAULT_DATASET = "netflix_reviews.csv"
DEFAULT_ENCODING = "utf-8"


def load_dataset(path: str | Path = DEFAULT_DATASET) -> pd.DataFrame:
    """Load the raw reviews CSV into a pandas DataFrame."""
    return pd.read_csv(path)


def summarize(df: pd.DataFrame) -> str:
    """Return a human readable summary of the dataset."""
    lines = [
        f"Shape of the dataset: {df.shape}",
        f"Columns in the dataset: {df.columns.tolist()}",
        "",
        "Missing values per column:",
        df.isnull().sum().to_string(),
        "",
        "Score distribution:",
        df["score"].value_counts().sort_index().to_string(),
        "",
        f"Unique reviewers: {df['userName'].nunique()}",
        f"Total thumbs up: {df['thumbsUpCount'].sum()}",
        f"Earliest review date: {df['at'].min()}",
        f"Latest review date: {df['at'].max()}",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", default=DEFAULT_DATASET, help="path to the reviews csv")
    parser.add_argument("--encoding", default=DEFAULT_ENCODING, help="csv encoding")
    args = parser.parse_args()

    df = load_dataset(args.path)
    print(summarize(df))


if __name__ == "__main__":
    main()
