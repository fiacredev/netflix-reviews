# Project structure

```
netflix-reviews/
├── netflix.ipynb            the analysis notebook, executed top to bottom
├── netflix_reviews.csv      the raw review dataset
├── requirements.txt         pinned Python dependencies
├── environment.yml          conda environment specification
├── Makefile                 shortcuts for the common commands
├── pytest.ini               test runner configuration
├── .github/
│   └── workflows/
│       └── notebook-ci.yml  continuous integration for the tests
├── docs/                    written documentation for the analysis
│   ├── data_dictionary.md
│   ├── dataset_profile.md
│   ├── faq.md
│   ├── findings.md
│   ├── glossary.md
│   ├── limitations.md
│   ├── methodology.md
│   ├── outputs.md
│   ├── project_structure.md
│   ├── reproducibility.md
│   ├── themes.md
│   └── usage.md
├── scripts/                 helper scripts that mirror the notebook
│   ├── config.py            shared constants and paths
│   ├── export_summary.py    writes the sentiment summary to CSV
│   ├── inspect_dataset.py   profiles the raw dataset
│   ├── nlp_utils.py         shared preprocessing helpers
│   ├── recurring_terms.py   most frequent terms in negative reviews
│   ├── sentiment_summary.py sentiment distribution report
│   └── topic_modeling.py    trains the LDA model
└── tests/                   unit tests for the helper modules
    ├── test_config.py
    ├── test_inspect_dataset.py
    └── test_nlp_utils.py
```

## Design rules

- The notebook stays the reference implementation. The scripts exist so that
  the same logic can be executed from a terminal or a continuous integration
  job.
- Shared constants live in `scripts/config.py`; shared text processing lives in
  `scripts/nlp_utils.py`.
- Generated artefacts are written to `outputs/`, which is ignored by git.
