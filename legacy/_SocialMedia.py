import webbrowser

# keep in mind that it can also be used for the other queries like loggin into the particular websites.
# These all moduels are under progress,
# Development module will be started building after 30 november 2016, !

# TODO : Social Media Access like facebook , Instagram and others
class SocialMedia:
    def __int__ (self):
        print("This is the Constructor of the class Social media")

    def email_access (self):
        print("")

    # The below function will be used regerding to the twitter accessing and stuff
    def twitter_access (self):
        print("Granting the twitter Access")

    # The below function will be used for the messaging and getting the messages from the facebook

    def Messenger_access (self):
        print("MESSEBGER ACCESS FOR SENDING AND RECIEVING MESSSAGES")

    # The below function will be used to access the facebook and all the stuff.


    def facebook_access (self):
        print("FACEBOOK Access for accessing and recieving facebook messages")

    # This will be used to access the instagram, so that you can access the current features

    def instagram_access (self):
        print("Granting the instagram Access and checking")

    # This function will be used to access the social medias and choose the correct social media for the particular stuff.

    # keep in mind that it can also be used for the other queries like loggin into the particular websites.
    def social_media_access (self, browse_key=""):
        print("SOCIAL MEDIA DETECTED")  # This will be used for the debugging purposes
        if browse_key != "":
            if browse_key == 'facebook':
                print("Browsing Facebook")
                webbrowser.open("www.facebook.com")
            elif browse_key == 'twitter':
                print("Browsing twitter")
                webbrowser.open("www.twitter.com")
            elif 'linkedin' == browse_key:
                print("Browsing linkedin")
                webbrowser.open("www.linkedin.com")
            elif browse_key == 'instagram':
                print("Browsing Instagram")
                webbrowser.open("www.instagram.com")
            elif browse_key == 'reddit':
                print("Browsing Reddit")
                webbrowser.open("www.reddit.com")

