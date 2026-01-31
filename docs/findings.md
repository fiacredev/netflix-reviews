# Findings

The numbers below come from running the pipeline over the full dataset.

## Ratings are bimodal

39.2% of the reviews are single star and 28.4% are five star. Neutral
ratings are rare: only 10.5% of the dataset sits on three stars. Users either
love the product or write an angry review.

## Sentiment polarity follows the rating

| Score | Negative | Neutral | Positive |
| --- | --- | --- | --- |
| 1 | 13,721 | 19,680 | 10,942 |
| 2 | 2,379 | 4,508 | 3,875 |
| 3 | 1,739 | 4,178 | 6,016 |
| 4 | 912 | 2,969 | 9,972 |
| 5 | 755 | 3,791 | 27,631 |

Single star reviews are negative or neutral in 76.4% of the cases, while
85.9% of the five star reviews are detected as positive.

## Overall sentiment split

| Label | Reviews | Share |
| --- | --- | --- |
| Positive | 58,436 | 51.7% |
| Neutral | 35,126 | 31.1% |
| Negative | 19,506 | 17.2% |

## What the complaints are about

The most frequent terms in negative reviews are `watch`, `cant`, `even`,
`please`, `movies`, `update`, `bad`, `shows`, `fix`, `worst`, `screen`,
`service`, `annoying`, `account` and `unable`. The topic model separates them
into five recurring themes:

| Topic | Theme | Representative keywords |
| --- | --- | --- |
| 0 | Account, payment and subscription access | payment, account, worst, cant, password, sign, money, bad, even, subscription |
| 1 | Playback, video quality and subtitles | screen, black, brightness, quality, video, subtitles, dark, watch, cant, see |
| 2 | App errors, updates and requested fixes | please, open, fix, unable, error, cant, try, update, play, keeps |
| 3 | Price, value and streaming complaints | cant, use, watch, even, now, expensive, streaming, pay, money, content |
| 4 | Content quality and catalogue complaints | movies, watch, shows, dont, bad, hate, want, new, watching, im |

## Practical takeaways

- Reliability of playback dominates the technical complaints: the black screen
  theme is the most concrete and the easiest to act on.
- Payment and account problems produce the most intense language, with short
  reviews packed with words such as `unable`, `error` and `worst`.
- Pricing and value questions form a separate theme, which suggests that a
  sizeable part of the negative sentiment is about the price of the
  subscription rather than about the product itself.
