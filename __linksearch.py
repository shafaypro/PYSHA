from google import search  # importing the search module from google
import webbrowser


def search_first_link(input_query):
    for url in search(input_query):
        print(url)
        webbrowser.open(url)
        break
