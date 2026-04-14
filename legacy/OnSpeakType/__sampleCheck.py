import speech_recognition as sr


class Writing_to_file:
    def __init__(self):
        total_saying = ""
        while True:
            temp = self.write_by_speak
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
        file_writer = open("OnSpeakType\\filedata.txt", "w")
        file_writer.write(text)
        file_writer.write("")
        file_writer.close()

    @property
    def write_by_speak(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
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
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return
        except sr.HTTPError as e:
            print("Couldn't connect to the websites perhaps , Hyper text transfer protocol error; {0}".format(e))
            return  # returning for the debugging


WTF = Writing_to_file()  # Calls in the Class !
