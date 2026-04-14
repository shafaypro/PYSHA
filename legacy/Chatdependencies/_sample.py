import chatterbot
from chatterbot import ChatBot  # importing the chatbot
from chatterbot.trainers import ListTrainer  # importing the training list for the chatbot

name = "PYSHA"
chatbot = ChatBot(name, read_only=False)
chatbot = ChatBot("PYSHA")  # passing in the name for the chatbot
conversations = ["Hello", "Hi there!", "How are you doing?", "I'm doing great.", "That is good to hear", "Thank you.",
                 "You're"]
chatbot.set_trainer(ListTrainer)  # Training on the basis of list  of inputs
chatbot.train(conversations)  # training the conversational list ,
responce = chatbot.get_response(input("SAY:"))
print(responce)
