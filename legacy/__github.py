import webbrowser


class GitHubSearch:
    def __init__(self):
        print("Github Intialized")

    def search(self, text):
        text = str(text).replace(" ", "+")
        search_link = "https://github.com/search?utf8=%E2%9C%93&q="+text
        webbrowser.open(search_link)
        return search_link  # this returns the search link created
