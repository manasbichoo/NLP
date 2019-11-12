import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import nltk
import urllib.request
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from string import punctuation
from heapq import nlargest
nltk.download("stopwords")
from collections import defaultdict

file = open("myfile.txt", "r")
text1 = file.readlines()
text=text1[0]
# tokenize the text
tokens =[t for t in text.split()]

clean_token =tokens[:]
#define irrelevant words that include stop words , punctuations and numbers
stopword = set(stopwords.words('english') + list(punctuation) + list("0123456789") )
for token in tokens:
    if token in stopword:
        clean_token.remove(token)

print(clean_token)

freq = nltk.FreqDist(clean_token)
top_words=[]
top_words=freq.most_common(100)
print(top_words)

sentences = sent_tokenize(text)
print(sentences)

print("###################################################################################")
ranking = defaultdict(int)
for i, sent in enumerate(sentences):
    for word in word_tokenize(sent.lower()):
        if word in freq:
            ranking[i]+=freq[word]
    top_sentences = nlargest(10, ranking, ranking.get)
print(top_sentences)
print("###################################################################################")

print(sentences)
print("###################################################################################")

sorted_sentences = [sentences[j] for j in sorted(top_sentences)]
print(sorted_sentences)