# Frequently asked questions

## Why is the dataset stored in the repository?

The analysis is reproducible only if the exact input travels with the code.
The file is 30 MB, which is acceptable for a dataset of this kind and avoids
any dependency on an external download that could change over time.

## Why are the reviews not sentiment analysis with a transformer model?

The notebook uses `TextBlob`, which is fast, deterministic and dependency
light. The goal is a transparent baseline that shows the full pipeline. A
transformer based classifier can be plugged in later by replacing
`get_sentiment` in `scripts/nlp_utils.py`.

## Why is one star not always negative?

`TextBlob` measures the polarity of the written text, not the rating. Short
complaints such as `good app` with a one star rating are detected as neutral
or positive. The crosstab of rating and sentiment in `docs/findings.md` shows
where the two disagree.

## How many topics does the model use?

Five. That number keeps every topic large enough to be interpretable and
matches the five recurring complaint themes described in `docs/themes.md`.

## Why does the notebook call `simple_preprocess` on token lists?

The tokenisation step in the notebook keeps the review text as a list of
tokens. The helper script `scripts/topic_modeling.py` joins the tokens before
calling `simple_preprocess`, which expects a string, and produces the same
corpus.

## Do the scripts duplicate the notebook?

Yes, on purpose. The notebook is the narrative version of the analysis and the
scripts are the operational version. Both use the helpers in
`scripts/nlp_utils.py` so that they cannot drift apart silently.

## Where are the generated tables stored?

The scripts write their artefacts to `outputs/`, which is excluded from git.
The results of the recorded run are documented in `docs/findings.md`.
