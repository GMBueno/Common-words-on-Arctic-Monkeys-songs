Girlfriend wondered what were the most common words on Arctic Monkeys' songs.

To answer, we wrote a simple Python script and ran on the dataset (lyrics.csv) from [this link on Kaggle](https://www.kaggle.com/datasets/ggapp1/arctic-monkeys-lyrics/).

### Top 50 most common words:

![50_most_common_words](50_most_common_words.png)

We also checked for the most common pairings of words (bigrams).

### Top 25 most common pairings:

![25_most_common_bigrams](25_most_common_bigrams.png)




#### important notes

Dataset doesn't contain all the latest songs, and also contains covers and demos.

We removed all mentions of song structure, which are not proper lyrics, such as "verse", "chorus", etc.

We also removed all punctuations and made everything lower case so we count properly. 

That said, there can be cases that words as wrongly counted, like "it's" and "its" becoming the same "word" after the removal of "'"

Numbers in the lyrics can be expressed as strings (eg: "one") or integers (eg: "1"), and we did not account for that.

There could be more problems, like "instrumental break" or smth like that.