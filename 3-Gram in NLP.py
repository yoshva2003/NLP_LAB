#!/usr/bin/env python
# coding: utf-8

# #  N-Gram

# In[2]:


def generate_ngrams(text, n):
    # Tokenize the text into words
    words = text.split()
    
    # Create n-grams using list comprehension
    ngrams = [words[i:i+n] for i in range(len(words)-n+1)]
    
    return ngrams

# Example usage:
sentence = "I am learning Natural Language Processing"
n = 1  # Change to 1 for unigram, 2 for bigram, 3 for trigram

ngrams = generate_ngrams(sentence, n)
for gram in ngrams:
    print(gram)


# # Bi-Gram

# In[5]:


from nltk import bigrams
from nltk.tokenize import word_tokenize
import nltk

# Download punkt tokenizer if not already downloaded
nltk.download('punkt')

# Example sentence
sentence = "I love reading books"

# Tokenize the sentence into words
tokens = word_tokenize(sentence)

# Generate bigrams using nltk
bi_grams = list(bigrams(tokens))

# Display bigrams
for bg in bi_grams:
    print(bg)


# # Tri-Gram

# In[4]:


from nltk import trigrams
from nltk.tokenize import word_tokenize
import nltk

# Download punkt tokenizer if not already downloaded
nltk.download('punkt')

# Example sentence
sentence = "I love reading NLP books daily"

# Tokenize the sentence into words
tokens = word_tokenize(sentence)

# Generate trigrams using nltk
tri_grams = list(trigrams(tokens))

# Display trigrams
for tg in tri_grams:
    print(tg)


# In[ ]:




