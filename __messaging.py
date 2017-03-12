import fbchat
credential_read = [line.strip() for line in open("E:\\Credentials.txt", "r").readlines()]
user_name,user_pw = credential_read[0],credential_read[1]
print(user_name)
print(user_pw)
try:
    Client = fbchat.Client(user_name, user_pw) # Creating the client on the basis of user name and the user password
except Exception:
    print("unable to create a client, Communication not possible") # Creating the exception
    exit(0)

friends = Client.getUsers("Salman AbdulKarim")  # input the name of the friend you want to sent the text to
friend = friends[0] # getting the 0th element from the friends list

sent = Client.send(friend.uid, "PYSHA TESTING : 1 Messaging")
if sent:
    print("Message have been sent Successfully")
    exit(0)
