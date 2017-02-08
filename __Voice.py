import pyttsx

def checkvoice():
    engine = pyttsx.init()
    voices = engine.getProperty('voices') # checking the list of the voices
    pyttsx.voice.Voice.age = 5
    for voice in voices:
        print(voice.id)
        engine.setProperty('voice',voice.id)  # this gets the current voice id
        engine.say(" i like you shafay, what do you want me to do ? help you ?")
        engine.runAndWait()
# change the speed rate
def change_speed():
    pass
checkvoice()