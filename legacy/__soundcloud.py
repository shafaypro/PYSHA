import webbrowser
import soundcloud
def SoundCloudSearch(text):
    text = str(text).replace(' ',"%20")
    search_link = "https://soundcloud.com/search?q=" + text
    print(search_link)
    webbrowser.open(search_link)
class SoundCloudApi:
    client_id  = ""
    cliend_secreat = ""
    redirect_url = ""
    def __init__(self):
        client = soundcloud.Client(client_id=self.client_id,client_secret = self.cliend_secreat,redirect_url = self.redirect_url)
#if __name__ === '__main__':
#    SoundCloudSearch("Eminem Yourself")