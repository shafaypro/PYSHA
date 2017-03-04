from chatterbot import ChatBot  # importing the chat bot from the chatter api
from chatterbot.trainers import ListTrainer  # importing the list trainer
from chatterbot.trainers import ChatterBotCorpusTrainer  # importing the courpus package for the training of the

# Natural language processed (pre processed Chattber Bot corpus for the training purpose
'''The Class is for the Chatting of the PYthon Speech on hand assistant PYSHA'''


# Chatterbot belongs to chatterbot, any upgrading is on the basis of PYSHA.

class Chatting_PYSHA:
    def __init__(self, name="PYSHA", trainable=True, train_corpus=True):
        CB = None  # this is the none Chatbot
        if trainable:
            try:
                self.CB = ChatBot(name, read_only=not trainable)
                # if the chat bot is trainable then the read_only = false
                # self.train_text()  # Calling the train text to set the default trainable to be list trainable
                # self.train_textcourpus()  # Training on the basis of the text corpus
                self.CB.set_trainer(ListTrainer)  # Setting the Chatbot trainer to be CB trainer.
            except Exception as E:
                print("internal chat bot is not working Correctly, instantiation failed, and failed to"
                      " find the corpus", str(E))
        else:
            self.CB = ChatBot(name, read_only=trainable)  # if the chatbot is not trainable then the readonly - true
        if train_corpus:
            self.train_textcourpus()  # Training the text corpus if the statment is true

    '''The function used to training the text on the basis of the provided list'''
    # This has to be the training list , on which the chat bot needs to be trained on the basic off.
    '''Accepts a list , and trains from it. If you have a longer syntax use this'''
    def train_text(self, text_list):  # takes a text_list in the input
        self.CB.set_trainer(ListTrainer)
        self.CB.train(text_list)  # training the Chat bot from the Train text list

    ''' Function used to train the chatbot for English Text '''

    def train_textcourpus(self):
        self.CB.set_trainer(ChatterBotCorpusTrainer)  # Setting the chatbot trainer to be trained text corpus.
        self.CB.train("chatterbot.corpus.english")  # Training the english corpus of the chatterbot.
        # print("--Learning English corpus for PYSHA chat assistant")  # just for debugging

    ''' Function to retrieve the response  on the basis of the input string'''
    def retrieved_response(self, input_string):
        return self.CB.get_response(input_string)
        # getting the respectable responce
