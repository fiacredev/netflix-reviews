"""Shared configuration for the Netflix reviews analysis scripts."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data
DEFAULT_DATASET = PROJECT_ROOT / "netflix_reviews.csv"
OUTPUT_DIR = PROJECT_ROOT / "outputs"

# Analysis parameters
POSITIVE_THRESHOLD = 0.1
NEGATIVE_THRESHOLD = -0.1
NUM_TOPICS = 5
NUM_PASSES = 5
RANDOM_SEED = 42

# Vocabulary
DOMAIN_STOPWORDS = (
    "netflix",
    "movie",
    "show",
    "time",
    "app",
    "series",
    "phone",
)
