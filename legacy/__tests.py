import speech_recognition as sr
import pyttsx as pt


def speech_to_text():
    client_id = ""  # this is the google api client id
    client_secret = ""  # this is the google api client secret key
    api_key = ""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        #print(r.energy_threshold)
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
        #text = r.recognize_google(audio, language='en-US')

        text = r.recognize_google(audio, language='en-GB')
        # text = r.recognize_ibm(audio,"mshafayamjad@gmail.com", "shafay12332100s")
        # r.re
        # r.re
        print("You said: " + text)
        # self.total_saying = text
        # self.process_text_input(self.total_saying)
        return text  # returning the text which has been inputed.
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def speak(text):
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    while True:
        engine = pt.init()  # Creates the engine and then intializes the engine on the modeule of the data
        text = speech_to_text()
        speak(text)
