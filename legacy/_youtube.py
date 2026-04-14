try:
    import webbrowser
    import urllib.request  # library for the importing
    from bs4 import BeautifulSoup  # --web beautify and finding
    import sqlite3
    import pafy  # This wont work in Proxy server which block youtube
    from _dbdata import *  # importing the database for storing the youtube table
    # Youtube search based on the webbrowser links
    # ToDo: Use the youtube api rather than using the the web browser
except Exception as E:
    print("Header file (module ) needs to be installed ",E) # Debugging

class YouTubeSearch:
    def __init__(self):
        self.db = db_data()  # creating the database connetion so that it can be connected

    def search(self, search_text='', play_list=False):
        search_text = search_text.strip()
        search_text = search_text.replace(' ', '+')  # This replaces the spaces with the + sign
        search_url = "https://www.youtube.com/results?search_query=" + search_text
        if not play_list:
            found_link_list = self.scrap_link(
                search_url)  # calling the search url function to start scrapping the scripts.

            # This is the insertion of the youtube list in the database
            # Inserting of the play list and the other should be of the simple link
            self.insert_into_youtube(search_text,search_url, str(found_link_list))
            webbrowser.open(found_link_list[0])  # this opens the url on the webbrowser , first weblink
            try:
                self.video_description_info(found_link_list[0])  # getting the description for the foundlink
            except Exception as E:
                print("Couldn't get the description : ", E)
            return search_url  # This returns the link, which has to be returned in order to be read in the next phase

        elif play_list:
            found_playlink_list = self.scrap_playlist(search_url)  # A list of play lists
            self.insert_into_youtube(search_text, search_url, str(found_playlink_list))
            # We are inserting the list of the found playlist.
            print(found_playlink_list[0])
            webbrowser.open(found_playlink_list[0])  # opening the first play list as per specified

            return search_url  # returning the found URl , so that it can identify the stuff

    '''FOR SCRAPPING THE VIDEOS LINK FROM THIS FUNCTION USE SIMPLE THIS, IT RETURNS THE LIST OF LINKS'''

    def scrap_link(self, link):
        requested_html = urllib.request.urlopen(link).read()  # reading the code
        Beautified_code = BeautifulSoup(requested_html, "html.parser")  # getting the html parser in a right way
        list_youtube_videos = list()
        for _ in Beautified_code.find_all('h3', {'class': 'yt-lockup-title'}):  # replace the search query here
            list_youtube_videos.append("https://www.youtube.com" + str(
                _.a["href"]))  # Creating the name youtube link list and appending the list terms
            print("https://www.youtube.com" + str(_.a["href"]))
        return list_youtube_videos

    ''' For SCRAPPING THE PLAY LIST FROM THE YOUTUBE USE THIS FUNCTION'''

    def scrap_playlist(self, link):
        requested_html = urllib.request.urlopen(link).read()  # reading the code
        Beautified_code = BeautifulSoup(requested_html, "html.parser")  # getting the html parser in a right way
        list_youtube_playlists = list()
        for _ in Beautified_code.find_all('h3', {'class': 'yt-lockup-title'}):  # replace the search query here
            if str(_.a["href"]).__contains__("list=PL"):
                list_youtube_playlists.append("https://www.youtube.com" + str(
                    _.a["href"]))  # Creating the name youtube link list and appending the list terms
                print("https://www.youtube.com" + str(_.a["href"]))
        return list_youtube_playlists

    ''' Inserting into database for the youtube to implement machine learning for later onwards'''
    # TODO: make the database more efficent
    def insert_into_youtube(self, Y_Requested_string="", Y_requested_url="", Y_Responce_List=""):
        self.db.insert_into_youtube(Y_Requested_string, Y_requested_url, Y_Responce_List)
    ''' To Insert in to  database which will be later used to '''

    ''' Downloading the video description from youtube and others.'''
    @staticmethod
    def video_description_info(self, link=""):
        if link != "":
            # If there is no linkd spedcified than the data will not be displayed
            video_required = pafy.new(link)  # getting the link from the youtube
            print(video_required.title)  # Title of the video
            print(video_required.duration)  # Duration of the video
            print(video_required.rating)  # Rating of the video
            print(video_required.author)  # Author of the video
            print(video_required.length)  # length of the video
            print(video_required.keywords)  # keywords in the video
            print(video_required.thumb)  # How much likes
            print(video_required.videoid)  # What is the current video id
            print(video_required.viewcount)  # How much views has this youtube video
            return
        return

''' TO CHECK THIS FILE USE THE BELOW CODE SO THAT IT CAN RUN THE VIDEOS AND GO THROUGH IT'''
# YTS = YouTubeSearch()
# YTS.insert_into_youtube('HELLO','www.youtube.com/whatthevuk ', '[WWW.youtube.com]')
# inserting the dummy databse in the data so that the data can be added .!
# # check_list = YTS.scrap_playlist("https://www.youtube.com/results?search_query=python+tutorial")
