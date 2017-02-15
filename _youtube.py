import webbrowser

# Youtube search based on the webbrowser links
# ToDo: Use the youtube api rather than using the the web browser
class YouTubeSearch:
    def __init__ (self):
        pass

    def search (self, search_text=''):
        search_text = search_text.strip()
        search_text = search_text.replace(' ', '+')  # This replaces the spaces with the + sign
        search_url = "https://www.youtube.com/results?search_query=" + search_text
        webbrowser.open(search_url)  # this opens the url on the webbrowser
        return search_url  # This returns the link, which has to be returned in order to be read in the next phase
