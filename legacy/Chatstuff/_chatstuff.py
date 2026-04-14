from chatterbot import ChatBot  # importing the chat bot from the chatter api


CB = ChatBot("SHAFAY")
responce = CB.get_response("What is this ?")
print(responce)