import webbrowser
import urllib.request  # library for the importing
from bs4 import BeautifulSoup # --web beautify and finding

# Youtube search based on the webbrowser links
# ToDo: Use the youtube api rather than using the the web browser
class YouTubeSearch:
    def __init__ (self):
        pass

    def search (self, search_text=''):
        search_text = search_text.strip()
        search_text = search_text.replace(' ', '+')  # This replaces the spaces with the + sign
        search_url = "https://www.youtube.com/results?search_query=" + search_text
        found_link_list = self.scrap_link(search_url) # calling the search url function to start scrapping the scripts.
        webbrowser.open(found_link_list[0])  # this opens the url on the webbrowser , first weblink
        return search_url  # This returns the link, which has to be returned in order to be read in the next phase
    '''FOR SCRAPPING THE VIDEOS LINK FROM THIS FUNCTION USE SIMPLE THIS, IT RETURNS THE LIST OF LINKS'''
    def scrap_link(self,link):
        requested_html = urllib.request.urlopen(link).read() # reading the code
        Beautified_code = BeautifulSoup(requested_html,"html.parser")  # getting the html parser in a right way
        list_youtube_videos = list()
        for _ in Beautified_code.find_all('h3',{'class':'yt-lockup-title'}):  # replace the search query here
            list_youtube_videos.append("https://www.youtube.com"+str(_.a["href"]))  # Creating the name youtube link list and appending the list terms
            print("https://www.youtube.com"+str(_.a["href"]))
        return list_youtube_videos
    ''' For SCRAPPING THE PLAY LIST FROM THE YOUTUBE USE THIS FUNCTION'''
    def scrap_playlist(self,link):
        requested_html = urllib.request.urlopen(link).read() # reading the code
        Beautified_code = BeautifulSoup(requested_html,"html.parser")  # getting the html parser in a right way
        list_youtube_playlists = list()
        for _ in Beautified_code.find_all('h3',{'class':'yt-lockup-title'}):  # replace the search query here
            if str(_.a["href"]).__contains__("list=PL"):
                list_youtube_playlists.append("https://www.youtube.com"+str(_.a["href"]))  # Creating the name youtube link list and appending the list terms
                print("https://www.youtube.com"+str(_.a["href"]))
        return list_youtube_playlists


''' TO CHECK THIS FILE USE THE BELOW CODE SO THAT IT CAN RUN THE VIDEOS AND GO THROUGH IT'''
# YTS = YouTubeSearch()
# check_list = YTS.scrap_playlist("https://www.youtube.com/results?search_query=python+tutorial")
