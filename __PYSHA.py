try:
    import psutil # This imports the process utilities , for the checking of the specific application running an closing
    import datetime  # Importing the datetime for the timing modules since the date time is used to answer the questions
    import wave  # Importing the wave of for the recording(This is the format for the recording which is used .wav
    from random import *  # Using the random  function for the creation
    import pyaudio  # importing the header file of the pyaudio
    import speech_recognition as sr  # Importing the speech recognition file for the code.!!
    import random  # importing the random module for the random Short term memory
    import datetime as dt  # date time module for the implementation of the date and the time
    from urllib.request import urlopen  # If there is a webpage to be downloaded
    from pdfminer.pdfinterp import PDFResourceManager, process_pdf
    # For creating the resource manager and processor for the pdf
    from pdfminer.converter import TextConverter  # For the conversion of the Text in the pdf
    from pdfminer.layout import LAParams  # Taking the Linear layout in mind
    # import BytesIO
    from io import StringIO  # String IO for conversion to string representation
    from io import open  # opening the file
    from zipfile import ZipFile  # Zip file will be used to zip word into xml
    from io import BytesIO  # for the conversion of the word files will be used later
    import os  # the module will be used to find in the correct directory and files extensions check
    import docx  # importing the docs module as per advised
    import ntpath  # for extracting filename from full path
    # import pyscreenshot # for taking screenshots of the Desktop on Current command
    # from .PygletMusic.Pyglet implementation import *  # Music player GUI implemented
except Exception as E:
    print("Missing header file which needed to be installed", E)
    exit(0)
try:
    from _Joke import *  # For the Jokes, Cracked from the web (web scrapping Module)
    from _NaturalLanguageProcessing import *  # This is the Natural language processing
    from _WolFrameAlphaClass import *  # For computation and intelligence engine.
    from __soundcloud import *  # Soundcloud is for the File
    # from __linksearch import *  # importing for the link search
    from __speakcode import *  # For speaking the code from the web scrapping .
    from _dbdata import *  # Database function for the request and all others.
    from _stackoverflow import *  # Stackoverflow code implementation of the current file.
    from _twitter import *  # imports the twitter Pysha client which has been.
    from _youtube import *  # imports youtube created local header file , for searching on youtube
    from __github import *  # Github Repository , For accessing the Github
    from _SocialMedia import *  # importing the social media moduel for the implementation of the social medias
    from _TextMode import *  # the text mode will be used for the messaging application like look, like a bot
    from AssistantProperties import _chooseassitant  # importing the properties of the assistant being choosen.
    from __shorttermmemory import *  # Short term memory
    from Chatdependencies._chat import *  # importing the _chat module
    # from SentimentalAnalysis.Basic_sentimentanalysis import *  # imports to download tweets
    from __newsupdates import *  # imports the news class for the news updates.
    from SentimentalAnalysis.downloadTweets import *  # imports for performing the sentimetn analysis
    from __facebook import *  # importing the facebook module for GraphAPI.
    from MouseMovments import mm  # Importing the mouse movement file, to control Mouse and keyboard
    from load_inall import *  # script for playing the loading in All mp4 files
    from __imagescheck import *  # this is for the checking of the images
    from sportslive import watch_live_sports_stream  # This imports the funtion of the watching live streams
except Exception as E:  # Taking the Exception as E
    print("Missing the Built in PYSHA files for the Development", E)
    exit(0)  # Exiting the Application
# imports the short term memory code  --> for getting the last strings backs 7 +-2
# this si the importing of the header files !
# Pre requirements : You need to Install Microsoft SDK fo Speech and all the available Tools
# Keep in mind that This is Under Heavy Construction and will be used in the later increments and
# TODO : YOU NEED TO ADD IN THE ARTIFICIAL FAST INTELLGIENCE AND THE FAST PROCESSING. !
'''
// This build is heavily under progress by , If you want to check all the dependencies,
and want to contribute to improve the particular algorithm, check Repository.
https://github.com/shafaypro/PYSHA1.0
Info Dated: 2/3/2016  , WaterFall method is being Followed

User Guideline:

Wherever you run this Project, the basic dependencies are converted in to the local machine,

--> The machine tells about her self and then wait for the user to have the specified an speech input,

The device of the microphone is connected and then it is parsed to the pyaudio where the input is then

Converted to the Audio file  Formatted as WAV, under the F.L.A.C encoding, then it is parsed to the google api,

since the api is then accessed and the chunks of the audio is converted into the string and then returned into the
string.

There are some already stored procedures for the particular messages , like if a message starts from the :::

what is the ----> Time, Date and others can tell you the the time ,date and others.
Ther are some other features also added in the header file , like haviing a random chat and working on different kind of
Loops

you can ask for the questions and the Answers regarding to the Natural language processing module .

If you want to ask for the Application running modules then
for that :
RUN or OPEN _________ the Underscore should be replaced by the application name
--> This script will also be monitroing the computer (Here it contains the data analysis and the data visualization part
This will be including the statistical analysis and well as the sentimental analysis . ! so that this may be used in the
 later
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
ask --> switch to _______   : replace the _________ with Female , male , dave , hazel , zira

ask --> tweet __________________  : posts a tweet on twitter.

ask --> search  music ________________ : searched the music.

ask --> find music _______________ : finds the music from the internet.

ask --> search for ________________ : searches on google

ask --> launch ___________________ or RUN ______________ : runs the define application.

ask --> read it out for me : reads the last visited page

ask --> Search for _________: This opens up the browser for the result so that the Virtual assistant is able to read
from the
data

ask --> find me a wallpaper __________ or Find a wallpaper _____________ : replace ______ with your query

ask --> Mouse Move _________ : replace ___- with up , down, left , right , click , scroll # Controls the Mouse Movements

--ask --> Stop chrome or other applications : Stops the processes of the application

ask --> Stop,stop listening,quit : This will results in the Quiting , exiting for the virtual assistant!!

ask --> search ________ on Wikipedia : will search on wikipedia based on certain meaningful words(replaces at _____)

ask --> show me a comic : finds a comic from the internet and displayed the comic

ask --> tell me a joke : Finds a joke from the web and shows the joke
-ask --> what is the date / what is the time
 -
 -
 -ask --> What is the integeration of 2 x squared + 3 x + 7
 -
 -
 -ask --> which is greater in quantity 1 liter of water or 1 liter of milk
 -
 -
 -ask --> Stack over flow search _____________
 -
 -
 -______ replace this with your query
 -
 -ask--> search youtube ____________ or youtube _________________
 -
 -
 -ask--> searh youtube playlist _________ : ___ is the query of yours
 -
 -search youtube ___________________:  -______ replace this with your query
 -
 -or youtube ___________________
 -
 -ask--> search music _____________ or find music _______________ : replace ___ with your song name or artist or both
 
 -ask--> Read it out to me      or Read it out for me
 
 -# This will read all the text from the last visited page
 
 -ask --> switch to _______   : replace the _________ with Female , male , dave , hazel , zira
 
 -ask --> tweet __________________  : posts a tweet on twitter.
 -
 -ask --> search  music ________________ : searched the music.
 -
 -ask --> find music _______________ : finds the music from the internet.
 -
 ask --> play music  : plays the music
 -
 -
 ask --> Music Please : plays the music
 -
 -
 ask --> music video please : plays a music video
 -
 -
 -ask --> search for ________________ : searches on google
 -
 -
 -ask --> launch ___________________ or RUN ______________ : runs the define application.
 -
 -
 -ask --> read it out for me : reads the last visited page
 -
 -
 -ask --> Search for _________: This opens up the browser for the result so that the Virtual assistant is able to read from the
 -data
 -
 -
 -ask --> Stop,stop listening,quit : This will results in the Quiting , exiting for the virtual assistant!!
 -
 -
 -ask --> search ________ on Wikipedia : will search on wikipedia based on certain meaningful words(replaces at _____)
 -
 -
 -ask --> show me a comic : finds a comic from the internet and displayed the comic
 -
 -
 -ask --> tell me a joke : Finds a joke from the web and shows the joke
 --
 -ask --> tokenize sentence ____________________________ : will returned a tokenized sentence 
 
 -ask --> tokenize sentence ____________________________ : will returned a tokenized sen
 -
 -
 -ask --> What did i just said : returns the last query from the short term memory(termed as the top runned query --> the last most)
 -
 -ask --> What did i said you:  Returns maximum from the shrot term memory(last 7+-2 statments ) as per human brain. 
-
-ask --> ______________________- Ask anything other than the above text the responce wil be returned based on the machine larning algorithums and then the responce data will be returned.!

-ask --> Stop __________ : replace ____ with any application name such as Calculator , windows media player and others


-ask --> Write to a file : after that you can keep saying any thing, and it will write to the specified file
unless you say exit only.


'''
# TODO : Working on EMAILS, MESSENGERS, OPEN CV, IMAGE RECOGNITION, NATURAL LANGUAGE PROCESSING, MACHINE LEARNING, DB
# TODO : SELF LEARNING, additonal Chat properties


''' Keep in mind to have all the back up things,
For the personal computer you need to have the computer access,
And all the other things given to the Assistant so that it can work in there.
'''

# TODO : USE THE Natural Language processing TOO, To improve the Virtual Assistant
__author__ = "M Shafay Amjad"
__QA__ = "mshafayamjad@gmail.com"
__copyrights__ = "© to  , No changes should be made prior to his permission"
__supervisor__ = ""
__version__ = 1.0
__productname__ = "PYSHA"
__university__ = "Government College University Lahore"
# TODO : File Information needs to be implemented


# The reverse shell process is for personal use, where we will be using to ping the Updated Code, to your Home location
# Computer Code!
'''
Below Function is responsible for the writing of the file , Since if you want to write VIA through Text strings
you can use that through the Writing_to_file Function, the text is based on speech to text  and Exits when you say
":EXIT" <-- it stops writing to the file and goes to General Mode.
'''


# Writing to the file , while speaking class (Writing_to_file )
# TODO : Make it more effient .!

