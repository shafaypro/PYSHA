import webbrowser
from bs4 import BeautifulSoup
import urllib


# Stack over flow code and checking
# ToDO: You can improve the Search using the OAUTH and other apis of the stack over flow

class StackoverFlow:
    def __init__ (self):
        pass

    def search (self, search_text=''):
        search_text = search_text.strip()
        search_text = search_text.replace(' ', '+')  # This replaces the spaces with the + sign
        search_url = "http://stackoverflow.com/search?q=" + search_text
        self.scrap_tool(search_url)  # Passing the url for the searching
        webbrowser.open(search_url)
        return search_url  # returns the search url for the reading purposes
        # need to work with the api instead of the static referring

    def scrap_tool (self, inner_link):
        read_url = urllib.request.urlopen(inner_link).read()
        beautiful_source = BeautifulSoup(read_url)
        for _ in beautiful_source.find_all('div', {'class': 'result-link'}):
            print(_)


            # if __name__ == '__main__':
            # sf = StackoverFlow()
            # sf.search('Python 5')
