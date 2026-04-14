import random
import textblob
from nltk.tokenize import *  # tokenizing the sentences on the basis of natural langauge processing
from textblob import *
from nltk.stem import PorterStemmer  # importing the port stemmer for later purpose
from nltk.corpus import stopwords
from nltk.corpus import state_union  # for importing the already stored data, to be trained with
from nltk.tokenize import PunktSentenceTokenizer  # importing the already POS intelligent punkbuster tokenizer
import nltk
GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)

GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]


def check_for_greeting(sentence):
    sentence = sentence.lower()
    words = sentence.split(" ")
    for word in words:
        if word.lower() in GREETING_KEYWORDS:
            return random.choice(GREETING_RESPONSES)
def parts_of_speechtag( sentences=""):
        from nltk.corpus import state_union  # for importing the already stored data, to be trained with
        from nltk.tokenize import PunktSentenceTokenizer  # importing the already POS intelligent punkbuster tokenizer
        training_text = state_union.raw("2005-GWBUSH.txt")  # Training set imported from the state union local repo.
        sample_text = sentences
        custom_sentence_tokenized = PunktSentenceTokenizer(train_text=training_text)
        # This is the unsupervised learning
        tokenization_unsupervised = custom_sentence_tokenized.tokenize(str(sample_text))

        # tokenizing using unsupervised learning
        # print(tokenization_unsupervised)  # just for the debugging purposes
        # print(type(tokenization_unsupervised))  # checking the type of the sentences

        processing_POS_tokenization(tokenization_unsupervised=tokenization_unsupervised)


def processing_POS_tokenization( tokenization_unsupervised):
    for _ in tokenization_unsupervised:
        words = word_tokenize(_)  # Current sentence is beign passed to the word being tokenized
        tagged_posts = nltk.pos_tag(words)
        print(tagged_posts)


def respond(sentences):
    tokenized_sentence = sent_tokenize(sentences)
    stop_words = set(stopwords.words("english"))  # Getting the stop words from the Local DB
    if len(tokenized_sentence) > 1:  # if the length of the tokenized sentence is greater than one

        # for sentence in tokenized_sentence:
        #     words = word_tokenize(sentence)  # Each word is tokenized
            pos_tagged = parts_of_speechtag(sentences)
            print(tuple(pos_tagged))
            # filtered_words = [w for w in words if w not in stop_words]  # removing the additional stop words for
            # portStemer_object = PorterStemmer()
            # filtered_steam_words = [portStemer_object.stem(w) for w in filtered_words]
            # return filtered_steam_words
    else:
        pos_tagged = parts_of_speechtag(sentences)
        print(type(pos_tagged))
        # words = word_tokenize(sentences)
        # filtered_words = [w for w in words if w not in stop_words]
        # portStemer_object = PorterStemmer()
        # filtered_steam_words = [portStemer_object.stem(w) for w in filtered_words]
        #return filtered_steam_words

print(respond(input()))
