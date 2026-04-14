import urllib.request
import urllib  # importing the urllub
'''basic Image scrapping for the Pysha Virtual Assistant '''
class __ImageShower:

    def __init__(self):
        pass

    def get_image(self, query):
        query = query.lower()
        query = str(query).replace(" ", "+")  # replacing the space with the plus
        url = "www.imgur.com/search?q="+query  # Creating the url of the search string .
        requested_data = urllib.request.urlopen(url,"html.parser").read()  # reading the data
        print(requested_data)
        pass



if __name__ == '__main__':
    IS = __ImageShower()
    IS.get_image("Hope is a mistake")