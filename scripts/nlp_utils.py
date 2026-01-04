"""Reusable text processing helpers shared by the scripts and the notebook.

The functions mirror the logic used in `netflix.ipynb` so that results can be
reproduced from a terminal without opening Jupyter.
"""

from __future__ import annotations

import re
from typing import Iterable, List

import pandas as pd
from textblob import TextBlob

POSITIVE_THRESHOLD = 0.1
NEGATIVE_THRESHOLD = -0.1

DOMAIN_STOPWORDS = (
    "netflix",
    "movie",
    "show",
    "time",
    "app",
    "series",
    "phone",
)


def preprocess_text(text: object) -> str:
    """Lowercase the text, strip punctuation and remove digits.

    Non string values, including the missing values produced by pandas, are
    mapped to an empty string so the function is safe to apply to a whole
    column.
    """
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    return text.strip()


def tokenize(text: str) -> List[str]:
    """Split a review into lowercase alphanumeric tokens."""
    return [token for token in text.lower().split() if token.isalnum()]


def get_sentiment(text: str) -> float:
    """Return the polarity score of a piece of text."""
    return TextBlob(text).sentiment.polarity


def label_sentiment(polarity: float) -> str:
    """Map a polarity score to the positive, negative or neutral label."""
    if polarity > POSITIVE_THRESHOLD:
        return "positive"
    if polarity < NEGATIVE_THRESHOLD:
        return "negative"
    return "neutral"


def build_stopwords(extra: Iterable[str] = DOMAIN_STOPWORDS) -> set:
    """Return the analysis stopwords enriched with Netflix specific terms."""
    from wordcloud import STOPWORDS

    stopwords = set(STOPWORDS)
    stopwords.update(extra)
    return stopwords


def clean_series(series: pd.Series) -> pd.Series:
    """Apply `preprocess_text` to a whole column of reviews."""
    return series.apply(preprocess_text)


def sentiment_series(series: pd.Series) -> pd.Series:
    """Return the polarity score of every element of a column of reviews."""
    return series.apply(get_sentiment)


def label_series(polarity: pd.Series) -> pd.Series:
    """Label a series of polarity scores as positive, negative or neutral."""
    return polarity.apply(label_sentiment)
