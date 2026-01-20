"""Smoke tests for the dataset inspection script."""

import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))

from config import DEFAULT_DATASET  # noqa: E402
from inspect_dataset import load_dataset, summarize  # noqa: E402


class InspectDatasetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not DEFAULT_DATASET.exists():
            cls.df = None
        else:
            cls.df = load_dataset(DEFAULT_DATASET)

    def setUp(self):
        if self.df is None:
            self.skipTest("the reviews dataset is not available")

    def test_expected_columns(self):
        for column in ("reviewId", "userName", "content", "score", "at"):
            self.assertIn(column, self.df.columns)

    def test_summary_mentions_the_score_distribution(self):
        report = summarize(self.df)
        self.assertIn("Score distribution", report)
        self.assertIn("Earliest review date", report)

    def test_scores_are_within_the_valid_range(self):
        self.assertGreaterEqual(self.df["score"].min(), 1)
        self.assertLessEqual(self.df["score"].max(), 5)


if __name__ == "__main__":
    unittest.main()
