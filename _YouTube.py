import webbrowser
# TODO  : Use youtube api , instead of the static Youtube References
class YouTubeSearch:
    def __init__ (self):
        pass

    def search (self, search_text=''):
        search_text = search_text.strip()
        search_text = search_text.replace(' ', '+')  # This replaces the spaces with the + sign
        search_url = "https://www.youtube.com/results?search_query=" + search_text
        webbrowser.open(search_url)  # this opens the url on the webbrowser

