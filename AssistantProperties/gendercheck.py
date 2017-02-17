import pyttsx

engine = pyttsx.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice.id)
    engine.setProperty('voice',voice.id)
    engine.say("The quick Brown Fox jumped over the lazy dog.")
    engine.runAndWait()