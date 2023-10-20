import pandas as pd
from collections import Counter
import string
import matplotlib.pyplot as plt
import nltk
from nltk import bigrams

# Load the dataset
df = pd.read_csv("lyrics.csv")

# Concatenate all the lyrics into one long string
all_lyrics = ' '.join(df['lyrics'])

# Convert the lyrics to lowercase and remove punctuation
all_lyrics = all_lyrics.lower().translate(str.maketrans('', '', string.punctuation))

# Split the lyrics into words
all_words = all_lyrics.split()

def plot_most_common_words(quantity = 50, start = 0):
  # Remove words that are not lyrics but lyric structure such as 'verse' and 'chorus'
  filter_words = {"verse", "chorus", "1", "2", "3", "4", "bridge"}
  filtered_words = [ww for ww in all_words if ww not in filter_words]

  
  # Count the occurrences of each word
  word_count = Counter(filtered_words)

  most_common_words = word_count.most_common(quantity + start)[start:]

  # Split the results into words and counts for plotting
  words, counts = zip(*most_common_words)

  # Plotting
  plt.figure(figsize=(14, 8))
  plt.bar(words, counts, color='skyblue')
  plt.xlabel('Words')
  plt.ylabel('Counts')
  plt.title(f'{start+1} to {start+quantity} Most Common Words in Arctic Monkeys Lyrics')
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.show()

def plot_most_common_bigrams(quantity=20):
  # Generate bigrams from the words
  bi_grams_list = list(bigrams(all_words))

  # Remove bigrams that contain not lyrics but lyric structure such as 'verse' and 'chorus'
  filter_words = {"verse", "chorus", "1", "2", "3", "4", "bridge"}
  filtered_bigrams = [bg for bg in bi_grams_list if not any(word in bg for word in filter_words)]


  # Count the occurrences of each bigram
  bigram_count = Counter(filtered_bigrams)

  # Get the 20 most common bigrams
  most_common_bigrams = bigram_count.most_common(quantity)

  # Split the results into bigrams and counts for plotting
  bigrams_tuples, counts = zip(*most_common_bigrams)
  bigram_strings = [' '.join(bigram) for bigram in bigrams_tuples]

  # Plotting
  plt.figure(figsize=(15, 9))
  plt.bar(bigram_strings, counts, color='lightcoral')
  plt.xlabel('Bigrams')
  plt.ylabel('Counts')
  plt.title(f'Top {quantity} Most Common Bigrams in Arctic Monkeys Lyrics')
  plt.xticks(rotation=65)
  plt.tight_layout()
  plt.show()

plot_most_common_words(50)
plot_most_common_bigrams(50)