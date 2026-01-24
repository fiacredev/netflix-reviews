"""Unit tests for the shared configuration module."""

import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))

from config import (  # noqa: E402
    DEFAULT_DATASET,
    NEGATIVE_THRESHOLD,
    NUM_PASSES,
    NUM_TOPICS,
    POSITIVE_THRESHOLD,
    RANDOM_SEED,
)


class ConfigTests(unittest.TestCase):
    def test_dataset_points_to_the_repository_root(self):
        self.assertEqual(DEFAULT_DATASET.name, "netflix_reviews.csv")

    def test_sentiment_thresholds_are_symmetric(self):
        self.assertEqual(POSITIVE_THRESHOLD, -NEGATIVE_THRESHOLD)

    def test_analysis_defaults(self):
        self.assertEqual(NUM_TOPICS, 5)
        self.assertEqual(NUM_PASSES, 5)
        self.assertIsInstance(RANDOM_SEED, int)


if __name__ == "__main__":
    unittest.main()
