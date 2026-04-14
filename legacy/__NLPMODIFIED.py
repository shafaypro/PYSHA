from nltk.tokenize import sent_tokenize, word_tokenize  # importing the word and the sentence tokenization.
from nltk.stem import PorterStemmer  # importing the port stemmer
import nltk


class __NLPModified:
    def __init__(self):
        pass  # Just for debugging purpose.

    def download_preferences(self):
        import nltk  # importing the natural language processing module
        nltk.download()  # opening the gui based Natural language processing download kit

    def sentence_Tokenizations(self, sentences=""):
        tokenized_sentences = sent_tokenize(sentences)  # Tokenizing on the basis of the sentences
        return tokenized_sentences  # Returns the tokenized sentences

    def word_Tokenization(self, sentence=""):
        if sentence.__contains__(". "):
            pass  # debugging purpose !
        else:
            tokenized_words = word_tokenize(sentence)  # this is the word tokenization of the sentences.
            return tokenized_words  # returning the tokenized string as well.

    def stop_word_filterning(self, sentence=""):
        from nltk.corpus import stopwords  # importing the required package at the desired time.
        stop_words_list = set(stopwords.words("english"))  # identifying the stop words
        words_sentence_list = word_tokenize(sentence)  # For the filtered sentences list
        filtered_new_sentence = [w for w in words_sentence_list if w not in stop_words_list]
        # above is the filtering of the sentences so that the sentence can be filtered by removing the non sense words
        return filtered_new_sentence

    '''
    The process of steaming is having the base root of something and trying to shorted the length of the text
    without changing the meaning of it. Sort of a normalization method.
    Why we steam ?
    To shorten the lookup and normalize sentences.
    Consider the following example.
    I was taking a ride in the car.
    I was riding in the car.
    This sentence means the same thing. in the car is the same. I was is the same. the ing denotes a clear past-tense in
    both cases, so is it truly necessary to differentiate
    between ride and riding, in the case of just trying to figure out the meaning of what this past-tense activity was?
    No, not really.This is just one minor example, but imagine every word in the English language, every possible tense
    and affix you can put on a word. Having individual dictionary entries per version would be highly redundant and
    inefficient, especially since, once we convert to numbers, the "value" is going to be identical.
    One of the most popular stemming algorithms is the Porter steamer, which has been around since 1979.
    '''

    # keep in mind it takes words as input , and stem the specified word
    def steam_words(self, word):
        ps_obj = PorterStemmer()  # creating the port steamer
        steamed_word = ps_obj.stem(word)
        return steamed_word  # returns the steamed word to the main file .

    # Natural Language displaying setneces .


    """
    One of the most powerful aspects of NLTK module is the parts of speech ,
    It CAN DO PARTS OF SPEECH TAGGING FOR YOU. This means labelling the words on the basis of NOUN, Adjectives,
     verbs etc.
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

    # TODO : here we have used the unsupervised learning
    def parts_of_speechtag(self, sentences=""):
        from nltk.corpus import state_union  # for importing the already stored data, to be trained with
        from nltk.tokenize import PunktSentenceTokenizer  # importing the already POS intelligent punkbuster tokenizer
        training_text = state_union.raw("2005-GWBUSH.txt")  # Training set imported from the state union local repo.
        sample_text = sentences
        custom_sentence_tokenized = PunktSentenceTokenizer(train_text=training_text)
        # This is the unsupervised learning
        tokenization_unsupervised = custom_sentence_tokenized.tokenize(str(sample_text))

        # tokenizing using unsupervised learning
        # print(tokenization_unsupervised)  # just for hedebuggin purposes
        # print(type(tokenization_unsupervised))  # checking the type of the sentences

        self.processing_POS_tokenization(tokenization_unsupervised=tokenization_unsupervised)

        # Calling the Process content

    '''The below is theprocessing for the unsuper vised learning due to the PUNKbustertokenizer'''

    def processing_POS_tokenization(self, tokenization_unsupervised):
        for _ in tokenization_unsupervised:
            words = word_tokenize(_)  # Current sentence is beign passed to the word being tokenized
            tagged_posts = nltk.pos_tag(words)
            print(tagged_posts)

    def display_sentences(self, sentences):
        for sentence in sentences:
            print(sentence)


if __name__ == '__main__':
    nlpmodified = __NLPModified()
    sentences = "My name is Muhammad Shafay Amjad. i live in New york city in my dreams. " \
                "I do have different things going on in my life and you are not in it."
    # Below is for debugging of the sentence tokenization
    tokenized_sentenceslist = nlpmodified.sentence_Tokenizations(sentences=sentences)
    # filtered_sentences = []
    # for sentence in tokenized_sentenceslist:
    #     filtered_sentences.append(nlpmodified.stop_word_filterning(sentence=sentence))  # Filterenign the spentences
    #
    # print("Filtered Sentence after sentence tokenization --> word tokenization --> stop words exclusions--> \n", filtered_sentences)
    print("POS", nlpmodified.parts_of_speechtag(sentences))
    # for sentence in tokenized_sentenceslist:
    #     words_list = nlpmodified.word_Tokenization(sentence)  # this will having the tokenized return value !!
    #     print(words_list)
