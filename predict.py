import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem.snowball import SnowballStemmer
import re
import sys
import warnings
stemmer = SnowballStemmer("english")
stop_words = set(stopwords.words('english'))
stop_words.update(['geek','given','zero','may','also','across','among','beside','however','yet','within','return'])
re_stop_words = re.compile(r"\b(" + "|".join(stop_words) + ")\\W", re.I)
from sklearn.feature_extraction.text import TfidfVectorizer

def cleanHtml(sentence):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', str(sentence))
    return cleantext

def cleanPunc(sentence): #function to clean the word of any punctuation or special characters
    cleaned = re.sub(r'[?|!|\'|"|#]',r'',sentence)
    cleaned = re.sub(r'[.|,|)|(|\|/]',r' ',cleaned)
    cleaned = cleaned.strip()
    cleaned = cleaned.replace("\n"," ")
    return cleaned

def keepAlpha(sentence):
    alpha_sent = ""
    for word in sentence.split():
        alpha_word = re.sub('[^a-z A-Z]+', ' ', word)
        alpha_sent += alpha_word
        alpha_sent += " "
    alpha_sent = alpha_sent.strip()
    return alpha_sent


def removeStopWords(sentence):
    global re_stop_words
    return re_stop_words.sub(" ", sentence)


def stemming(sentence):
    stemSentence = ""
    for word in sentence.split():
        stem = stemmer.stem(word)
        stemSentence += stem
        stemSentence += " "
    stemSentence = stemSentence.strip()
    return stemSentence

def preprocess(new_prob):
    new_prob = cleanHtml(new_prob)
    new_prob = keepAlpha(new_prob)
    new_prob = removeStopWords(new_prob)
    new_prob = stemming(new_prob)
    new_prob = [new_prob]
    return new_prob

