# Limitations

## The sentiment model is lexical

`TextBlob` relies on a lexicon of word polarities and a simple negation
handler. It does not understand sarcasm, irony or domain specific slang, all
of which are common in app store reviews. The measured polarity should be
read as a rough signal rather than a ground truth.

## Ratings and text disagree

Around a quarter of the one star reviews are detected as positive or neutral.
This is expected: the rating captures the overall experience while the text
only captures part of it.

## Short reviews dominate the vocabulary

Many reviews are a single word or a single sentence. The word cloud and the
topic model therefore reflect frequent complaints rather than detailed
arguments, and rare but severe problems are easily drowned out.

## The dataset is not a random sample

The reviews were collected from the Google Play Store, which over represents
users in certain markets and platforms. The iOS store is not represented, so
the findings describe Android users of the Netflix application.

## Topics depend on preprocessing choices

The stopword list, the number of topics and the number of passes change the
result. The settings used here are recorded in `scripts/config.py` and in the
notebook so that the outcome can be reproduced or challenged.

## No causal claims

The analysis is descriptive. It shows which complaints are frequent and how
sentiment relates to ratings, but it does not explain why a product change
caused a rating shift.
