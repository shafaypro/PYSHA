# TODO : IMplementation of the AI
from nltk.stem import \
    PorterStemmer  # this is  the steamer which will be used for the Steaming of the Tokenized Words
from nltk.tokenize import word_tokenize, sent_tokenize, \
    PunktSentenceTokenizer  # importing both of the tokenization packages form the modules
from nltk.corpus import \
    state_union  # this imports the state union function which need to be taken in the corpus as the state union of the words.
import nltk # importing the natural lagnuage processing package
from nltk.corpus import stopwords  # locating the stop words.


class NaturalProcessing:
    def __init__ (self):
        print("NONCE!!!!")

    def recognize_text (self):
        print("")

    def steam_word_port (self, text=""):
        if text != "":
            tokenized_word = word_tokenize(text)  # this is the word tokenized !
            ps = PorterStemmer()  # Creating a port stemmer , its basically a stemmer technique , which Gives you the stem representation of the specified Words !
            tokenized_stem_words = []  # representing a list !
            for word in tokenized_word:
                tokenized_stem_words.append(ps.stem(word))
            return

    def word_tokeniztion (self, text="", sent_tokenized=True):
        if text != "":
            if sent_tokenized == True:
                Tokenized_sentence = sent_tokenize(text)
                return Tokenized_sentence
            else:
                Tokenized_words = word_tokenize(
                    text)  # this converts te passed stirng to the word tokenized for the scanning of the probability
                return Tokenized_words  # This returns the tokenized words !

    def stop_words_exclude (self, sentences=''):
        stop_words = set(stopwords.words('english'))  # English words are parssed out which are meaning less
        word_tokens = word_tokenize(sentences)
        filtered_sentences = [w for w in word_tokens if
                              w not in stop_words]  # this is the list of the filtered sentence
        ''' Alternative code for the word tokenization
        for w in word_tokens: # loop through each of the word in the word tokens!
            if w not in stop_words:  # if the word is not i nStop words Then
                filtered_sentence.append(w)]'''
        return filtered_sentences

    """
    One of the most powerful aspects of NLTK module is the parts of speech ,
    It CAN DO PARTS OF SPEECH TAGGING FOR YOU. This means labelling the words on the basis of NOUN, Adjectives, verbs etc.
    POS tag list:

    CC	coordinating conjunction
    CD	cardinal digit
    DT	determiner
    EX	existential there (like: "there is" ... think of it like "there exists")
    FW	foreign word
    IN	preposition/subordinating conjunction
    JJ	adjective	'big'
    JJR	adjective, comparative	'bigger'
    JJS	adjective, superlative	'biggest'
    LS	list marker	1)
    MD	modal	could, will
    NN	noun, singular 'desk'
    NNS	noun plural	'desks'
    NNP	proper noun, singular	'Harrison'
    NNPS	proper noun, plural	'Americans'
    PDT	predeterminer	'all the kids'
    POS	possessive ending	parent's
    PRP	personal pronoun	I, he, she
    PRP$	possessive pronoun	my, his, hers
    RB	adverb	very, silently,
    RBR	adverb, comparative	better
    RBS	adverb, superlative	best
    RP	particle	give up
    TO	to	go 'to' the store.
    UH	interjection	errrrrrrrm
    VB	verb, base form	take
    VBD	verb, past tense	took
    VBG	verb, gerund/present participle	taking
    VBN	verb, past participle	taken
    VBP	verb, sing. present, non-3d	take
    VBZ	verb, 3rd person sing. present	takes
    WDT	wh-determiner	which
    WP	wh-pronoun	who, what
    WP$	possessive wh-pronoun	whose
    WRB	wh-abverb	where, when
    """

    def process_content (self,tokenized=''):
        try:
            for i in tokenized[
                     :5]:  # here we are applying sentence limit so we can use this one for the processing the sentences.
                words = nltk.word_tokenize(i)  # Tokenizes all the word , using the word tokenize!
                tagged = nltk.pos_tag(words)  # Tags the specific words with the Natural language .
                print(tagged)  # Prints the words with the Tags in the form of the tupple .!


        except Exception as e:
            print(str(e))  # if there is an exception then this prints out the exception

    def partofspeechtag (self, sentences=''):  # th
        train_text = state_union.raw(
            "2005-GWBUSH.txt")  # This is the train text which will be used to tokenize the sample Test(unsupervised learning)
        sample_text = state_union.raw("2006-GWBUSH.txt")  # This is the sample text which will be tokenized later onward
        # print(type(sample_text))
        custom_sent_tokenizer = PunktSentenceTokenizer(
            train_text)  # This is the Train Text in the form of sentence being tokenized using the unsupervised learning.!
        # tokenized  = custom_sent_tokenizer.tokenize(sample_text) # Tokenizing he Custom sentence tokenize
        tokenized = custom_sent_tokenizer.tokenize(sentences)
        self.process_content(tokenized)