class Writing_to_file:
    def __init__(self):
        total_saying = ""
        while True:
            temp = self.write_by_speak()
            if (temp != "exit" or not temp.__contains__("exit")) and temp is not None:
                total_saying += temp
                print(temp)
            elif temp is None:
                continue  # Debugging
            elif temp == "exit" or temp.__contains__("exit"):  # This is the Exiting condition
                break  # Goes outside the loop
                print(total_saying)
                self.write_in_file(total_saying)
                print("------------")

    def write_in_file(self, text):
        current_directory = os.path.dirname(os.path.realpath(__file__))  # Getting the current directory from the file
        print("Writing to a file")
        specified_file = current_directory + "OnSpeakType\\datain.txt"  # Creating the specified file
        file_writer = open(specified_file, "w+")  # Opening the specified file
        file_writer.write(text)
        print("Writte to the file data .txt ! ")
        file_writer.write(" ")
        file_writer.close()

    def write_by_speak(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)  # Adjustment of the microphone on the basis of the required
            # Envirenoment adjustment of the specified microphone
            # print(r.energy_threshold)
            # print("Chucking rate: ", source.CHUNK)
            # print("format rate :", source.format)  # Debuggin purpose
            # CHUNK = 1024
            # FORMAT = pyaudio.paInt16  # the Format is picked up from the pyaudio
            # CHANNELS = 2  # The Cross Channels
            # # RATE = 44100
            # source.CHUNK = CHUNK
            # source.format = FORMAT  # FORMATING THE SOURCE FILE
            # print(dir(source))
            print("Say something!...")
            # print(r.energy_threshold)
            r.energy_threshold += 280
            # # print(r.adjust_for_ambient_noise(source,duration=1))
            audio = r.listen(source)

            # Speech recognition using Google Speech Recognition
        try:
            print("Parsing ...")  # Debugging To
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            # print(r.energy_threshold )
            # print(help(r.recognize_google))
            # text = r.recognize_google(audio, language='en-US')
            text = r.recognize_google(audio, language='en-GB')  # Recognizing the command through the google
            # r.re
            # r.re
            print("You said: " + text)  # printing the text of the input
            return text
        except sr.UnknownValueError:  # Knowing the exception
            print("Google Speech Recognition could not understand audio")
            return
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return
        except sr.HTTPError as e:  # In Case of Server down or server not able to be found 404, 503
            print("Couldn't connect to the websites perhaps , Hyper text transfer protocol error; {0}".format(e))
            return  # returning for the debugging


class FilestoTextFiles:
    dir_path = os.path.dirname(os.path.realpath(__file__))  # Global Object accessible directory name

    # Constructor aka INITIALIZER
    def __init__(self):
        print("FilestoTextFiles have been intialized")  # Debugging

    # The below function writes to a file_name as .txt extension, for later onward.
    def save_to_txt(self, text_data, file_name):
        file_name = ((file_name.replace(".pdf", ".txt")).replace(".docx", ".txt")).replace(".doc",
                                                                                           ".txt")  # Renaming the file to txt
        exact_path = ntpath.basename(file_name)
        # if not os.path.exists(self.dir_path+"\\ConvertedTexts"):
        #     os.makedirs(self.dir_path+"\\ConvertedTexts")
        # file_writer = open(self.dir_path+"\\ConvertedTexts\\"+str(file_name), "w")  # Writing option in the file
        if not os.path.exists(self.dir_path + "/ConvertedTexts"):
            os.makedirs(self.dir_path + "/ConvertedTexts")
        file_writer = open(self.dir_path + "/ConvertedTexts/" + exact_path, "w")  # Writing option in the file
        # file_writer = open(file_name, "w")  # Writing option in the file
        # print(text_data.encode('utf-8'))
        file_writer.writelines(str(text_data.encode('utf-8')))  # Writes to a file
        file_writer.close()  # Closes the file writer.

    # The below function is responsible for the reading of the pdf File
    def readPDF(self, pdfFile):
        try:
            rsrcmgr = PDFResourceManager()  # Creates the resource manager
            # resource_mang = PDFResourceManager()
            retstr = StringIO()  # string object for the representation of the pdf
            # string represetnation from string input and output module
            laparams = LAParams()  # Parameters Object Creation
            device = TextConverter(rsrcmgr, retstr, laparams=laparams)  # Creating the device for the conversion
            process_pdf(rsrcmgr, device, pdfFile)  # Process the specific pdf, to convert into string representations
            device.close()  # Closes the device.
            # print(retstr) # Debuggin
            # Decoded value is returned here UTF-8
            content = retstr.getvalue()  # gets the text from the string object
            # print(content)5
            return content  # Returns the content where its called
        except Exception as Ex:
            print("While reading the file , there was an error in the function Readodf as :",
                  Ex)  # printing the exception

    # Check case for the pdf
    def testpdf(self):
        try:
            pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")  # Gettting from the web
            print("Converting ...")
            # print(pdfFile)
            outputString = self.readPDF(pdfFile)  # Calls the function to read from the pdf
            # pdfFile.close() # Closes the pdf File
            print("Conversion Completed")  # Debugging
            return outputString  # this returns the output string for the specified format
        except Exception as Ex:
            print("Unable to convert the pdf to text due to : ", Ex)  # Printing the Exception
            # print(Ex)  # DEBUGGING
            print("In function testpdf")  # Testing
        finally:
            pdfFile.close()  # keep in mind to close the file which you are working on !

    # Converting the specified file to pdf

    def convert_pdf(self, pdf_filelocation):
        if pdf_filelocation != "":
            print(pdf_filelocation)
            pdf_File = open(pdf_filelocation, "rb")  # Opens the pdf in the read format
            print("Converting ..")  # PROMPT
            outputString = self.readPDF(pdf_File)  # Calls the read PDF function to work on with it
            lines = outputString.split("\n")
            outputvalue = ""
            for line in lines:  # Since the line contains the next line and the unicode schemes to remove those.
                if line != "":
                    line = line.strip()
                    line = line.replace("b\"", "")  # replacing for the filtering
                    outputvalue += line  # Adding in the output value again and again.
            return outputvalue  # Returns the output string to the function called
        else:
            print('There is no Location Valid , specified ')  # DEBUGGING
            # pdf_File.close() # Closes the specified file

    # The below function recieves the list of pdf files and then convert them in to set of files.

    def convert_list_pdffiles(self, list_pdfs):
        # total_file_text_data = []  # This is the list storing the file information as specified
        if len(list_pdfs) >= 1 and type(list_pdfs) == list:
            for filelocation in list_pdfs:
                # file_data = open(filelocation, "rb")  # reading the specifid file
                text_converted_file = self.convert_pdf(filelocation)  # Converts the file data to the text format
                # The below function writes to txt
                file_name = filelocation.split("\\")[-1]  # Gets the file name from the speified path
                print("Converted -->" + file_name)
                self.save_to_txt(text_converted_file, file_name)  # --Saving to .txt file
                # total_file_text_data.append(total_file_text_data)  # Appends in the list of the text files
                # return total_file_text_data # returns to the main function the total file text data with multiple files in action
            print("All the pdf files have been converted")  # PROMPT
        else:
            print(
                "List of pdf files had length less equal toone and the type pf the files passed are not in the form of list")  # DEbugging

    def get_AllpdfFiles(self):
        # Get all the PDF filenames.
        pdfFiles = []  # this is the pdf file list
        # for filename in os.listdir(self.dir_path + "\\Files"):  # Specifying the folder and looping through the folder
        for filename in os.listdir(self.dir_path + "/Files"):  # Specifying the folder and looping through the folder
            if filename.endswith('.pdf'):
                # pdfFiles.append(self.dir_path + "\\Files\\" + filename)  # Adding the pdf complete location in the list.
                pdfFiles.append(self.dir_path + "/Files/" + filename)  # Adding the pdf complete location in the list.
        pdfFiles.sort(key=str.lower)
        return pdfFiles

    def get_all_running_files(self):
        file_list = []  # This gets the list of the files
        for proc in psutil.process_iter():  # going through all of the processes to get the list of the running processes
            try:
                if len(proc.open_files()) != 0:  # If there is a process running
                    file_list.append(proc.open_files())  # adding in the file so that the data can be used.
            except:
                continue
        return file_list  # this returns the file list

    def get_pdf_files(self):
        pdf_files_location = []
        file_list = []  # This gets the list of the files
        for proc in psutil.process_iter():  # going through all of the processes to get the list of the running processes
            try:
                if len(proc.open_files()) != 0:  # If there is a process running
                    file_list.append(proc.open_files())  # adding in the file so that the data can be used.
            except:
                continue
        for list in file_list:
            for inner_list in list:
                if str(inner_list).split(',')[0].__contains__(
                        '.pdf'):  # Splitting on the basis of commas as it will be providing the data !
                    if str(inner_list).split(',')[0][16:-1].endswith('StandardBusiness.pdf'):
                        continue
                    else:
                        pdf_files_location.append(
                            str(inner_list).split(',')[0][16:-1])  # this wil get the file location

        return pdf_files_location
        # print(pdf_file_list)

    '''----BELOW FUNCTIONS ARE FOR WORD FILES with .doc or .docx---'''

    def read_wordFile(self, filename):  # Reading the file from the word file
        doc = docx.Document(filename)  # Creating the document of docs form the specified fule
        fullText = []  # Creating a list of texts
        for para in doc.paragraphs:
            fullText.append(para.text)
        return '\n'.join(fullText)  # returning by joining in the next line by line

    def get_AllwordFiles(self):
        wordFiles = []  # List which wil be holding the file names of word file
        # for filename in os.listdir(self.dir_path + "\\Files"):  # listing the current directory files
        for filename in os.listdir(self.dir_path + "/Files"):  # listing the current directory files
            if filename.endswith('.word') or filename.endswith('.docx') or filename.endswith('.doc'):
                # wordFiles.append(self.dir_path + "\\Files\\" + filename)  # adds the file name in the word list
                wordFiles.append(self.dir_path + "/Files/" + filename)  # adds the file name in the word list
        wordFiles.sort(key=str.lower)  # sorts the list with respect to key value
        return wordFiles  # returns all the file list

    def convert_allwordFiles(self, wordfilelist):
        if type(wordfilelist) == list and len(wordfilelist) >= 1:
            for single_wordFile in wordfilelist:
                data = self.read_wordFile(single_wordFile)  # Calling in the word data writing function
                file_name = single_wordFile.split("\\")[-1]  # Gets the file name from the speified path
                lines = data.split("\n")
                total_data = ""  # Will hold the data
                for line in lines:  # Data filterning
                    if line != "":
                        line = line.strip()
                        total_data += line + "\n"  # Appending in the line
                print("Converting...." + single_wordFile)
                self.save_to_txt(total_data, file_name)  # Passing the data and the single file name to the list
        else:
            print("NOPE NOT POSSIBLE")

    def convert_all(self):
        pdf_files = self.get_AllpdfFiles()  # Gets all the pdf file.
        word_files = self.get_AllwordFiles()  # Gets all the word files.
        print("pdf Files found are ", pdf_files)  # Prompting the message in the console
        print("word_files found are", word_files)  # prompting the message on console
        '''----------------READING AND CONVERTING ALL THE PDF FILES TO TXT FILES -------------------------------'''
        self.convert_list_pdffiles(pdf_files)  # Calls in the convert function to convert all the pdfs
        self.convert_allwordFiles(word_files)  # Converts all the word files
        # pdf_files_converted_data = self.convert_list_pdffiles(pdf_files)  # Gets all the data in the pdf files .
        # The Above returns a list .


