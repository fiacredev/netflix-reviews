"""Unit tests for the shared text processing helpers."""

import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))

from nlp_utils import (  # noqa: E402
    DOMAIN_STOPWORDS,
    get_sentiment,
    label_sentiment,
    preprocess_text,
    tokenize,
)


class PreprocessTextTests(unittest.TestCase):
    def test_lowercases_and_strips_punctuation(self):
        self.assertEqual(preprocess_text("Great Movie, Truly!"), "great movie truly")

    def test_removes_digits(self):
        cleaned = preprocess_text("season 2 was bad")
        self.assertNotIn("2", cleaned)
        self.assertEqual(cleaned.split(), ["season", "was", "bad"])

    def test_missing_values_become_empty_strings(self):
        self.assertEqual(preprocess_text(float("nan")), "")
        self.assertEqual(preprocess_text(None), "")


class TokenizeTests(unittest.TestCase):
    def test_keeps_alphanumeric_tokens_only(self):
        self.assertEqual(tokenize("Netflix app 4K streaming!"), ["netflix", "app", "4k"])

    def test_empty_string_returns_no_tokens(self):
        self.assertEqual(tokenize(""), [])


class LabelSentimentTests(unittest.TestCase):
    def test_positive_above_threshold(self):
        self.assertEqual(label_sentiment(0.5), "positive")

    def test_negative_below_threshold(self):
        self.assertEqual(label_sentiment(-0.5), "negative")

    def test_neutral_inside_the_band(self):
        self.assertEqual(label_sentiment(0.0), "neutral")

    def test_thresholds_are_inclusive_boundaries(self):
        self.assertEqual(label_sentiment(0.1), "neutral")
        self.assertEqual(label_sentiment(-0.1), "neutral")


class StopwordTests(unittest.TestCase):
    def test_domain_stopwords_are_listed(self):
        self.assertIn("netflix", DOMAIN_STOPWORDS)
        self.assertIn("app", DOMAIN_STOPWORDS)


if __name__ == "__main__":
    unittest.main()


class GetSentimentTests(unittest.TestCase):
    def test_positive_text_has_a_positive_polarity(self):
        self.assertGreater(get_sentiment("I love this application, it is wonderful"), 0.0)

    def test_negative_text_has_a_negative_polarity(self):
        self.assertLess(get_sentiment("This app is terrible and broken"), 0.0)

    def test_empty_text_is_neutral(self):
        self.assertEqual(get_sentiment(""), 0.0)
