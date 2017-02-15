import datetime  # Importing the datetime for the timing modules since the date time is used to answer the questions
import time
import urllib.request  # importing the url pacakage for the
import wave  # Importing the wave of for the recording(This is the format for the recording which is used .wav
import webbrowser
from random import *  # Using the random  function for the creation
import pyaudio  # importing the header file of the pyaudio
import speech_recognition as sr  # Importing the speech recognition file for the code.!!
import tweepy
from bs4 import BeautifulSoup  # importing the beautiful soup package
from PYSHA.PygletMusic.Pygletimplementation import *  # Music player GUI implemented
from PYSHA._Joke import *
from PYSHA._NaturalLanguageProcessing import *
from PYSHA._WolFrameAlphaClass import *
from PYSHA.__soundcloud import *
from PYSHA.__speakcode import *  # For speaking the code from the web scrapping .
from PYSHA._dbdata import *  # Database function for the request and all others
from PYSHA._stackoverflow import * # Stackoverflow pysha module beeing imported
from PYSHA._twitter import * # imports the twitter Pysha client which has been
from PYSHA._weatherchecking import *
from PYSHA._youtube import *
from PYSHA.__github import *
from facepy import GraphAPI
import facebook

# this si the importing of the header files !
# Pre requirements : You need to Install Microsoft SDK fo Speech and all the available Tools
# Keep in mind that This is Under Heavy Construction and will be used in the later increments and

'''
// This build is heavily under progress by Muhammad Shafay Amjad, If you want to check all the dependencies,
and want to contribute to improve the particular algorithm, check Repository.
https://github.com/shafaypro/PYSHA1.0
Info Dated: 23/12/2016  , WaterFall method is being Followed

User Guideline:

Wherever you run this Project, the basic dependencies are converted in to the local machine,

--> The machine tells about her self and then wait for the user to have the specified an speech input,

The device of the microphone is connected and then it is parsed to the pyaudio where the input is then

Converted to the Audio file  Formatted as WAV, under the F.L.A.C encoding, then it is parsed to the google api,

since the api is then accessed and the chunks of the audio is converted into the string and then returned into the string.

There are some already stored procedures for the particular messages , like if a message starts from the :::

Search for <--- This opens up the browser for the result so that the Virtual assistant is able to read from the data!!!

Stop,stop listening,quit <---- This will results in the Quiting , exiting for the virtual assistant!!

search ________ on Wikipedia : will search on wikipedia based on certain meaningful words(replaces at _____)

what is the ----> Time, Date and others can tell you the the time ,date and others.
Ther are some other features also added in the header file , like haviing a random chat and working on different kind of
Loops

you can ask for the questions and the Answers regarding to the Natural language processing module .

If you want to ask for the Application running modules then
for that :
RUN or OPEN _________ the Underscore should be replaced by the application name
--> This script will also be monitroing the computer (Here it contains the data analysis and the data visualization part
This will be including the statistical analysis and well as the sentimental analysis . ! so that this may be used in the later
sequences of the version
--> ask for any operation ,, if other than all of the above , it will
--> You can ask the Mathematical operation as : 2+ 3 or integeration of 4 or General Knowledge.
--> Since It can also be asked the general knowledge questions like : who was the  6th president of Unitedstates


!!!!!!!!!!!!!!!!!!!!!!!EXAMPLE QUESTIONS !!!!!!!!!!!!!!!!!!!!!!!!
Who won the Election of 2016 in United states ?
Who wrote the book The lord of the Flies ?
What is the meaning of life ?
What is the meaning of Nostalgia?
bread <-- This will return the Other Requirements


--------------------------Example Programming Solution-----------------------
ask --> Stack over flow search _____________
______ replace this with your query
ask--> search youtube ____________ or youtube _________________
search youtube ___________________
______ replace this with your query
or youtube ___________________

ask--> search music _____________ or find music _______________
_________ replace this with your song name of artist or any :p

ask--> Read it out to me      or Read it out for me
# This will read all the text from the last visited page
'''

''' Keep in mind to have all the back up things,
For the personal computer you need to have the computer access,
And all the other things given to the Assistant so that it can work in there.
'''

# TODO : USE THE IBM WATSON TOO, To improve the Virtual Assistant
__author__ = "M Shafay Amjad"
__QA__ = "mshafayamjad@gmail.com"
__version__ = 1.0
__productname__ = "PYSHA"
# TODO : File Information needs to be implemented


# The reverse shell process is for personal use, where we will be using to ping the Updated Code, to your Home location
# Computer Code!
'''
This is the personal Computer Reverse shell!
'''