class PYSHA_CLASS:
    db = NONE
    lastlink = ""  # just to be reminded for the last link visited
    engine = pyttsx.init()  # intializing the engine here so that there are global engine speech , which can be changed
    py_chat_bot = Chatting_PYSHA(name="PYSHA", trainable=True, train_corpus=True)  # intialized the Chatting Pysha
    newscheck = NEWS()  # Creates an object for news
    music_player = MUSIC_PLAYER()  # This creates the music player object class
    image_shower = IMAGE_CHECK()  # This creates the object for the images , this can be accessible locally
    pdf_file = None # Specifing the pdf file to be none !
    fttf = FilestoTextFiles()  # Creating the class of the text filtering , whic hwill be used to convert to pdf
    music_check_indicator = 0  # This will be used to check the music of the
    image_check_indicator = 0  # This will be used to check if the image is already there or not

    def __init__(self):

        print("PYSHA INITIALIZED!")
        self.createlocaldb()  # this creates the localdb for requests

    # creating the local Database
    def greetings_check(self):
        try:
            hour = datetime.datetime.now().hour  # Getting the stat of the current hour !
            if hour in [4, 5, 6, 7, 8, 9, 10]:
                self.text_to_speech("Good Morning Shafay, seems like you woke up on time")
            elif hour in [11, 12, 13, 14, 15]:
                self.text_to_speech("Good After noon Shafay, seems like you are going to university")
            elif hour in [16, 17, 18, 19]:
                self.text_to_speech("Good Evening Shafay!, What are your doing ? You should be taking classes ")
            elif hour in [20, 21, 22, 23, 24, 1, 2, 3]:
                self.text_to_speech(
                    "Well seems a little off , haven't you slept Well ? . Its " + str(hour) + str(" here"))
            else:
                self.text_to_speech("Time checking Error faced")
        except Exception as Ex:
            print("Exception Occurred in function Greetings_check :", Ex)

    def schedule_check(self):
        try:
            file_read = open("Schedule.txt", "r").readlines()
            for line in file_read:
                self.text_to_speech(line.strip())  # Speaks all the lines for the today schedule
        except Exception as Ex:
            print("Not found", Ex)

    '''Having the specified short term memory in case of checking through the Brain'''

    def shortterm_check(self, limit=0):
        try:
            stm_list_recieved = stmcheck()  # calls the stm check module
            list_recieved = display_stm(
                stm_list_recieved)  # Filterening all the sentences and specifying the current list
            if limit == 0:
                random.shuffle(list_recieved)  # random shuffling , Using the random shuffle for the current memory
                for i in range(len(list_recieved)):
                    self.text_to_speech("You said at " + str(i) + " " + list_recieved[i])
                    # just printing the list for the things.
            elif limit == 1:
                self.text_to_speech(list_recieved[0])  # pass the first element inthe list which is the last said.
                # TODO : call the text to speech and speak the list in an specified order
        except Exception as Ex:
            print("short term memory check Failure at ", Ex)

    # Create the local database for the function
    def createlocaldb(self):
        try:
            self.db = db_data()  # this calls the db class
            self.db.create_database()  # this creates the database for the class.
        except Exception as Ex:
            print("there was an error while creating the local database", Ex)

    # Playing the video for the module trhough python check
    def play_video(self):
        try:
            os.system("start  E:\\MusicVideos\\Marshmello---Keep-it-Mello-ft-Omar-LinX-Official-Music-Video.mp4")
        except Exception as Ex:
            print("check the directory exception", Ex)

    # TODO : more Accurate apps running
    # for going through the history

    def insert_into_request(self, request_text, responce_text):
        # this is the function responsible for the writing in the history.
        try:
            self.db.insert_into_Requests(request_text, responce_text)  # this is twrite into the reposce text
        except Exception as Ex:
            print("There was and Error inserting in to the database at insert_into_request function", Ex)

    # For terminating the prgrams use the following code
    def close_program(self, input_string):
        if input_string == "window media player":
            try:
                self.text_to_speech("Closing Window Media Player")
                os.system("TASKKILL /F /IM wmplayer.exe")
                self.text_to_speech("Window media player has been closed")
            except Exception as ex:
                print("Exception occured a ", ex)  # printing the exception
        elif input_string == "music":
            try:
                os.system("TASKKILL /F /IM wmplayer.exe")
                self.text_to_speech("Music stopped")
            except Exception as Ex:
                print("close program input string debugging requires")
        elif input_string == "calculator":
            try:
                self.text_to_speech("Closing Calculator")
                os.system("TASKKILL /F /IM calc.exe")
                self.text_to_speech("calculator has been closed")
            except Exception as ex:
                print("Exception occured a ", ex)  # printing the exception

        elif input_string == "note pad" or input_string == "notepad":
            try:
                os.system("TASKKILL /F /IM notepad.exe")
            except Exception as ex:
                print("Exception occured a ", ex)  # printing the exception
        elif input_string == "performance monitor":
            try:
                os.system("TASKKILL /F /IM perfmon.exe")  # Closing the performance monitor
            except Exception as ex:
                print("Exception occurred ", ex)  # printing the exception
        elif input_string == "smartscreen" or input_string == "smart screen":
            try:
                os.system("TASKKILL /F /IM smartscreen.exe")
            except Exception as ex:
                print("Exception occurred ", ex)  # printing the exception
        elif input_string == "space agent" or input_string == "spaceagent":
            try:
                os.system("TASKKILL /F /IM SpaceAgent.exe")
            except Exception as ex:
                print("Exception occured a ", ex)  # printing the exception
        elif input_string == "network status":
            try:
                os.system("TASKKILL /F /IM netstat.exe")
            except Exception as ex:
                print("Exception occurred a ", ex)  # printing the exception
        elif input_string == "defragment":
            try:
                os.system("TASKKILL /F /IM defrag.exe")
            except Exception as ex:
                print("Exception occurred as ", ex)  # printing the exception
        elif input_string == "clean manager":
            try:
                self.text_to_speech("")
                os.system("TASKKILL /F /IM cleanmgr.exe")
            except Exception as ex:
                print("Exception occurred as ", ex)  # printing the exception
        elif input_string == "command prompt":
            try:
                self.text_to_speech("Closing Command prompt")  # Voice
                os.system("TASKKILL /F /IM cmd.exe")
                self.text_to_speech("Command prompt has been closed")  # Voice
            except Exception as ex:
                print("Exception occurred as ", ex)  # printing the exception
        elif input_string == "chrome" or input_string == "google chrome":
            try:
                os.system("TASKKILL /F /IM chrome.exe")
                self.text_to_speech("Chrome has been closed")  # Closed the chrome
            except Exception as ex:
                print("Exception occurred as ", ex)  # printing the exception
        else:
            print("I found something new to close , I cannot locate the thing")
            self.text_to_speech("I found something new to close, i cannot locate the location")
            # Debugging

    # TODO: For running the apps
    def run_apps(self, text_input=""):
        text_input = text_input.strip()
        if text_input != "":
            if text_input == "calculator":
                self.text_to_speech("Launching Calculator")
                os.startfile('calc.exe')  # Running the calculator in the Operating system
                self.text_to_speech("Calculator launched")
                return
            elif text_input == "notepad":
                self.text_to_speech("Launching Notepad")
                os.startfile('notepad.exe')  # Running the notepad using the Os module for the specified Attrirbute !
                self.text_to_speech("notepad launched")
                return
            elif text_input == "performance monitor":
                os.startfile('perfmon.exe')  # Launchign the Performance monitor from the exe
                self.text_to_speech("Performance monitor has been launched")
                return
            elif text_input == "smart screen":
                os.startfile('smartscreen.exe')  # Working on the smart screen and running the Exe !
                self.text_to_speech("smart screen launched ")
                return
            elif text_input == "space agent":
                os.startfile('SpaceAgent.exe')  # Running the space agent for the
                self.text_to_speech("space agent has been launched")
                return
            elif text_input == "network status":
                os.startfile('netstat.exe')  # you are working ehre !
                self.text_to_speech("Network status for today have been shown on the screen")
                self.text_to_speech("somethings seems to be off")
                return
            elif text_input == "bluetooth setting":
                os.startfile('fsquirt.exe')  # you are working here !
                return
            elif text_input == "defragment":
                os.startfile('Defrag.exe')  # you are working here !
                return
            elif text_input == 'clean manager':
                os.startfile("cleanmgr.exe")
                return
            elif text_input == "command prompt":
                os.startfile("cmd.exe")
                return
            elif text_input == 'direct ex' or text_input == 'direct setting':
                os.startfile("dxdiag.exe")
                return
            elif text_input == "control panel":
                os.startfile('control.exe')
                return
            elif text_input == 'resource monitor':
                os.startfile('resmon.exe')
                return
                # this launched the resource monitor to monitor the resource!
            elif text_input == "game panel":
                os.startfile('GamePanel.exe')
                return
            elif text_input == 'graphic settings':
                os.startfile('Gfxv4_0.exe')  # this access the graphic cards
                return
            elif text_input == 'dpi scaling':
                os.startfile('DipScaling.exe')  # this truns the dpi scalling for the
                return
            elif text_input == 'disk partition':
                os.startfile('diskpart.exe')
                return
            elif text_input == 'python' or text_input == "python interpreter":
                try:
                    os.startfile("C:\\Program Files\\Python35\\pythonw.exe")
                    # this calls the file location and then run the program of the python.
                    # There you should run the pyton programming language
                    # so that the language will be specified by the face of the
                    return
                except Exception as Ex:  # printing the exception of the assistant
                    print("Pycharm not found in the specificied location in the operating system", Ex)
            elif text_input == "pycharm" or text_input == "python best interpreter":
                try:
                    os.startfile("C:\\Program Files\\Python35\\Lib\\idlelib\\idle.pyw")
                    # --- This runs the pycharm Compiler which can be used for the Html or the python programming
                    # The Below function will be used to search on the browser and then show the desire result
                    return
                except Exception as Ex:
                    print(
                        "Sorry i was unable to open the IDle of python perhaps , its not found in the specified location",
                        Ex)
            elif text_input == "movie player":
                print("started movie player!!!")
                os.startfile("wmplayer.exe")  # window media player execution!
                return
            else:
                print("What you want to open or run ?")  # Debuggin
                self.text_to_speech("What do you want to open or run ")  # Debuggin
                return

    # TODO : Exact Searching
    def search_browser(self, text_input):
        print('-searching on browser-')
        try:
            url = 'http://google.com/search?q=' + text_input
            # Creating or generating a google link for the particular file
            webbrowser.open(url)
            return

        except Exception as Ex:
            self.text_to_speech(
                "I'm sorry, I couldn't reach google", Ex)
            # Calling the Function so that it can be identified that ,machine can speaks for itself
            return

    # Below is the code for searching on yahoo.
    def search_yahoo(self, text_input):
        try:
            self.text_to_speech("Searching on yahoo")  # Voice Message
            url = "https://search.yahoo.com/search;_ylc=X3oDMTFiN25laTRvBF9TAzIwMjM1MzgwNzUEaXRjAzEEc2VjA3NyY2hfcWEEc2xrA3NyY2h3ZWI-?p=" + text_input.replace(
                " ", "+") + "&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8"
            webbrowser.open(url)  # opens the search query
            self.text_to_speech("Yahoo search has been displayed ")
        except Exception as E:
            print("Problem reaching to yahoo, perhaps you have no internet connection")
            self.text_to_speech("Connecting to yahoo failed, there must be a connection problem")

    # Below is the code to search on the bing website
    def search_bing(self, text_input):
        print('-searching on browser-')
        try:
            url = 'http://www.bing.com/search?q=' + text_input.replace(" ", "+") + "&qs=n&form=QBLH"
            # Creating or generating a google link for the particular file
            webbrowser.open(url)
            return

        except:
            self.text_to_speech(
                "I'm sorry, I couldn't reach bing")
            # Calling the Function so that it can be identified that ,machine can speaks for itself
            return

    # Below is the function responsible for the searching of the wallpaper on the web
    def search_wallpaper(self, search_input):
        try:
            link = "http://www.wallpaperup.com/search/results/" + search_input.replace(" ", "+")
            webbrowser.open(link)  # Opens the links for the wallpaper
            self.text_to_speech("Found some of the wallpapers regarding to" + search_input)
        except Exception as Ex:
            print("There was an error finding the exact wallpaper", Ex)

    # The below function is responsible for the search on the Wikipedia

    # searching on the Wikipedia and then asking the pysha to speak the respectable result!!

    # TODO : WIkI Algorithm improvements
    def search_wiki(self, text_input):
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
        except Exception as Ex:
            self.text_to_speech(
                "Sorry i couldn't connect to the wikipedia!! nor find a relevant link, there must be a connection problem",
                Ex)
            return

    def search_quora(self, text_input):
        try:
            search_string = text_input.replace(" ", "+")
            search_link = "https://www.quora.com/search?q=" + search_string
            self.text_to_speech("Searching on Quora")
            webbrowser.open(search_link)  # Opening the link on search quora
            self.text_to_speech("Result have been Displayed")
        except Exception as Ex:
            print("There was an Error in the Quora, in function search_quora", Ex)  # Exception Raised

    def search_pc_part_picker(self, text_input):
        text_input = text_input.replace(" ", "+")  # This creates the search string
        search_url = "https://pcpartpicker.com/search/?q=" + text_input
        self.text_to_speech("Searching on pc part picker")
        webbrowser.open(search_url)
        self.text_to_speech("Found some things , have a look ! ")

    # Getting the news from the web.
    def get_news(self):
        try:
            news_string = self.newscheck.national_news()  # Get the national news from the __newsupdate.py file
            self.text_to_speech(news_string)  # Speaks out the news about the particular things (current)
            return news_string  # The function will return the current news from the web
        except Exception as Ex:
            print("There was an error retrieving the news :", Ex)
            self.text_to_speech("Sorry i could not connect to news center , database failure")
            return None  # returns none in case of failuire

    # The below function is responsible for the running of the chat with the below function
    # This will be used to show the Frontend for the application.

    # There are two dynamic ways for storing the Frontend , since this is a Hit and run trail using the function!
    # The Human computer interaction will be updated according to the software development module!

    # TODO: Frontend HCI needs to be created !
    def frontend_hci(self, label_text):
        try:
            root = Tk()  # This created the tkinter , face.!
            root.title("PYSHA 1.0")  # Making the Title for the Py Sha 1.0 ,
            root.geometry("300x300")  # specifying the x and the y axis in the scenario
            label1 = Label(root, text=label_text, font='size,25')  # This is the label insertion for the Tkinter module
            print(label1)  # Showing in the console for the debuggin purposes
            label1.pack()  # Packing up the label1 module in the GUI
            root.after(10000, lambda: root.destroy())  # Destroying after 10 seconds
            root.mainloop()  # Executing the main loop for the Gui Till it gets exited
            return
        except Exception as Ex:
            print("unable to create the front end for the User interface . ", Ex)
            return

    # TODO : make the Chat intelligent , using the Natural language processing and AIML (artifical intelligence markup)
    #  language)
    def chat(self, input):
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

    # When there is a question regarding to the self
    # Like the questions given to the Pysha, or the personal question about her !
    # Since , The below Function is an already stored function by the developer, there are some processed required like
    # Machine learning should be implemented in here too, for the particular specific questions
    # TODO : Do some of the Complex parsing
    def Personal_PYSHA(self, text_input=""):
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
                return
                # This will send all the related hobbies to the specified Place.
        elif text_input == "gender":
            self.text_to_speech("Female")
            return
        elif text_input.__contains__("how is your name") or text_input.startswith("why is your name"):
            list_responces_how = ["because my creator is Shafay, He should be answering this question.",
                                  "i did asked Shafay most of the time but he says its way too technical",
                                  "What can i say, perhaps is PYTHON SPEECH ON HAND ASSISTANT :p , what i "
                                  "think, he named me after his name and language which is  PYTHON SHAFAY (PY SHA)",
                                  "Because I am the one who is created using python language and shafay's brain",
                                  "Well, How are you using my algorithms then ? if you don't know the answer",
                                  "Shafay is my Chief Executive Officer CEO, He named me because of his name "
                                  "and his favourite language",
                                  "Shafay PYTHON makes more sense to humans, if you are in a computer field, "
                                  "it should be Python Speech on hand assistant"
                                  ]
            random_select = random.randint(0, len(list_responces_how) - 1)  # gets the random responce from the list
            selected_input = list_responces_how[random_select]
            print(selected_input)  # Debugging purpose.
            self.text_to_speech(text_input=selected_input)
            return

    # this is the particular day check , that the user will be defining the day check ,since the day
    #  Follows the same day check priciple for the  particular day check<!

    # TODO NOTHING
    def day_check(self):
        current_date = datetime.datetime.now()  # gets the current date from the datetime module
        self.text_to_speech("The current date is " + str(
            current_date.date()))  # Convert the current date time module and then specifying to the user.
        return

    # Checking the time for the computer while the

    # IF the user asked for the particular time check , after the text processing this function is called ! ,
    # This later calls the text to speech function using the P.y.t.t.s.x. for the user to speak the particular output !
    # TODO : Nothing
    def time_check(self):
        current_time = time.strftime('%H:%M:%S')
        self.text_to_speech("The time is " + current_time)
        return

    # TODO : add live streaming

    def watch_live_sports_stream(self, text=""):
        if text == "boxing":
            webbrowser.open(
                "http://www.stream2watch.cc/livenow/boxing/")  # opens up the webbrowser for the specified link
        elif text == "wrestling":
            webbrowser.open("http://www.stream2watch.cc/livenow/wrestling/")  # opens up the link for the wresting
        elif text == "athletics":
            webbrowser.open("http://www.stream2watch.cc/livenow/athletics/")
        elif text == "basketball":
            webbrowser.open("")
        elif text == "beach soccer":
            webbrowser.open("http://www.stream2watch.cc/livenow/beach-soccer/")
        elif text == "baseball":
            webbrowser.open("http://www.stream2watch.cc/livenow/baseball/")
        elif text == "cricket":
            webbrowser.open("http://www.stream2watch.cc/livenow/crick/")
        elif text == "UFC":
            webbrowser.open("http://www.stream2watch.cc/livenow/ufc/")
        elif text == "hockey":
            webbrowser.open("http://www.stream2watch.cc/livenow/hockey/")
        elif text == "snooker":
            webbrowser.open("http://www.stream2watch.cc/livenow/snooker/")
        elif text == "football":
            webbrowser.open("http://www.stream2watch.cc/livenow/football/")

    # storing the respectable input for the user  while the computer will be able to use the resources and speak

    # TODO: add sqlite3 database and store the input in the form of the data base
    def store_userinput(self, input_check):
        self.db.insert_into_History(str(input_check))  # this stores and creates a history
        # file_out = open("USERINPUT.txt", "a")
        # file_out.writelines("USER SAID: \t" + input_check)
        # file_out.write("\n")  # ending the line with the next line
        # file_out.close()  since we don't need to write in the file now
        return
        # This function will be responsible for storing the responses so that it may able to answer in the future.pute

    # Converting the spoken string to the speech , so that the call is Visible

    # TODO : speech to Text   (Google api, Microsoft Speech recording )
    def speech_to_text(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            # print(r.energy_threshold)
            print("Chucking rate: ", source.CHUNK)
            print("format rate :", source.format)
            # CHUNK = 1024
            # FORMAT = pyaudio.paInt16  # the Format is picked up from the pyaudio
            # CHANNELS = 2  # The Cross Channels
            # # RATE = 44100
            # source.CHUNK = CHUNK
            # source.format = FORMAT  # FORMATING THE SOURCE FILE
            # print(dir(source))
            print("Say something!...")
            # print(r.energy_threshold)
            r.energy_threshold += 280
            # # print(r.adjust_for_ambient_noise(source,duration=1))
            audio = r.listen(source)

            # Speech recognition using Google Speech Recognition
        try:
            print("Parsing ...")  # Debugging To
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            # print(r.energy_threshold )
            # print(help(r.recognize_google))
            # text = r.recognize_google(audio, language='en-US')
            text = r.recognize_google(audio, language='en-GB')  # Recognizing the command through the google
            # r.re
            # r.re
            print("You said: " + text)
            self.total_saying = text
            self.process_text_input(self.total_saying)
            return text  # returning the text which has been inputed.
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return
        except sr.HTTPError as e:
            print("Couldn't connect to the websites perhaps , Hyper text transfer protocol error; {0}".format(e))
            return  # returning for the debugging 

    '''Optional Other methods for the recognition of the voice texts using the other api's'''

    def read_out_pdf(self):
        pass

    # with sr.Microphone() as source:
    #     print("Say something!")
    #     audio = r.listen(source)
    #
    # # recognize speech using Sphinx
    # try:
    #     print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    # except sr.UnknownValueError:
    #     print("Sphinx could not understand audio")
    # except sr.RequestError as e:
    #     print("Sphinx error; {0}".format(e))
    #
    # # recognize speech using Google Speech Recognition
    # try:
    #     # for testing purposes, we're just using the default API key
    #     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    #     # instead of `r.recognize_google(audio)`
    #     print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    # except sr.UnknownValueError:
    #     print("Google Speech Recognition could not understand audio")
    # except sr.RequestError as e:
    #     print("Could not request results from Google Speech Recognition service; {0}".format(e))
    #
    # # recognize speech using Google Cloud Speech
    # GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
    # try:
    #     print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio,
    #                                                                             credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
    # except sr.UnknownValueError:
    #     print("Google Cloud Speech could not understand audio")
    # except sr.RequestError as e:
    #     print("Could not request results from Google Cloud Speech service; {0}".format(e))
    #
    # # recognize speech using Wit.ai
    # WIT_AI_KEY = "INSERT WIT.AI API KEY HERE"  # Wit.ai keys are 32-character uppercase alphanumeric strings
    # try:
    #     print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
    # except sr.UnknownValueError:
    #     print("Wit.ai could not understand audio")
    # except sr.RequestError as e:
    #     print("Could not request results from Wit.ai service; {0}".format(e))
    #
    # # recognize speech using Microsoft Bing Voice Recognition
    # BING_KEY = "INSERT BING API KEY HERE"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
    # try:
    #     print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
    # except sr.UnknownValueError:
    #     print("Microsoft Bing Voice Recognition could not understand audio")
    # except sr.RequestError as e:
    #     print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
    #
    # # recognize speech using Houndify
    # HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID HERE"  # Houndify client IDs are Base64-encoded strings
    # HOUNDIFY_CLIENT_KEY = "INSERT HOUNDIFY CLIENT KEY HERE"  # Houndify client keys are Base64-encoded strings
    # try:
    #     print("Houndify thinks you said " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID,
    #                                                              client_key=HOUNDIFY_CLIENT_KEY))
    # except sr.UnknownValueError:
    #     print("Houndify could not understand audio")
    # except sr.RequestError as e:
    #     print("Could not request results from Houndify service; {0}".format(e))
    #
    # # recognize speech using IBM Speech to Text
    # IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
    # IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
    # try:
    #     print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME,
    #                                                                   password=IBM_PASSWORD))
    # except sr.UnknownValueError:
    #     print("IBM Speech to Text could not understand audio")
    # except sr.RequestError as e:
    #     print("Could not request results from IBM Speech to Text service; {0}".format(e))
    # if you want to record for the specific interval of time

    # The duration ins specified by the user, since the default value passed from the main funtion is 7 seconds,
    # since the short term memory duration is 5 +- 2 So , for the maximum iof seven seconds.!!!
    # TIps : Using the Wave , which is built by the microsoft
    # TODO : Record something for the local machine and then go for the data that is to be parsed .!

    def record_something(self, duration):
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
                        frames_per_buffer=CHUNK)
        # Creating the stream and specifing the access channels , and the rate, Input to be on.

        print("* recording, Ask me something!")  # Just a Message to tell the user that the Voice is being recorded

        frames = []  # A list of frame is created which is

        for i in range(0, int(
                                RATE / CHUNK * RECORD_SECONDS)):
            # This is the Rate(bit rate) / Chuncks to be recorded * the Seconds
            data = stream.read(CHUNK)  # Reading the dat afrom the stream
            frames.append(data)  # Adding the each data to the frame list and appending it up.

        print("* done recording")
        print("Processing the input................")

        stream.stop_stream()  # Stopping the stream so that the stream(recorder for audio is stopped )
        stream.close()  # Closing the stream of the audio
        p.terminate()  # Termination the Py AUDIO Module cause it was accesses

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')  # Accessing the WAV
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    #
    # Converting the text to speech using the pysha personal assistant and then specifying the input!
    '''  BELOW ARE THE FUNCTIONS FOR THE ENGINE change regarding to Text to Speech
    '''

    # Machine Speaking!
    def text_to_speech(self, text_input='HI!'):
        self.engine.say(text_input)
        self.engine.runAndWait()
        self.engine.stop()
        '''Adding the changing of the voices according to the specified module
        , since the module will be changing the applications'''
        #

        return

    # TODO: Add additional Voices such as  child voice and later onward , create an algorithum so that we can have voice
    # TODO: The accent of the particular region and the people voices should also be considered
    # Creating the function for the changing of the voice of the module
    def change_person(self, name='', gender=''):
        self.engine = None  # setting the engine to NONE
        if name != '':  # make it more intelligent
            if name == 'hazel':
                self.engine = _chooseassitant.change_byname('hazel')
            elif name == 'david':
                self.engine = _chooseassitant.change_byname('david')  # changing the name to david
            elif name == 'zira':
                self.engine = _chooseassitant.change_byname('zira')  # Changing the engine to zira
            return
        elif gender != '':
            if gender == 'male':
                self.engine = _chooseassitant.change_gender('male')  # Changing the assistant by gender --> daVid
            else:
                self.engine = _chooseassitant.change_gender('female')  # female gender assistant
            return
            # TODO : Add More additonal voices and other things

    ''' Ending of the functions of the system change regarding to the engine text speech
    '''

    def volumeupdate(self, status_value=''):
        assert status_value != '', 'Value should have been not emptied'  # Debugging purpose
        if status_value != '':
            try:
                self.engine = _chooseassitant.volume_update(status_value)  # Updating the status of the engine
            except Exception as Ex:
                print("There was an error while updating the assistant  Volume", Ex)
                self.text_to_speech("Unable to change the status of volumne")
        else:
            print("--------Volume status---------")  # just for debugging purpose
        return  # returning

    # This function is responsible for the defining of the particular session and
    # then recording the particular input, and working on the continuous
    # Recognition of the voice.!
    # TODO: Responsible for recording the audio in the wave format
    def speech_to_text_wav(self, file_to_recognize):
        r = sr.Recognizer()

        with sr.WavFile(str(file_to_recognize)) as source:  # use "test.wav" as the audio source
            audio = r.record(source)  # extract audio data from the file

        try:
            total_saying = r.recognize_google(audio)
            # total_saying = r.recognize_sphinx()
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
        except KeyError:  # Key error
            print("Invalid API KEY ERROR")
        except sr.UnknownValueError:
            print("UNKNOWN!!")

        def save_to_txt(self, text_data, file_name):
            file_name = ((file_name.replace(".pdf", ".txt")).replace(".docx", ".txt")).replace(".doc",
                                                                                               ".txt")  # Renaming the file to txt
            exact_path = ntpath.basename(file_name)
            # if not os.path.exists(self.dir_path+"\\ConvertedTexts"):
            #     os.makedirs(self.dir_path+"\\ConvertedTexts")
            # file_writer = open(self.dir_path+"\\ConvertedTexts\\"+str(file_name), "w")  # Writing option in the file
            if not os.path.exists(self.dir_path + "/ConvertedTexts"):
                os.makedirs(self.dir_path + "/ConvertedTexts")
            file_writer = open(self.dir_path + "/ConvertedTexts/" + exact_path, "w")  # Writing option in the file
            # file_writer = open(file_name, "w")  # Writing option in the file
            # print(text_data.encode('utf-8'))
            file_writer.writelines(str(text_data.encode('utf-8')))  # Writes to a file
            file_writer.close()  # Closes the file writer.

        # The below function is responsible for the reading of the pdf File
        def readPDF(self, pdfFile):
            try:
                rsrcmgr = PDFResourceManager()  # Creates the resource manager
                # resource_mang = PDFResourceManager()
                retstr = StringIO()  # string object for the representation of the pdf
                # string represetnation from string input and output module
                laparams = LAParams()  # Parameters Object Creation
                device = TextConverter(rsrcmgr, retstr, laparams=laparams)  # Creating the device for the conversion
                process_pdf(rsrcmgr, device,
                            pdfFile)  # Process the specific pdf, to convert into string representations
                device.close()  # Closes the device.
                # print(retstr) # Debuggin
                # Decoded value is returned here UTF-8
                content = retstr.getvalue()  # gets the text from the string object
                # print(content)5
                return content  # Returns the content where its called
            except Exception as Ex:
                print("While reading the file , there was an error in the function Readodf as :",
                      Ex)  # printing the exception

        # Check case for the pdf
        def testpdf(self):
            try:
                pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")  # Gettting from the web
                print("Converting ...")
                # print(pdfFile)
                outputString = self.readPDF(pdfFile)  # Calls the function to read from the pdf
                # pdfFile.close() # Closes the pdf File
                print("Conversion Completed")  # Debugging
                return outputString  # this returns the output string for the specified format
            except Exception as Ex:
                print("Unable to convert the pdf to text due to : ", Ex)  # Printing the Exception
                # print(Ex)  # DEBUGGING
                print("In function testpdf")  # Testing
            finally:
                pdfFile.close()  # keep in mind to close the file which you are working on !

    # The following function will be responsible for the text to be parsed regarding to the certain input.

    # The below function is responsible for the text processing of the Total saying
    #  since what the user i ssaying is recorded in this
    # TODO : add in the other parts as specified in the requirements , such as face recogniton and the voice recognition !
    def process_text_input(self, total_saying=""):
        self.total_saying = total_saying.strip()  # Stripping the string for the extra white spaces
        total_saying = self.total_saying.lower()  # Converting a string to lower case
        self.total_saying = self.total_saying.lower()  # Debugging purpose
        if self.total_saying == "quit" or self.total_saying == "stop listening" or total_saying == "stop" or \
                        self.total_saying == "exit":
            self.store_userinput("quit")
            self.text_to_speech("BYE Keep working.")
            os._exit(0)  # exiting the program
        else:
            # this stores the Specified Input we said Regerding to something
            # Textual_Analysis(total_saying)
            '''
                Below is the place where are your working on!!!

                '''
            if total_saying.__contains__("stop listening both of you") or total_saying.__contains__(
                    "stop listening Anna"):
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

            elif total_saying.startswith("bing") or total_saying.startswith("search bing") \
                    or (total_saying.startswith("search") and total_saying.__contains__("bing")):
                self.text_to_speech("Searching on bing")
                self.total_saying = total_saying.replace("search for", "")
                self.total_saying = self.total_saying.replace("bing", "")
                self.total_saying = self.total_saying.replace("search bing", "")  # Texts filtering
                self.total_saying = self.total_saying.replace("search", "")
                self.store_userinput("searching on bing :" + self.total_saying)  # storing the texxt input in the bing
                self.search_bing(self.total_saying)  # Calling the bing function
                self.search_bing("Bing result have been displayed")

            elif total_saying.startswith("search yahoo") or total_saying.startswith(
                    "yahoo search") or total_saying.startswith("search on yahoo"):
                self.total_saying = total_saying.replace("search yahoo", "")
                self.total_saying = self.total_saying.replace("yahoo search", "")
                self.total_saying = self.total_saying.replace("search on yahoo", "")
                self.search_yahoo(self.total_saying)  # Calling the Yahoo search
                print("-^-^-")

            elif self.total_saying.startswith("search on quora") or self.total_saying.startswith("quora search"):
                self.total_saying = self.total_saying.replace("search on quora", "")
                self.total_saying = (self.total_saying.replace("quora search", "")).strip()  # Data filtering
                self.store_userinput("search on quora : " + str(self.total_saying))  # Passing in the input
                self.search_quore(self.total_saying)  # Searching on the quora for the stuff

            elif total_saying.startswith('social media'):
                self.store_userinput(total_saying)  # this stores the particular input.
                browse_key = total_saying.replace('social media',
                                                  '')  # Replacing the total saying variable value'd (social media with empty string)
                browse_key = browse_key.strip()  # removing the extra white spaces
                sma = SocialMedia()  # Creating the social media object
                sma.social_media_access(
                    browse_key=browse_key)  # Passing the browser key to the social media access function.

            elif (total_saying.__contains__('wikipedia') and total_saying.startswith('search')) or \
                    self.total_saying.__contains__("wiki pedia") or (
                        total_saying.__contains__('on wikipedia') and total_saying.startswith('search')):
                total_saying = total_saying  # this converts the string to the lower case
                total_saying = total_saying.replace('search', '')  # replacing the start with the empty string
                total_saying = total_saying.replace('on wikipedia', '')  # replacing the on wikiepdia with empty string
                total_saying = total_saying.replace('wiki pedia', '')
                self.text_to_speech('Searching on Wikipedia')
                retrieved_link = self.search_wiki(
                    total_saying)  # calling the wikipedia search function , for the results
                self.lastlink = retrieved_link
                print(self.lastlink)

            elif total_saying.startswith("what is the date") or total_saying == 'date':
                # Here you will be required to input the date
                self.day_check()  # This calls the day check

            elif total_saying.startswith("what is the time") or total_saying == 'time' or \
                    total_saying.startswith("what time it is"):
                self.time_check()  # this checks the current time according to the specified state

            # Create a Grammer , that represents the questions regerding to the respectable machine

            # TODO: Working on the changing of the Assistant and others.
            elif total_saying.startswith("switch to") or self.total_saying.startswith("want to talk to someone else"):
                self.total_saying = total_saying.replace("switch to", "")  # replacing the text string
                self.total_saying = self.total_saying.strip()  # stripping the white spaces
                self.db.insert_into_History("Switch to:" + self.total_saying)  # adding the string in the database
                # assert self.total_saying not in ['male', 'female', 'david', 'zira',
                # 'hazel'], "You haven't selected the correct list"  # Debugging purpose
                Assistant_string = self.total_saying
                if Assistant_string in ['male', 'female']:
                    self.change_person(gender=Assistant_string)  # Changing on the basis of gender
                    self.text_to_speech("I am here Shafay , Ask your query ")
                elif Assistant_string in ['david', 'hazel', 'zira', 'anna', 'lizy']:
                    if Assistant_string == 'anna':
                        self.change_person(name='hazel')
                    elif Assistant_string == 'lizy':
                        self.change_person(name='zira')
                        pass
                    else:
                        self.change_person(name=Assistant_string)  # Changing on the basis of name
                        self.text_to_speech("I am here Shafay , Ask your query ")
                else:
                    self.text_to_speech("Who you want to switch to")

            elif self.total_saying.startswith("what is your") or self.total_saying.startswith(
                    "your name") or self.total_saying.startswith("how is your name") or total_saying.startswith(
                "why is your name"):
                # here you need to create the question saying file so that the file is readable.
                '''
                    Write the Respectable question in this format so that, the Agent learns from the file.

                    '''
                self.store_userinput("Personal Question asked :" + self.total_saying)  # Asking the personal question.
                self.total_saying = total_saying.replace("what is your ", "")
                # self.total_saying = self.total_saying.replace("how is your name ", "")
                # replacing the words so that it will be easier for the program to Check the last thing
                self.Personal_PYSHA(text_input=self.total_saying)
            # Switching to text mode .
            elif total_saying.startswith("text mode"):
                tm = TextMode()
                # this calls the text mode function, and there we can do the processing in the form of the text!
                tm.text_mode(total_saying)  # Passes the total saying to the Class Function!

            elif total_saying in ["who created you", "who invented you", "who build you", "who is your creator",
                                  "who is your CEO"]:
                self.total_saying = total_saying.replace("who created you", "")
                self.total_saying = self.total_saying.replace("who invented you", "")  # filterning
                self.total_saying = self.total_saying.replace("who build you", "")
                self.total_saying = self.total_saying.replace("who is your ceo", "")
                self.total_saying = self.total_saying.replace("who is your creator", "")
                required_text_list = [" created me", "Shafay is my CEO", "Shafay is my creator",
                                      "Well , Shafay build me from header files and his brain"]
                selected_index = random.randint(0, len(required_text_list) - 1)
                self.text_to_speech(required_text_list[selected_index])  # Speaking

            elif total_saying == "show me a comic" or total_saying == "show me the comic":
                self.store_userinput("show me a comic")  # finding the comic from the web
                joke_object = Joke()  # creating an object of ht Joke class !
                self.text_to_speech("Finding a Comic the Database")
                joke_object.Image_Joke()
                # Calls the Joke class Image Joke Object to show a Joke in the form of an image

            elif total_saying == "tell me a joke" or total_saying == "tell me another joke" \
                    or total_saying == "joke please":
                print("JOKE JOKE JOKE!!!")
                self.store_userinput("tell me a joke")
                joke_object = Joke()
                self.text_to_speech("OH wait")
                joke_text = joke_object.joke_category()  # Calls any nerdy or Explicit joke about Chuck Norris.!
                # frontend_HCI(Joke_Text)  # calling the tkinter library to create the joke for the particular thing ,
                print(joke_text)
                # This is the Joke text , which will be printed in the console ,since we don't have much time ,
                # working for the Console.!
                self.text_to_speech(joke_text)  # Speaking up the joke (By machine ) PYSHA <3

            elif self.total_saying.startswith("open url") or self.total_saying.startswith("find url"):
                # self.store_userinput("opening url :")

                text_to_search = self.total_saying.replace("open url", "")
                # search_first_link(text_to_search)

            elif total_saying.startswith("open") or total_saying.startswith("run"):
                self.store_userinput(total_saying)  # This stores the Data in the Us
                # er input file so that the history is kept
                total_saying = total_saying.replace('open ', '')  # replacing the word open with the Total_saying!
                total_saying = total_saying.replace('run ', '')  # This is the replacement of the run with the
                self.run_apps(total_saying)  # This is the total saying being passed to the Running apps. !

            # Closing the application for the Derived Module

            elif total_saying.startswith("close") or self.total_saying.startswith(
                    "terminate") or self.total_saying.__contains__("close application"):
                self.total_saying = self.total_saying.replace("close", "")
                self.total_saying = self.total_saying.replace("terminate", "")
                self.total_saying = self.total_saying.replace("close application", "")
                self.total_saying = self.total_saying.strip()
                self.store_userinput("Closing Application: " + str(self.total_saying))
                # print("->",self.total_saying,"<-") # Debugging
                self.close_program(self.total_saying)  # Calling the closing function to close programs
                # self.text_to_speech("Application has been closed") # Voice Message
                # The below functioon will tell the specified news for the particular thing
            elif total_saying.startswith("news updates") or self.total_saying.startswith(
                    "what's on news") or self.total_saying.startswith(
                "what is on the news") or self.total_saying.startswith("news update"):
                self.store_userinput("News check :")
                self.get_news()  # Calls in the function self.newscheck and retrieve the news
            elif total_saying.startswith('parse sentence') or total_saying.startswith(
                    'parse this') or total_saying.startswith('tokenize this'):
                self.store_userinput(total_saying)
                total_saying = total_saying.replace('tokenize this', '')
                total_saying = total_saying.replace('parse sentence',
                                                    '')  # replacing the total saying with the parse sentence
                self.total_saying = total_saying.replace('parse this',
                                                         '')  # replacing the total saying of the parse this with none !
                np = NaturalProcessing()  # creating the object of the classes
                # -------------You are working here -------------
                tokenized_sentences_return = np.word_tokeniztion(
                    self.total_saying, sent_tokenized=False)  # this parse the Np with the tokenizing of the words
                print(tokenized_sentences_return)  # this prints the Tokenize the words

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
                # TODO: make it more perfect, for searching on youtube.
                '''Finding the playlist on the youtube for the specified search query '''
                if self.total_saying.__contains__("playlist") or self.total_saying.__contains__(
                        "play list") or self.total_saying.__contains__("playlists"):
                    try:
                        self.total_saying = self.total_saying.replace("playlist", '')
                        self.total_saying = self.total_saying.replace("play list", '')
                        self.text_to_speech("Finding the playlist from youtube.")
                        self.lastlink = Y.search(search_text=self.total_saying,
                                                 play_list=True)  # Searched for the playlist
                        self.text_to_speech("I Guess i found some , have a look at these.")
                        return
                    except Exception as Ex:
                        print("EXCEPTION occurred as :", Ex)  # Printing the exception
                        self.text_to_speech("Sorry i was unable to find the playlist on youtube")
                        return
                # If we search for a single link rather than a play list ,

                else:
                    self.lastlink = Y.search(
                        search_text=self.total_saying)  # Sends the Total Saying to the Youtube Search Function
                    self.text_to_speech('Youtube Result , Best match found')
                    '''Stackoverflow searching on the specified pattern'''

            elif total_saying.startswith('stack over flow') or total_saying.startswith(
                    'stackoverflow') or total_saying.startswith("stack overflow") or total_saying.startswith(
                'search stack over flow') or total_saying.startswith('stack search') or total_saying.startswith(
                'search stackoverflow'):
                try:
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
                    return
                except Exception as Ex:
                    print("Unable to connect to the stackoverflow :", Ex)
                    self.text_to_speech("Sorry i was unable to connect to stackoverflow")
                    return
                '''Music search on Sound Cloud and finding the music on soundcloud , calls the __soundcloud.py'''

            elif total_saying.startswith("search music") or total_saying.__contains__(
                    "search music") or total_saying.__contains__("find music") or \
                    total_saying.__contains__("search soundcloud"):
                try:
                    self.total_saying = total_saying.replace('search music',
                                                             "")  # replacing the search music with empty
                    self.total_saying = self.total_saying.replace("search music", '')
                    self.total_saying = self.total_saying.replace("search soundcloud", '')
                    self.total_saying = self.total_saying.replace("find music", '')
                    self.total_saying = self.total_saying.replace("music", '')
                    self.text_to_speech("I Found some of the result")
                    SoundCloudSearch(self.total_saying)
                    self.text_to_speech("Seems like this was the music you were looking for")
                except Exception as Ex:
                    print("Unable to Connect to sound cloud perhaps there is a connection problem", Ex)  #
                    # Printing the exception
                    self.text_to_speech("Sorry i was unable to connect to the sound cloud")  # Text to speech

            elif self.total_saying.startswith("search wallpaper") or self.total_saying.startswith("find wallpaper") \
                    or self.total_saying.startswith("find wallpapers for me") or self.total_saying.startswith(
                "find a wallpaper for me"):

                try:
                    self.total_saying = self.total_saying.replace("search wallpaper", "")
                    self.total_saying = self.total_saying.replace("find wallpaper", "")
                    self.total_saying = self.total_saying.replace("find wallpapers for me", "")
                    self.total_saying = self.total_saying.replace("find a wallpaper for me ",
                                                                  "")  # Replacing the Sentence
                    self.total_saying = self.total_saying.strip()  # Striping the white spaces from the both of the side.
                    self.text_to_speech("Finding the wallpaper for you !")  # Voice
                    self.search_wallpaper(self.total_saying)  # Finds the Wallpaper from the website
                except Exception as Ex:  #
                    print(
                        "Sorry i wasn't able to find the specified wallpaper for you because there was a connection problem",
                        Ex)
                    self.text_to_speech("Sorry i wasn't able to find")

                self.text_to_speech("Found Wallpapers for : ", self.total_saying)  # Text to speech -->

                '''Searching on the Github for the specified repository or the c'''
            elif self.total_saying.startswith("github search") or self.total_saying.__contains__("github") or \
                    self.total_saying.startswith("search on github"):
                try:
                    self.total_saying = self.total_saying.replace("github search", "")
                    self.total_saying = self.total_saying.replace("github", "")
                    self.total_saying = self.total_saying.replace("search on github", "")
                    self.store_userinput("search on github: " + self.total_saying)
                    GS = GitHubSearch()  # Creating the class for the github search
                    self.text_to_speech("Searching on github")
                    GS.search(self.total_saying)  # searching on the Github
                    self.text_to_speech("Found somethings on github")
                    return
                except Exception as Ex:
                    print("Sorry I was unable to connect to github", Ex)
                    self.text_to_speech("Sorry I was unable to connect to GitHub")  # text to speech conversion

                """Playing the music below"""
            elif total_saying.startswith("play music") or total_saying.__contains__("music please"):
                try:
                    self.total_saying = total_saying.replace("play music", "")
                    self.total_saying = self.total_saying.replace("music please", "")  # replacing the string !
                    self.text_to_speech("Playing Music")
                    self.play_video()  # plays the video
                    self.music_check_indicator = 1  # when this is one you can move in between the music
                    self.text_to_speech("Music Video has been played")
                    # MP_gui = main()
                    # MP_gui.run()
                    # ime.sleep(1)  # Sleeps the computer for 4 seconds. so that the user can listen to the Sound
                    self.store_userinput("playing music")
                except Exception as Ex:
                    print("Unable to play the music", Ex)  # Unable to play the music .!

            elif total_saying.startswith("next music") or total_saying.__contains__("next music"):
                try:
                    if self.music_check_indicator == 1:
                        self.music_player.control_player("next music")  # This will play the next music
                    else:
                        print("You are not even playing any music :/ ")  # Debugging purpose !
                        self.text_to_speech("you are not even playing any music")  # Text to speech conversion
                except Exception as Ex:
                    print("There was an error in the line 1479 - 1487")  # Debugging and error Exceptions

            elif total_saying.startswith("previous music"):
                try:
                    if self.music_check_indicator == 1:
                        self.music_player.control_player("previous music")  # Previous music is read out
                    else:
                        print("You are not even playing any music :/ ")  # Debugging purpose !
                        self.text_to_speech("you are not even playing any music")  # Text to speech conversion
                except Exception as Ex:
                    print("There was an error in the line (previous music)   ", Ex)

            elif total_saying.startswith("show image"):
                try:
                    responces_list = ["seems a little off", "ahan. sure wait up", "intresting this time", "Umhm"]
                    selected = responces_list[
                        random.randint(len(responces_list))]  # Getting the random responce for the specified thing
                    self.text_to_speech(selected)  # Speaks the particular output
                    self.image_check_indicator = 1  # Changes the value of the image check indicator
                    self.image_shower.display_image()  # Displaying the current image
                    # ------------------------------------------------------------------------------------------ #
                    # Working on the particular images
                    self.text_to_speech("Here you go bae")
                except Exception as Ex:
                    pass

            elif total_saying.startswith("next image"):
                try:
                    if self.image_check_indicator == 1:
                        self.text_to_speech("Moving to the next image ")
                        self.image_shower.view_image_file(self.image_shower.next_image())
                        # This calls in the next image.
                    else:
                        self.text_to_speech("Um , there is no Image being viewed mate")
                        # If there is no image there , then it will do that !
                except Exception as Ex:  # This is just for the exception detection ,
                    print("There was an error in the next image < -- ", Ex)

            elif total_saying.startswith("previous image"):
                try:
                    self.text_to_speech("aha! , interesting")
                    self.image_shower.view_image_file(self.image_shower.previous_image())
                    # Goes to the previous image and then displays
                    self.text_to_speech("all done boss")  # text to speech
                except Exception as Ex:
                    print("There was an Error in the line (previous image) ", Ex)  # Debugging
            # last link being read
            # This calls the Web scrap class in the __speakcode.py
            # TODO : Add the links to be dynamically updated from the last scrapped page
            elif total_saying.startswith("play video"):

                try:
                    self.text_to_speech("Playing Music Video for you")
                    self.play_video()
                    self.text_to_speech("Music Video played")
                except Exception as Ex:
                    print("Unable to play the music video because of :", Ex)  # printing the exception as

            elif total_saying.startswith("read it out to me") or total_saying.startswith("read it out for me"):
                # self.db.insert_into_History(total_saying + ":" + self.lastlink)
                self.store_userinput(total_saying + ":" + self.lastlink)
                self.total_saying = total_saying.replace("read it out to me", "")
                self.text_to_speech("Reading the Text from the website")
                WS = WebScrap()
                WS.scrap_link(self.lastlink)
                self.store_userinput(total_saying + ":" + self.lastlink)
            # This will call in the process to read the current pdf data ,
            elif total_saying.startswith("read pdf for me"):
                try:
                    pdf_file = self.fttf.get_pdf_files()
                    if len(pdf_file) != 0:
                        file_read = open(str(pdf_file[0]).replace("\\\\\\\\", "/"), "rb")  # specifying the pdf file to be read!
                        data = self.fttf.readPDF(file_read)  # Passing in the file buffer to the pdf file
                        self.text_to_speech(data)  # Reading the specific data. !
                except Exception as Ex:
                    print("There was an error in reading the pdf out.")
                    self.text_to_speech("line ")
                # Calling in the fttf to get all the pdf files from the psutill class.
                pass  # You are working here ! ! !

            elif total_saying.startswith("web"):
                self.total_saying = total_saying
                self.store_userinput("Web : opening " + self.total_saying)
                self.text_to_speech("opening the website for : ", self.total_saying)
                webbrowser.open(self.total_saying)

            elif self.total_saying.startswith("schedule update") or self.total_saying.startswith("schedule"):
                self.text_to_speech("Checking Schedule")
                self.schedule_check()  # calls the Schedule function to check the schedule
            elif total_saying.startswith("pause"):
                total_saying = total_saying.replace("pause").strip()
                if total_saying.strip() =="ten":
                    time.sleep(10) # Sleeps for ten seconds
                elif total_saying.strip() == "twenty":
                    time.sleep(20) # Waits for 20 seconds
            elif total_saying.__contains__("facebook status") or total_saying.startswith(
                    "post status on facebook") or total_saying.startswith("facebook post"):
                self.text_to_speech("posting the status on facebook")  # posting the status on facebook
                self.total_saying = total_saying.replace("facebook status ",
                                                         "")  # replacing the spaces with the non space typed.
                self.total_saying = self.total_saying.replace("post status on facebook", "")
                self.total_saying = self.total_saying.replace("facebook post ", "")  # replacing cleaning the data
                self.store_userinput(
                    "Facebook status post: " + self.total_saying)  # storing the input for the Facebook in the history
                FB_class = FB()  # Creating the facebook class for the pysha
                # Calling in the class which will return the boolean experession on the basis ofthe ate that is being returned
                boolean_condition = FB_class.post_status(
                    "ANOTHER TESTING OF POSTING STATUS")  # posting the message on facebook
                if boolean_condition:  # this is the boolean condition which is set true
                    self.text_to_speech("Status on facebook have been posted")
                else:
                    self.text_to_speech("Status posting was not possible, there is a problem reaching the facebook")
                    return

            elif total_saying.startswith("twitter status") or total_saying.startswith("post on twitter") \
                    or total_saying.startswith("status") or total_saying.startswith("post twitter"):
                self.total_saying = total_saying.replace("tweet ", "")  # text filter
                self.total_saying = self.total_saying.replace("twitter status ", "")
                self.total_saying = self.total_saying.replace("status ", "")
                self.total_saying = self.total_saying.replace("twitter status ", "")
                self.total_saying = self.total_saying.replace("post twitter", "")
                self.total_saying = self.total_saying.replace("post on twitter", "")
                # TODO: Replace your twitter credentials here
                # ckey = ''
                # csecret = ''
                # atoken = ''
                # asecret = ''
                try:
                    credential_read = [line.strip() for line in open("E:\PYSHA\Twitter_credentials", "r").readlines()]
                    ckey, csecret = credential_read[0], credential_read[1]
                    atoken, asecret = credential_read[2], credential_read[3]
                    TP = Twitter_PYSHA(ckey, csecret, atoken, asecret)  # create object and pass in values
                    api = TP._api_auth()
                    status = self.total_saying
                    self.store_userinput("tweeting on twitter:" + self.total_saying)
                    self.text_to_speech("tweeting on twitter :" + self.total_saying)
                    api.update_status(status)  # Posts the status om the twitter.
                except Exception as E:
                    print("your forgot to check the File destination please reconfigure the file", E)
                    self.text_to_speech("PYSHA sees twitter failure, shafay")

                self.text_to_speech("Tweet have been posted in your twitter account")

                # The below function is responsible for the sentimental analysis of the specified input
                # Keep in mind that hte dependencies are int the Sentimental analysis folder.
            # elif self.total_saying.startswith("sentimental analysis") or self.total_saying.startswith(
            #         "do sentimental analysis"):
            #     if self.total_saying == "sentimental analysis only":
            #         try:
            #             start_working()  # starts working on the specified stirng
            #         except Exception as Ex:
            #             print("There was an exception in the specified Sentimental analysis only", Ex)
            #     else:
            #         self.total_saying = self.total_saying.replace("sentimental analysis", "")
            #         self.total_saying = self.total_saying.replace("do sentimental analysis", "")
            #         self.store_userinput("SENTIMENTAL ANALYSIS ON: " + self.total_saying)
            #         try:
            #             download_tweets_call(self.total_saying)  # Passes the total saying for downloading the tweet
            #             start_working()  # performs the sentimental analysis
            #         except Exception as Ex:
            #             print("Unable to perform the sentimental analysis on the specified string", Ex)
            elif self.total_saying.startswith("write to a file") or self.total_saying.startswith(
                    "can you help me write to a file") \
                    or self.total_saying.startswith("write to a document") or self.total_saying.startswith(
                "file write"):
                self.store_userinput("COMMAND : Write to a File")
                self.text_to_speech("Sure i can write to a file though, Start speaking after i say GO")
                # time.sleep(1)  # Just for the notification of the Current time work
                self.text_to_speech("GO")
                WTF = Writing_to_file()  # This calls the Writing to the file
            elif self.total_saying.startswith("mouse") or self.total_saying.startswith(
                    "move mouse") or self.total_saying.startswith("move"):
                M_obj = mm.MouseMove()
                self.total_saying = self.total_saying.replace("mouse ", "")
                self.total_saying = self.total_saying.replace("move mouse", "")  # Data Filtering
                self.total_saying = self.total_saying.replace("move", "")  # Data filtering
                self.total_saying = self.total_saying.strip()  # Now there is a command
                self.store_userinput("COMMAND: Mouse Movement: " + self.total_saying)
                self.text_to_speech("Moving Mouse:" + self.total_saying)  # Debugging purpose
                M_obj.on_command_move(self.total_saying)  # Passing Command
                self.text_to_speech("Moved")  # Debugging purpose
            elif total_saying.startswith("mail") or total_saying.startswith("check email") or total_saying.startswith(
                    "check mail"):
                self.text_to_speech("Checking email")
                webbrowser.open("www.gmail.com")
                webbrowser.open("www.hotmail.com")
                webbrowser.open("www.yahoo.com")
                self.text_to_speech("You need to fill the credentials otherwise Machines will become terminator")
            elif total_saying.startswith("twitter"):  # opening the web browser as Twitter
                webbrowser.open("www.twitter.com")
            elif total_saying.startswith("reddit"):
                webbrowser.open("www.reddit.com")
            elif total_saying.startswith('which statements i said to you') or total_saying.startswith(
                    "what did i said you") or \
                    total_saying.startswith("what is in your shortterm memory") \
                    or total_saying.startswith("what is in your short term memory") or \
                    total_saying.startswith('what is in your ram') or total_saying.startswith("short term memory"):
                try:
                    self.shortterm_check()  # this calls the current Short term memory shuffled.
                except Exception as Ex:
                    print("The exception is :", Ex)  # This prints the specified exception
            # Checking in the last statment read by the assistant
            elif total_saying.__contains__("what did i just said to you") or total_saying.__contains__(
                    "what did i just said"):
                self.shortterm_check(limit=1)  # specifying the limit to 1 so that the last statements is returned
            # Going on line streaming !
            elif total_saying.startswith("live stream"):
                total_saying = total_saying.replace("live stream", "")  # Replacing the string of live stream with empty
                self.db.insert_into_History('live sports stream ::' + total_saying)
                self.text_to_speech("Finding the live stream for ", total_saying)  # This searches for the live stream
                watch_live_sports_stream(total_saying)  # Passing in the function !
            # Checking out the pc part picker list
            elif total_saying.startswith("pc part pick search") or total_saying.startswith(
                    "pc part search") or total_saying.startswith("pc part"):
                total_saying = total_saying.replace("pc part search", "")
                total_saying = total_saying.replace("pc part pick search", "")
                total_saying = total_saying.replace("pc part", "")
                self.text_to_speech("Searching on the pc part picker")
                self.search_pc_part_picker(total_saying)  # Calls in the function for
            # Reading the current pdf out for the specified user
            elif self.total_saying.startswith("read the pdf out for me") or self.total_saying.startswith("read the pdf") or self.total_saying.startswith("read pdf for me"):
                M = FilestoTextFiles()
                returned_data = M.get_pdf_files()  # This calls in the function to get all the pdf files from the stuff
                if len(returned_data) != 0:
                    returned_text = M.readPDF(returned_data[0])  # This will pass in the pdf file data to be read
                    self.text_to_speech(str(returned_text))  #
                    # This converts the text to speech of the specific co
                else:
                    self.text_to_speech("I Couldn't see any pdf file shafay")
            elif total_saying.startswith("How you doing") or total_saying.startswith("how are you doing"):
                try:
                    random_answers = ["quite fine", "almost fine you should ask david", "interesting you never ask this",
                                      "may be you should switch me"]
                    random_answer = random_answers[random.randint(0, len(random_answers) - 1)]
                    self.text_to_speech(random_answer)
                except Exception as Ex:
                    print(Ex)
            elif total_saying.startswith('what') or total_saying.startswith("when") or total_saying.startswith(
                    "how") or total_saying.startswith("where") or total_saying.startswith(
                "solve") or total_saying.startswith("who") or total_saying.startswith(
                "whom") or total_saying.startswith("why") or total_saying.startswith("which") or \
                    total_saying.startswith("show me"):

                try:  # Debugging
                    self.store_userinput('Question Asked : ' + self.total_saying)  # The question asked by the computer
                    # since this is a computation engine that will be used for the computation of the question asked .!
                    WFM = WolFrameAlphaClass()  # This is the Wolframalpha class intialization
                    # creating the wolframapla class that will be used for the creation of the api assistant
                    # self.text_to_speech('searching database')  # this is for responcing to the user
                    WFM_backstring = WFM.search_engine(
                        self.total_saying)  # this searches the WolframAlpha for the Search Strings
                    if WFM_backstring != "":  # if there is not string returned from the Wolfram alpha
                        # if the input returned from the Wolframalpha turns out to be null then leave it .
                        self.text_to_speech(WFM_backstring)  # this converts text to speech
                except Exception as Ex:  # Printing the exception
                    print("Unable to connect and Compute the required problem", Ex)  # Exception printing
                    self.text_to_speech("Unable to connect and compute the required problem")
            else:
                try:
                    # The below function calls the chat script of the file , so that you can be able to chat with it.
                    retrieved_output = self.py_chat_bot.retrieved_response(self.total_saying)
                    print("VA says : ",
                          retrieved_output)  # printing the Virtual Assistant for the specified speech to texgt
                    self.text_to_speech(retrieved_output)  # calls in the retrieved output
                    self.store_userinput("PYSHA Chat input: " + str(self.total_saying))  # adding inthe database
                    # Storing the input value in the db
                    # if not self.total_saying.__contains__('search'):
                    #     print("training ") # just for debugging
                    self.py_chat_bot.train_text(list(self.total_saying))
                    # trains on the basis of the user specified
                    # input
                    self.store_userinput("PYSHA Chat output" + str(retrieved_output))
                    # Storing the received value in db
                except Exception as ExceptionChat:  # debugging purpose
                    print("Couldn't find something , Check the bot specification :", ExceptionChat)  # Debugging


