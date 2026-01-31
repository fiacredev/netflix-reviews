"""Train an LDA topic model on the negative Netflix reviews.

Usage:
    python scripts/topic_modeling.py [--path netflix_reviews.csv]
                                    [--topics 5] [--passes 5]

Mirrors the topic modelling section of `netflix.ipynb`: negative reviews are
tokenised, stopwords removed, a dictionary and bag of words corpus are built
and a latent Dirichlet allocation model is trained on top of them.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import gensim
import pandas as pd
from gensim import corpora
from gensim.utils import simple_preprocess

from config import DEFAULT_DATASET, NUM_PASSES, NUM_TOPICS, RANDOM_SEED
from nlp_utils import build_stopwords, get_sentiment, label_sentiment, preprocess_text


def negative_reviews(path: str | Path = DEFAULT_DATASET) -> pd.DataFrame:
    """Return the reviews whose sentiment label is negative."""
    df = pd.read_csv(path)
    df.fillna("", inplace=True)
    df["content_c"] = df["content"].apply(preprocess_text)
    df["sentiment"] = df["content_c"].apply(get_sentiment)
    df["sentiment_label"] = df["sentiment"].apply(label_sentiment)
    return df[df["sentiment_label"] == "negative"]


def build_corpus(df: pd.DataFrame, stopwords: set) -> tuple:
    """Build a dictionary and a bag of words corpus from the reviews."""
    documents = []
    for text in df["content_c"]:
        tokens = simple_preprocess(text)
        documents.append([token for token in tokens if token not in stopwords])
    dictionary = corpora.Dictionary(documents)
    corpus = [dictionary.doc2bow(document) for document in documents]
    return dictionary, corpus


def train_model(corpus, dictionary, num_topics: int, num_passes: int):
    """Train the LDA model with a fixed seed for reproducible output."""
    return gensim.models.LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics,
        passes=num_passes,
        random_state=RANDOM_SEED,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", default=str(DEFAULT_DATASET), help="path to the reviews csv")
    parser.add_argument("--topics", type=int, default=NUM_TOPICS)
    parser.add_argument("--passes", type=int, default=NUM_PASSES)
    args = parser.parse_args()

    stopwords = build_stopwords()
    df = negative_reviews(args.path)
    dictionary, corpus = build_corpus(df, stopwords)
    model = train_model(corpus, dictionary, args.topics, args.passes)

    print(f"Documents: {len(corpus)}  Vocabulary: {len(dictionary)}")
    print(f"Topics: {args.topics}  Passes: {args.passes}\n")
    for topic_id in range(model.num_topics):
        keywords = ", ".join(word for word, _ in model.show_topic(topic_id, topn=10))
        print(f"Topic {topic_id}: {keywords}")


if __name__ == "__main__":
    main()
