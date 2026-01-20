# Glossary

**App version** The build of the mobile application that a reviewer was using
when they wrote the review. Missing on the oldest reviews.

**Bag of words** A representation of a document as the multiset of its
tokens, ignoring their order. Used to build the corpus for the topic model.

**Corpus** The collection of bag of words documents that the topic model is
trained on. In this project it contains the 19,506 negative reviews.

**Dictionary** The vocabulary of the corpus together with the mapping from
tokens to integer identifiers used by `gensim`.

**LDA** Latent Dirichlet Allocation, a generative probabilistic model that
discovers the topics shared by a collection of documents.

**Negative review** A review whose polarity score is below -0.1. There are
19,506 of them.

**Neutral review** A review whose polarity score falls between -0.1 and 0.1.
There are 35,126 of them.

**Polarity** The output of `TextBlob.sentiment.polarity`, a value between -1
and 1 where positive values describe positive language.

**Positive review** A review whose polarity score is above 0.1. There are
58,436 of them.

**Stopwords** Frequent words with little analytical value, removed before the
word cloud and the topic model are built.

**Thumbs up** The number of users that marked a review as helpful.

**Topic** A probability distribution over the vocabulary that characterises a
group of documents. Each of the five topics in this project corresponds to a
recurring complaint theme.