class Main_Call:
    # TODO : Make it a little more intelligent
    PYSHA_Obj = PYSHA_CLASS()  # Creating the P.Y.S.H.A class for hte main checking of the values

    def __init__(self):
        print("Main Class Initialized.....")

    def main(self):  # main program access
        print("-^-")
        # duration = float(input("How much time you need to record for ?"))
        # record_something(duration)  just trying to pause the thing
        client_id = ""  # this is the google api client id
        client_secret = ""  # this is the google api client secret key
        # speech_to_text()  # calling the function
        try:
            voices = self.PYSHA_Obj.engine.getProperty('voices')
            self.PYSHA_Obj.engine.setProperty('voice', voices[1].id)
            self.PYSHA_Obj.text_to_speech()  # Calls the virtual assistant to speech
            self.PYSHA_Obj.greetings_check()  # Calls in the greeting Function to check or greet
        except Exception as Ex_change:  # Exception as Ex
            print("Couldn't change the voice for the Virtual Assistant as per Shafay Liked :", Ex_change)  # debugging
        while True:
            '''-- if you want to record for 7 seconds as short term memory and have a bad microphone then'''
            # # try:
            # self.PYSHA_Obj.record_something(7)  # providing the Duration in the Record function!
            # self.PYSHA_Obj.speech_to_text_wav("output.wav")  # Converting the recorded format of WAV to speech!
            self.PYSHA_Obj.speech_to_text()  # Calling the Speech to text object
            # Calls the function automatically getting the queries. This is for live recording
            # The above the Audio has been recorded , and now the Audio needs to be converted into texts/
            # Machine Learning book + N.L.T.K. BOOK need to be studied  with Plotting and O.P.E.N.C.V.2.
            # Work with the MEGA VOICE COMMAND AFTER THE EXAM HAVE BEEN FINISHED.

# # if __name__ == '__main__':
# y = PYSHA_CLASS()
# # print(Py.shortterm_check())
# y.play_video()  # for playing music video just for testing
# ---
