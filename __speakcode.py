import pyttsx # this is the Pyttsx application running module for the text to speech.
from bs4 import BeautifulSoup
import re
import urllib.request
class WebReader_PYSHA:
    def read_web_text_list(self,text_list):
        engine = pyttsx.init()  # initializing the pyttsx
        for line in text_list:  # looping through the lines
            engine.say(line) # engine is saying the line
            engine.runAndWait() # Running the engine
    def read_web_text(self,text):
        engine = pyttsx.init()  # initializing the pyttsx
        engine.say(text) # letting the engine say :P
        engine.runAndWait() # running and waiting
    def send_file_lines(self,filename):
        try:
            if str(filename).endswith('.txt'):
                text_to_read = open(str(filename),"r").readlines()
                self.read_web_text(text_to_read) # this calls the read function which will read te provided lines
            else:  # going to the else condition
                print("invalid file name")  # if you have an invalid file name
        except Exception as E:  # printing the exception as E
            print("There is an error checking the scrapped file hence you are required to rerun the file")
class WebScrap:
    def __init__(self):
        print("WebScrap object has been created ")
    def scrap_link(self, link):
        request_url_object = urllib.request.urlopen(link)  # link object
        request_read_code = request_url_object.read()  # link readable code
        Beautified_soup  = BeautifulSoup(request_read_code,"html.parser")  # parsing using the beautiful soup
        #texts = Beautified_code.findAll(text=True) # those who have he text true
        #[s.extract() for s  in Beautified_soup(['style', 'script', '[document]', 'head', 'title'])]
        # [s.extract() for s in BeautifulSoup(['p'])]
        # visible_text = Beautified_soup.getText()
        # #splited_list  = visible_text.split("\\n")
        # split_list = visible_text.split("\\n")
        for script in Beautified_soup(["script",'[document]', 'head', 'title', "style"]):  # to remove all the scripts from the required page.
            script.extract()    # rip it out

        # get text
        text = Beautified_soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = [chunk for chunk in chunks if chunk]
        filtered_text = [T for T in text if len(T)>50]
        print(filtered_text)
        #print(text)
        # for l in text:
        #     if l.startswith("'b"):
        #         l = l.replace("'b", '')
        #     else:
        #         pass
        #     print(l)
        WRP  = WebReader_PYSHA()
        WRP.read_web_text_list(filtered_text)
        # # # for line in splited_list:
        #     if line.strip() == "":
        #         pass
        #     else:
        #         print(line.strip())
    def visible(element):
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
            return False
        elif re.match('<!--.*-->', str(element)):
            return False
        return True




if __name__ == '__main__':
    WS = WebScrap()
    WS.scrap_link("http://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text")

