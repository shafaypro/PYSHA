# import fb
# import facebook
try:
    from facepy import GraphAPI  # For posting the facebook status we use the facepy module
    # import fbchat # imports the facebook chat module for chatting and sending messages.
except Exception as E:
    print("please install the Package facepy")
'''class FaceBookPysha:
    token = "" # This is an empty token
    fb_obj = None
    def __init__(self, token):
        self.token = token
        self.fb_obj = fb.graph_api(self.token)
    # The below Function recieved the Message and post it on the user wall
    def post_status(self,message_input="Hello World!"):
        self.fb_obj.publish(cat="feed",id="me",message = message_input)
    def del_status(self,status_id):
        self.fb_obj.delete(id = status_id) # Deleting the specified status.
        
class FB:
    # The class takes AT as Access tokens
    graph = None
    def __init__(self,AT = ""):
        try:
            graph = facebook.GraphAPI(access_token = AT,version = "2.2")
            self.graph = graph
            return self.graph
            # Creating the graph object by providing hte access tokens
            # THe graph objects will be through Graph API.
        except Exception as e:
            print("Unable to connect to the graph api",e)
    def post_status(self,status_message = "Hellow World"):
        self.graph.put_object("me", "feed", message=status_message)
        # Putting the graph object to put in the messages.
'''


class FB:
    graph = None

    def __init__(self):
        AT = "EAAaaMaJUE7MBAMcsfGrTwm8wxSUJN9ZBYBxbaN4IGGZByYR8fY8IkWcS8ZB1nckEWQFcZA046n4qKqEJOZCpZANwuXfnL9lg3tiNQyLNoDVhdZCd9RhwZCvqgD9rrJ6P6TYzZCTIzsydPZAjBydgvak10w476dCwcyPKBwyY12yTs5WWJszUZC9YiEAco14pZBhZCJBQZD"
        self.graph = GraphAPI(AT)

    def post_status(self, message):
        try:
            self.graph.post(path="me/feed", message=message)  # posting the message
            return True
        except Exception as E:
            print(E)
            return False

    def send_message(self):
        pass

    def check_messages(self):
        pass  # this will check the messages which have to be passed.

# AT = "EAAaaMaJUE7MBAHiLyWgofHroiPzRs6MB0j8LRewqxAnGycE0H6DntVA4G8qRDAwdVAje5ysyfofs4qJ8JtSrxbBMJ83PpKkqTJJJw
# CbGsowfQP0UrG5vHMZBvZA6bVbkjyPSx1hm2hyJAehK6blCC95yL5yF4eYuMZAFpMNYdrNY7WVEBoW19y2fBKWlfd3gPSR6LNxjgZDZD"
# graph = GraphAPI(AT)
# status_message = " testing Facebook access test 2: Access my all pictures . No,  You are UGLY"
# graph.post(path = "me/feed", message=status_message)
# print("All is done mate")

# below is the code for hte 
# fb = FB()
# fb.post_status("Pysha facebook headerfile testing ")
