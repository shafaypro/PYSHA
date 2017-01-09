import webbrowser
# ToDO: You can improve the Search using the OAUTH and other apis of the stack over flow
class StackoverFlow:
    def __init__ (self):
        pass

    def search (self, search_text=''):
        search_text = search_text.strip()
        search_text = search_text.replace(' ', '+')  # This replaces the spaces with the + sign
        search_url = "http://stackoverflow.com/search?q=" + search_text
        webbrowser.open(search_url)
        #need to work with the api instead of the static referring