class PYSHA_CLASS:
    db = NONE
    lastlink = ""  # just to be reminded for the last link visited

    def __init__ (self):

        print("PYSHA INITIALIZED!")
        self.createlocaldb()  # this creates the localdb for requests

    # creating the local Database
    def createlocaldb (self):
        self.db = db_data()  # this calls the db class
        self.db.create_database()  # this creates the database for the class.

    # TODO : more Accurate apps running
    # for going through the history


    def insert_into_request (self, request_text,
                             responce_text):  # this is the function responsible for the writing in the history.
        self.db.insert_into_Requests(request_text, responce_text)  # this is wrigint into the reposnce text

    # For running the apps
    def run_apps (self, text_input=""):
        if text_input != "":
            if text_input == "calculator":
                os.system('calc.exe')  # Running the calculator in the Operating system
                self.text_to_speech("Calculator launched")
            elif text_input == "notepad":
                os.system('notepad.exe')  # Running the notepad using the Os module for the spoecified Atrtirbuote !
                self.text_to_speech("notepad launched")
            elif text_input == "performance monitor":
                os.system('perfmon.exe')  # Launchign the Performance monitor from the exe
                self.text_to_speech("Performance monitor has been launched")
            elif text_input == "smart screen":
                os.system('smartscreen.exe')  # Working on the smart screen and running the Exe !
                self.text_to_speech("smart screen launched ")
            elif text_input == "space agent":
                os.system('SpaceAgent.exe')  # Running the space agent for the
                self.text_to_speech("space agent has been launched")
            elif text_input == "network status":
                os.system('netstat.exe')  # you are working ehre !
                self.text_to_speech("Network status for today have been shown in the screen")
                self.text_to_speech("somethings seems to be off")
            elif text_input == "bluetooth setting":
                os.system('fsquirt.exe')  # you are working ehre !
            elif text_input == "defragment":
                os.system('Defrag.exe')  # you are working ehre !
            elif text_input == 'clean manager':
                os.system("cleanmgr.exe")
            elif text_input == "command prompt":
                os.system("cmd.exe")
            elif text_input == 'direct ex' or text_input == 'direct setting':
                os.system("dxdiag.exe")
            elif text_input == "control panel":
                os.system('control.exe')
            elif text_input == 'resource monitor':
                os.system('resmon.exe')  # this laucnhed the resource monitor to onitor the resourcr!!es of the comput
            elif text_input == "game panel":
                os.system('GamePanel.exe')
            elif text_input == 'graphic settings':
                os.system('Gfxv4_0.exe')  # this access the graphic cards
            elif text_input == 'dpi scaling':
                os.system('DipScaling.exe')  # this truns the dpi scalling for the partu
            elif text_input == 'disk partition':
                os.system('diskpart.exe')
            elif text_input == 'python' or text_input == "python interpreter":
                os.startfile(
                    "C:\\Users\\Programmer\\AppData\\Local\\Programs\\Python\\Python35\\pythonw.exe")  # this calls the file location and then run the program of the python.
                # There you should run the pyton programming language so that the language will be specified by the face of the
            elif text_input == "pycharm" or text_input == "python best interpreter":
                os.startfile("C:\\Program Files (x86)\\JetBrains\\PyCharm 5.0.4\\bin\\pycharm.exe")
                # --- This runs the pycharm Compiler which can be used for the Html or the python programming
                # The Below function will be used to search on the browser and then show the desire result
            elif text_input == "movie player":
                print("started movie player!!!")
                os.startfile(
                    "C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe")  # window media player execution!

    # TODO : Exact Searching
    def search_browser (self, text_input):
        print('-searching on browser-')
        try:
            url = 'http://google.com/search?q=' + text_input  # Creating or generating a google link for the particular file
            webbrowser.open(url)
            return

        except:
            self.text_to_speech(
                "I'm sorry, I couldn't reach google")  # Calling the Function so that it can be identified that ,machine can speaks for itself
            return

    # The below function is responsible for the search on the wikipedia.

    # searching on the wikipedia and then asking the pysha to speak the respectable result!!

    # TODO : WIkI Algorithum improvment
    def search_wiki (self, text_input):
        # suggested_string = wikipedia.suggest(text_input)  # now going for the suggestion
        try:
            wiki_page = wikipedia.page(text_input)  # this opens up the wiki page for the particular thing
            # text_to_speech(str(wiki_page.title))  # asking the machine to speak this specified word
            # summary_text = wikipedia.summary(text_input, sentences=4)  # search on the wikipedia!
            wiki_link = str(wiki_page.url)  # Converts the url of the wiki links to the url.
            wiki_images = wiki_page.images  # Gets all the images link references. as a list
            wiki_sumry = wikipedia.summary(text_input, sentences=3)

            print(wiki_sumry)
            # webbrowser.open(wiki_link)  # opens the link on the web browser and then search the specified text link
            self.text_to_speech(wiki_sumry)
            return wiki_link  # this returns the wikilink , keep in mind this is just for reading in the later onward purposes
        except:
            self.text_to_speech(
                "Sorry i couldn't connect to the wikipedia!! nor find a relevant link, there must be a connection problem")
            return

    # The below function is responsible for the running of the chat with the below function
    # This will be used to show the Frontend for the application.

    # There are two dynamic ways for storing the Frontend , since this is a Hit and run trail using the function!
    # The Human computer interaction will be updated according to the software development module!

    # TODO: Frontend HCI needs to be created !
    def frontend_hci (self, label_text):
        root = Tk()  # This created the tkinter , face.!
        root.title("PYSHA 1.0")  # Making the Title for the Py Sha 1.0 ,
        root.geometry("300x300")  # specifying the x and the y axis in the scenario
        label1 = Label(root, text=label_text, font='size,25')  # This is the label insertion for the Tkinter module
        print(label1)  # Showing in the console for the debuggin purposes
        label1.pack()  # Packing up the label1 module in the GUI
        root.after(10000, lambda: root.destroy())  # Destroying after 10 seconds
        root.mainloop()  # Executing the main loop for the Gui Till it gets exited

    # TODO : make the Chat intelligent , using the Natural language processing and AIML (artifical intelligence markup language)
    def chat (self, input):
        insults = ["weirdo", "stupid", "weird", "dumb", "idiot", "retard", "retarded", "fat", "lazy",
                   "annoying", "moron", "simp", "big", "ugly", "sad", "wimp", "troll"]
        complements = ["nice", "happy", "good", "smart", "wonderful", "really ", "intellegent", "awesome", "beautiful"]
        ranNum = randrange(1, 4)
        # chatting features of PyDa:
        if input.startswith("do you want to "):
            if ranNum == 1:
                self.text_to_speech("Maybe later")
            if ranNum == 2:
                self.text_to_speech("I don't think that's a good idea")
            if ranNum == 3:
                self.text_to_speech("Yes! lets do it")

        if input.startswith("do you like to "):
            if ranNum == 1:
                self.text_to_speech("Sometimes I do")
            if ranNum == 2:
                self.text_to_speech("No, I hate doing that")
            if ranNum == 3:
                self.text_to_speech("Yes, I do that all the time")

        if input.startswith("i hate "):
            if "Shafay" in input[6:]:
                self.text_to_speech("What? Shafay is the coolest person ever!")
            elif ranNum > 2:
                self.text_to_speech("I think " + input[6:] + " is awesome")
            elif ranNum <= 2:
                self.text_to_speech("I don't like " + input[6:] + ' either')

        words = input.split

        if input.startswith("you are a"):
            if any(input[10:].startswith(c) for c in complements):
                if ranNum == 1:
                    self.text_to_speech("Thank you, I know")
                if ranNum == 2:
                    self.text_to_speech("isn't it obvious?")
                if ranNum == 3:
                    self.text_to_speech("you made my day!")
            elif any(input[11:].startswith(c) for c in complements):
                if ranNum == 1:
                    self.text_to_speech("Thank you, I know")
                if ranNum == 2:
                    self.text_to_speech("isn't it obvious?")
                if ranNum == 3:
                    self.text_to_speech("you made my day!")

            if any(input[10:].startswith(i) for i in insults):
                if ranNum == 1:
                    self.text_to_speech("I know you are but what am i?")
                if ranNum == 2:
                    self.text_to_speech("Don't troll me. bad things will happen")
                if ranNum == 3:
                    self.text_to_speech("sorry, i was to busy, BLOCKING OUT THE HATERS!")
            elif any(input[11:].startswith(i) for i in insults):
                if ranNum == 1:
                    self.text_to_speech("I know you are but what am i?")
                if ranNum == 2:
                    self.text_to_speech("Don't troll me. bad things will happen")
                if ranNum == 3:
                    self.text_to_speech("sorry, i was to busy, BLOCKING OUT THE HATERS!")

            elif input[10:] or input[11:] not in insults:
                if ranNum == 1:
                    self.text_to_speech("I don't know what you mean by that")
                if ranNum == 2:
                    self.text_to_speech("Your words are not in my library")
                if ranNum == 3:
                    self.text_to_speech("No comment")
            elif input[10:] or input[11:] not in complements:
                if ranNum == 1:
                    self.text_to_speech("I don't know what you mean by that")
                if ranNum == 2:
                    self.text_to_speech("Your words are not in my library")
                if ranNum == 3:
                    self.text_to_speech("No comment")

        if input.startswith("are you a"):
            if any(input[10:].startswith(c) for c in complements):
                if ranNum == 1:
                    self.text_to_speech("yes i am")
                if ranNum == 2:
                    self.text_to_speech("isn't it obvious?")
                if ranNum == 3:
                    self.text_to_speech("you betcha")
            elif any(input[11:].startswith(c) for c in complements):
                if ranNum == 1:
                    self.text_to_speech("yes i am")
                if ranNum == 2:
                    self.text_to_speech("isn't it obvious?")
                if ranNum == 3:
                    self.text_to_speech("you betcha")

            if any(input[10:].startswith(i) for i in insults):
                if ranNum == 1:
                    self.text_to_speech("no, are you")
                if ranNum == 2:
                    self.text_to_speech("don't troll me, i eat trolls")
                if ranNum == 3:
                    self.text_to_speech("does it look like i am?")
            elif any(input[11:].startswith(i) for i in insults):
                if ranNum == 1:
                    self.text_to_speech("no, are you")
                if ranNum == 2:
                    self.text_to_speech("don't troll me, i eat trolls")
                if ranNum == 3:
                    self.text_to_speech("does it look like i am?")

            elif input[10:] or input[11:] not in insults or complements:
                if ranNum == 1:
                    self.text_to_speech("I don't know what you mean by that")
                if ranNum == 2:
                    self.text_to_speech("Your words are not in my library")
                if ranNum == 3:
                    self.text_to_speech("No comment")

    # if there is any person question regarding to the Virtual Assistant go for this

    # When there is a question regarding to the self , Like the questions given to the Pysha, or the personal question about her !
    # Since , The below Function is an already stored function by the developer, there are some processed required like
    # Machine learning should be implemented in here too, for the particular specific questions
    # TODO : Do some of the Complex parsing
    def Personal_PYSHA (self, text_input=""):
        if text_input == "name":
            self.text_to_speech("PYSHA")
            return
        elif text_input == "age":
            b_date = datetime.date(2016, 10, 24)  # specifing the creation date.
            c_date = datetime.date.today()
            # now subtract the date from the date of creation
            self.text_to_speech(
                (c_date - b_date))  # this prints the age of the Virtual Assistant , which returns the date.
            print((c_date - b_date))
            return
            # Here you need to add the hob
        elif text_input == "hobbies":
            self.text_to_speech("Well i have many hobbies, i will tell you some")
            hobbies = ["Playing a Game", "Collecting your History", "Watching Football"]
            for each_hobby in hobbies:  # Iterating to each of the loops
                self.text_to_speech(str(each_hobby))  # Sending the each string to the Hobbies.
                # This will send all the related hobbies to the specified Place.
        elif text_input == "gender":
            self.text_to_speech("Female")

    # this is the particular day check , that the user will be defining the day check ,since the day
    #  Follows the same day check priciple for the  particular day check<!

    # TODO NOTHING
    def day_check (self):
        current_date = datetime.datetime.now()
        self.text_to_speech("The current date is " + str(current_date.date()))
        return

    # Checking the time for the computer while the

    # IF the user asked for the particular time check , after the text processing this function is called ! ,
    # This later calls the text to speech function using the P.y.t.t.s.x. for the user to speak the particular output !
    # TODO : Nothing
    def time_check (self):
        current_time = time.strftime('%H:%M:%S')
        self.text_to_speech("The time is " + current_time)
        return

    # storing the respectable input for the user  while the computer will be able to use the resources and speak

    # TODO: add sqlite3 database and store the input in the form of the data base
    def store_userinput (self, input_check):
        self.db.insert_into_History(str(input_check))  # this stores and creates a history
        file_out = open("USERINPUT.txt", "a")
        file_out.writelines("USER SAID: \t" + input_check)
        file_out.write("\n")  # ending the line with the next line
        file_out.close()
        return
        # This function will be responsible for storing the responses so that it may able to answer in the future.pute

    # Converting the spoken string to the speech , so that the call is Visible

    # TODO : speech to Text   (Google api, Microsoft Speech recording )
    def speech_to_text (self):
        client_id = ""  # this is the google api client id
        client_secret = ""  # this is the google api client secret key
        api_key = ""
        r = sr.Recognizer()
        with sr.Microphone() as source:
            CHUNK = 1024
            FORMAT = pyaudio.paInt16  # the Format is picked up from the pyaudio
            CHANNELS = 2  # The Cross Channels
            # RATE = 44100
            source.CHUNK = CHUNK
            source.format = FORMAT
            # print(dir(source))
            print("Say something!")
            print(r.energy_threshold)
            r.energy_threshold -= 80
            # print(r.adjust_for_ambient_noise(source,duration=1))
            audio = r.listen(source)

            # Speech recognition using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            # print(r.energy_threshold )
            # print(help(r.recognize_google))
            print("You said: " + r.recognize_google(audio, language='en-US'))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # if you want to record for the specific interval of time

    # The duration ins specified by the user, since the default value passed from the main funtion is 7 seconds,
    # since the short term memory duration is 5 +- 2 So , for the maximum iof seven seconds.!!!
    # TIps : Using the Wave , which is built by the microsoft
    def record_something (self, duration):
        # Below the Audio is accessed and then the audio is recorded and then converted in to text
        CHUNK = 1024  # Specifying the chunks for the recording
        FORMAT = pyaudio.paInt16  # the Format is picked up from the pyaudio
        CHANNELS = 2  # The Cross Channels
        RATE = 44100  # Bit rate , at which to record
        RECORD_SECONDS = duration  # Recording time duration for the computer
        WAVE_OUTPUT_FILENAME = "output.wav"  # Output file name as a string

        p = pyaudio.PyAudio()  # creating the Object and then calling the function of the PyAudio to access the audio

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)  # Creating the stream and specifing the access channels , and the rate, Input to be on.

        print("* recording, Ask me something!")  # Just a Message to tell the user that the Voice is being recorded

        frames = []  # A list of frame is created which is

        for i in range(0, int(
                                RATE / CHUNK * RECORD_SECONDS)):  # This is the Rate(bit rate) / Chuncks to be recorded * the Seconds
            data = stream.read(CHUNK)  # Reading the dat afrom the stream
            frames.append(data)  # Adding the each data to the frame list and appending it up.

        print("* done recording")
        print("Processing the input................")

        stream.stop_stream()  # Stopping the stream so that the stream(recorder for audio is stopped )
        stream.close()  # Clossing the stream of the audio
        p.terminate()  # Termination the Py AUDIO Module cause it was accesses

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')  # Accessing the WAV
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    #
    # Converting the text to speech using the pysha personal assistant and then specifing the input!
    '''  BELOW ARE THE FUNCTIONS FOR THE ENGINE change regarding to Text to Speech
    '''

    # Machine Speaking!
    def text_to_speech (self, text_input='HI! my name is PYSHA and i am your assistant'):
        engine = pyttsx.init()
        engine.say(text_input)
        engine.runAndWait()
        engine.stop()
        return

    ''' Ending of the functions of the system change regarding to the engine text speech
    '''

    # Checking the input of the speech to text so that the result can cbe picked up and then stored in the displat ..!!!

    # This function is responsible for the defining of the particular session and then recording the particular input, and working on the continuous
    # Recognition of the voice.!
    #TODO: Responsible for recording the audio in the wave format
    def speech_to_text_wav (self, file_to_recognize):
        r = sr.Recognizer()

        with sr.WavFile(str(file_to_recognize)) as source:  # use "test.wav" as the audio source
            audio = r.record(source)  # extract audio data from the file

        try:
            total_saying = r.recognize_google(audio)
            # if total_saying != "" or total_saying != NONE:
            #   text_to_speech("processing the audio")
            print("you said: " + total_saying)  # recognize speech using Google Speech Recognition
            # text_to_speech("You said ")
            # here i will be working on latter analysis
            total_saying = str(total_saying).lower()  # converting the total saying to the strings
            self.process_text_input(total_saying)

        except LookupError:  # speech is unintelligible
            print("Could not understand audio")
            self.text_to_speech("I Couldn't understand the audio")
        except sr.UnknownValueError:
            print("UNKNOWN!!")

    # The follwing function will be responsible for the text to be parsed regerding to the certain input.

    # keep in mind to use the natural language processing ,, www.pythonprogramming.org

    # The below function is responsible for the text prcessing of the Total syaing ,, since what the user i ssaying is recorded in this
    def process_text_input (self, total_saying=""):
        total_saying = total_saying.strip()  # Stripping the string for the extra white spaces
        total_saying = total_saying.lower()  # Converting a string to lower case
        if total_saying == "quit" or total_saying.lower() == "stop listening" or total_saying.lower() == "stop" or total_saying.lower() == "exit":
            self.store_userinput("quit")
            self.text_to_speech("BYE")
            os._exit(0)  # exiting the program
        else:
            # this stores the Specified Input we said Regerding to something
            # Textual_Analysis(total_saying)
            '''
                Below is the place where are your working on!!!

                '''
            if total_saying.__contains__("stop listenning both of you") or total_saying.__contains__(
                    "stop listenning Anna"):
                self.text_to_speech("ok ok I am turning myself off")
                exit(0)  # this exits the program, since we have stopped Anna from listenning
            if total_saying.startswith('search for') or total_saying.startswith('google'):
                self.text_to_speech("Opening a Browser For you.")
                self.total_saying = total_saying.replace("search for", "")
                self.total_saying = self.total_saying.replace("search", "")
                self.total_saying = self.total_saying.replace("on google", "")
                self.total_saying = self.total_saying.replace("google", "")
                self.store_userinput("Searching on Browser :" + self.total_saying)  # recording into database
                total_saying = total_saying.replace('search for',
                                                    '')  # Replacing the Search for with the total saying .
                total_saying = total_saying.replace('google', '')  # Replacing the Key word Googe with it
                self.search_browser(
                    text_input=self.total_saying)  # sending every remanining thing to the Browser to browse for
                self.text_to_speech("Browser Result have been displayed.")
            elif total_saying.startswith('social media'):
                self.store_userinput(total_saying)  # this stores the particular input.
                browse_key = total_saying.replace('social media',
                                                  '')  # Replacing the total saying variable value'd (social media with empty string)
                browse_key = browse_key.strip()
                sma = SocialMedia()  # Creating the social media object
                sma.social_media_access(
                    browse_key=browse_key)  # Passing the browser key to the social media access function.

            elif (total_saying.__contains__('wikipedia') and total_saying.startswith('search')) or (
                        total_saying.__contains__('on wikipedia') and total_saying.startswith('search')):
                total_saying = total_saying  # this converts the string to the lower case
                total_saying = total_saying.replace('search', '')  # replacing the start with the empty string
                total_saying = total_saying.replace('on wikipedia', '')  # replacing the on wikiepdia with empty string
                self.text_to_speech('Searching on Wikipedia')
                retrieved_link = self.search_wiki(
                    total_saying)  # calling the wikipedia search function , for the results
                self.lastlink = retrieved_link
                print(self.lastlink)
            elif total_saying.startswith("what is the date") or total_saying == 'date':
                # Here you will be required to input the date
                self.day_check()  # This calls the day check

            elif total_saying.startswith("what is the time") or total_saying == 'time':
                self.time_check()  # this checks the current time according to the specified state

            # Create a Grammer , that represents the questions regerding to the respectable machine

            elif total_saying.startswith("what is your"):
                # here you need to create the question saying file so that the file is readable.
                '''
                    Write the Respectable question in this format so that, the Agent learns from the file.

                    '''
                self.total_saying = total_saying.replace("what is your",
                                                         "")  # replacing the words so that it will be easier for the program to Check the last thing
                self.Personal_PYSHA(self.total_saying)

            elif total_saying.startswith("text mode"):
                tm = TextMode()  # this calls the text mode function, and there we can do the processing in the form of the text!
                tm.text_mode(total_saying)  # Passes the total saying to the Class Function!
            elif total_saying == "show me a comic":
                self.store_userinput("show me a comic")
                joke_object = Joke()  # creating an object of ht Joke class !
                self.text_to_speech("Finding a Comic the Database")
                joke_object.Image_Joke()  # Calls the Joke class Image Joke Object to show a Joke in the form of an image

            elif total_saying == "tell me a joke" or total_saying == "tell me another joke":
                print("JOKE JOKE JOKE!!!")
                self.store_userinput("tell me a joke")
                joke_object = Joke()
                self.text_to_speech("OH wait")
                joke_text = joke_object.joke_category()  # Calls any nerdy or Explicit joke about Chuck Norris.!
                # frontend_HCI(Joke_Text)  # calling the tkinter library to create the joke for the particular thing ,
                print(
                    joke_text)  # This is the Joke text , which will be printed in the console ,since we don't have much time , working for the Console.!
                self.text_to_speech(joke_text)  # Speaking up the joke (By machine ) PYSHA <3
            elif total_saying.startswith("open") or total_saying.startswith("run"):
                self.store_userinput(total_saying)  # This stores the Data in the Us
                # er input file so that the history is kept
                total_saying = total_saying.replace('open ', '')  # replacing the word open with the Total_saying!
                total_saying = total_saying.replace('run ', '')  # This is the replacement of the run with the
                self.run_apps(total_saying)  # This is the total saying being passed to the Running apps. !
            elif total_saying.startswith('parse sentence') or total_saying.startswith(
                    'parse this') or total_saying.startswith('tokenize this'):
                self.store_userinput(total_saying)
                total_saying = total_saying.replace('tokenize this', '')
                total_saying = total_saying.replace('parse sentence',
                                                    '')  # replacing the total saying with the parse sentence
                self.total_saying = total_saying.replace('parse this',
                                                         '')  # replacing the total saying of the parse this with none !
                np = NaturalProcessing()  # creting the object of the classs
                # -------------You are working here -------------
                tokenized_sentences_return = np.word_tokeniztion(
                    self.total_saying, sent_tokenized=False)  # this parse the Np with the tokenizing of the words
                print(tokenized_sentences_return)  # this prints the TOkenized the words
            elif total_saying.startswith("youtube") or total_saying.startswith(
                    "search on youtube") or total_saying.startswith("search youtube") or total_saying.startswith(
                "youtube search"):
                self.total_saying = total_saying.replace("search", '')
                self.total_saying = self.total_saying.replace("search on youtube", "")
                self.total_saying = self.total_saying.replace("youtube", "")
                self.total_saying = self.total_saying.replace("search youtube", "")
                self.total_saying = self.total_saying.replace("youtube search", "")
                self.text_to_speech("Searching on youtube for : " + total_saying)
                self.store_userinput("Search on Youtube :" + total_saying)
                Y = YouTubeSearch()  # Creates in the Youtube Class
                self.text_to_speech('Displaying Results')
                self.lastlink = Y.search(self.total_saying)  # Sends the Total Saying to the Youtube Search Function
                self.text_to_speech('Youtube Result Shown!')
            elif total_saying.startswith('stack over flow') or total_saying.startswith(
                    'stackoverflow') or total_saying.startswith("stack overflow") or total_saying.startswith(
                'search stack over flow') or total_saying.startswith('stack search') or total_saying.startswith(
                'search stackoverflow'):
                self.total_saying = total_saying.replace('stackoverflow', '')
                self.total_saying = self.total_saying.replace('stack overflow', '')
                self.total_saying = self.total_saying.replace('stack over flow', '')
                self.total_saying = self.total_saying.replace('search stack over flow', '')
                self.total_saying = self.total_saying.replace('stack', '')
                self.total_saying = self.total_saying.replace('stack search', '')
                self.total_saying = self.total_saying.replace('search stackoverflow', '')
                self.text_to_speech('Search on Stackoverflow' + self.total_saying)
                self.store_userinput('Search on Stackoverflow :' + self.total_saying)
                SOF = StackoverFlow()  # -- Creates the Object Stack over flow class and calls the search function
                self.lastlink = SOF.search(
                    self.total_saying)  # replacing the last link so that we can read it out later
                # self.db.insert_into_History("searching on stackoverflow : " + self.lastlink)
                self.text_to_speech("Stack over flow Results Shown")
            elif total_saying.startswith("search music") or total_saying.__contains__(
                    "search music") or total_saying.__contains__("find music"):
                self.total_saying = total_saying.replace('search music', "")  # replacing the search music with empty
                self.total_saying = self.total_saying.replace("find music", '')
                self.total_saying = self.total_saying.replace("music", '')
                SoundCloudSearch(self.total_saying)
            elif total_saying.startswith("play music") or total_saying.__contains__("music please"):
                self.total_saying = total_saying.replace("play music", "")
                self.total_saying = self.total_saying.replace("music please", "")  # replacing the string !
                MP_gui = main()
                MP_gui.run()
                self.store_userinput("playing music")
            # last link being read
            # This calls the Web scrap class in the __speakcode.py
            # TODO : Add the links to be dynamically updated from the last scrapped page
            elif total_saying.startswith("read it out to me") or total_saying.startswith("read it out for me"):
                # self.db.insert_into_History(total_saying + ":" + self.lastlink)
                self.store_userinput(total_saying + ":" + self.lastlink)
                self.total_saying = total_saying.replace("read it out to me", "")
                WS = WebScrap()
                WS.scrap_link(self.lastlink)
                self.store_userinput(total_saying + ":" + self.lastlink)
            elif total_saying.startswith("web"):
                self.total_saying = total_saying
                webbrowser.open("")
            elif total_saying.startswith("twitter status") or total_saying.startswith("status"):
                self.total_saying = total_saying.replace("tweet ", "")
                self.total_saying = self.total_saying.replace("status ", "")
                self.total_saying = self.total_saying.replace("twitter status ", "")
                ckey = 'MzaXuqZ6SDL9WTvYpQuSldfQ7'
                csecret = '6erIkd8q9eYfsuBAaFpSs7WFGg8ClTiKszaDjMscZsJxkv7JMR'
                atoken = '558084273-43R4qZg8jfAMKRVhlxruiHp1m1No1pbLMFjqIXwN'
                asecret = 'I5UIacTCLHAq7qwGhfTdoFxph3BLBSUhoZTHa9Ktz6sOU'
                TP = Twitter_PYSHA(ckey, csecret, atoken, asecret)  # create object and pass in values
                api = TP._api_auth()
                status = self.total_saying
                self.store_userinput("tweeting on twitter:" + self.total_saying)
                self.text_to_speech("tweeting on twitter :" + self.total_saying)
                api.update_status(status)  # Posts the status om the twitter.

            elif total_saying.startswith("mail") or total_saying.startswith("check email") or total_saying.startswith(
                    "check mail"):
                self.text_to_speech("")
                webbrowser.open("www.gmail.com")
                webbrowser.open("www.hotmail.com")
                webbrowser.open("www.yahoo.com")
            elif total_saying.startswith("twitter"):
                webbrowser.open("www.twitter.com")
            elif total_saying.startswith("reddit"):
                webbrowser.open("www.reddit.com")
            elif total_saying.startswith('what') or total_saying.startswith("when") or total_saying.startswith(
                    "how") or total_saying.startswith("where") or total_saying.startswith(
                "solve") or total_saying.startswith("who") or total_saying.startswith(
                "whom") or total_saying.startswith("why") or total_saying.startswith("which"):
                self.total_saying = total_saying
                self.store_userinput('Question Asked : ' + self.total_saying)
                # since this is a computation engine that will be used for the computation of the question asked .!
                WFM = WolFrameAlphaClass()  # creating the wolframapla class that will be used for the cretion of the api assistant
                self.text_to_speech('searching database')
                WFM_backstring = WFM.search_engine(
                    self.total_saying)  # this searches the WOlframAlpha for the Search Strings
                if WFM_backstring != "":  # if the input returned from the Wolframalpha turns out to be null then leave it .
                    self.text_to_speech(WFM_backstring)  # this converts text to speech






# TODO : text mode needs to be created
# going in the form of the chat bot, since the particular chat bot will be used
class TextMode:
    def __init__ (self):
        print("text mode Class Accessed!")

    def text_mode (self, text_input=''):
        print("--runs the Text Mode --")
        # here you need tohave a user interface , and then provide a chatting history to!


# keep in mind that it can also be used for the other queries like loggin into the particular websites.
# These all moduels are under progress,
# Development module will be started building after 30 november 2016, !

# TODO : Social Media Access like facebook , Instagram and others
class SocialMedia:
    def __int__ (self):
        print("This is the Constructor of the class Social media")

    def email_access (self):
        print("")

    # The below function will be used regerding to the twitter accessing and stuff
    def twitter_access (self):
        print("Granting the twitter Access")

    # The below function will be used for the messaging and getting the messages from the facebook

    def Messenger_access (self):
        print("MESSEBGER ACCESS FOR SENDING AND RECIEVING MESSSAGES")

    # The below function will be used to access the facebook and all the stuff.


    def facebook_access (self):
        print("FACEBOOK Access for accessing and recieving facebook messages")

    # This will be used to access the instagram, so that you can access the current features

    def instagram_access (self):
        print("Granting the instagram Access and checking")

    # This function will be used to access the social medias and choose the correct social media for the particular stuff.

    # keep in mind that it can also be used for the other queries like loggin into the particular websites.
    def social_media_access (self, browse_key=""):
        print("SOCIAL MEDIA DETECTED")  # This will be used for the debugging purposes
        if browse_key != "":
            if browse_key == 'facebook':
                print("Browsing Facebook")
                webbrowser.open("www.facebook.com")
            elif browse_key == 'twitter':
                print("Browsing twitter")
                webbrowser.open("www.twitter.com")
            elif 'linkedin' == browse_key:
                print("Browsing linkedin")
                webbrowser.open("www.linkedin.com")
            elif browse_key == 'instagram':
                print("Browsing Instagram")
                webbrowser.open("www.instagram.com")
            elif browse_key == 'reddit':
                print("Browsing Reddit")
                webbrowser.open("www.reddit.com")



class Main_Call():
    # TODO : Make it a little more intelligent
    PYSHA_Obj = PYSHA_CLASS()

    def __init__ (self):
        print("Main Class Intialized.....")

    def main (self):  # main program access
        print("--")
        # duration = float(input("How much time you need to record for ?"))
        # record_something(duration)  just trying to pause the thing
        client_id = ""  # this is the google api client id
        client_secret = ""  # this is the google api client secret key
        self.PYSHA_Obj.text_to_speech()  # Calls the virtual assistant to speech
        # speech_to_text()  # calling the function
        while True:
            # try:
            self.PYSHA_Obj.record_something(7)  # providing the Duration in the Record function!
            self.PYSHA_Obj.speech_to_text_wav("output.wav")  # Converting the recorded format of WAV to speech!
            # except:
            #   text_to_speech("There is a problem with the internet connection , kindly try to configure it.!")

            # The above the Audio has been recorded , and now the Audio needs to be converted into texts/

            # Machine Learning book + NLTK BOOK need to be studied  with Plotting and OPENCV2

            ## Work with the MEGA VOICE COMMAND AFTER THE EXAM HAVE BEEN FINISHED.
