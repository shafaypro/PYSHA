import pyttsx
import random


def change_gender(gender=""):
    try:
        Engine_updated = pyttsx.init()  # intializing the engine
        Engine_voices = Engine_updated.getProperty('voices')  # returns the list of the voices
        if gender is not "":
            if str(gender).lower() == "male":
                Engine_updated.setProperty('voice', Engine_voices[0].id)
                pass
            elif str(gender).lower() == "female":  # changing with respect to female
                choose_voice_id = random.randint(1,
                                                 2)  # finding the random number , as we want the females to be random
                print("Voice id changing to : ", choose_voice_id)
                Engine_updated.setProperty('voice', Engine_voices[
                    choose_voice_id].id)  # setting the voice property of the Engine
        return Engine_updated
    except Exception as E:
        print("An Error Occurred while changing by gender", E)  # printing the exception


def change_byname(name=""):
    Engine_updated = pyttsx.init()  # intializing the engine
    Engine_voices = Engine_updated.getProperty('voices')  # returns the list of the voices
    if name is not "":
        if str(name).lower() == "david":  # David Voice
            try:
                Engine_updated.setProperty('voice',
                                           Engine_voices[0].id)  # sets the voice to david, as it is on the index 0
            except Exception as E:
                print("Unable to change the voice to david, David not found :", E)
        elif str(name).lower() == "hazel":  # hazel Voice
            try:
                Engine_updated.setProperty('voice', Engine_voices[
                    1].id)  # sets the voice to hazel since the hazel is on the index 1
            except Exception as E:
                print("Unable to change the voice to hazel, hazel is not found :", E)  # Debugging purpose
        elif str(name).lower() == "zira":  # Zira Voice
            try:
                Engine_updated.setProperty('voice',
                                           Engine_voices[2].id)  # sets the voice to the Zira, its on the index 2
            except Exception as E:
                print("Unable to change the voice to zira, since zira is not found :", E)  # Debugging purpose
        return Engine_updated  # returns the engine (--> pyttsx engine <-- keep in mind )
        # TODO: Make more engines optimized add deconstructor for destroying the previous engine
    else:
        return Engine_updated  # default values are returned  since there is no change required


def volume_update(status_value="high"):
    Engine_updated = pyttsx.init()  # intializing the engine
    Engine_volume = Engine_updated.getProperty('volume')
    if status_value != "high" and (0.0 < Engine_volume <= 1.0):
        # The above condition speciffies that the status is not high and the current engine volume is in between .0 & .1
        if status_value == 'medium':

            Engine_updated.setProperty('volume', 0.75)
        elif status_value == 'low':
            Engine_updated.setProperty('volume', Engine_volume - 0.70)
        else:
            Engine_updated.setProperty('volume', 1.0)
        return Engine_updated  # returning the updated engine

    else:
        Engine_updated.setProperty('volume', 1.0)
        print("Default volume set of the engine.")
        return Engine_updated  # Returns the default engine



'''-- Below is the checking of the Female gender , only for debugging purposes'''
# engines = None
# engines = change_gender(gender="female")
# engines.say("The quick brown fox jumped over the lazy dog")
# engines.runAndWait()
'''-- Below is the Checking of the voices by the name--'''
# engine = None
# engines = change_byname('hazel')
# engines.say("The quick brown fox jumped over the lazy dog")
# engines.runAndWait()
'''Below is the checking of the change of the volumes , rather increasing or decreasing the volume of the assistant'''
# engine = volume_update("high")
# engine.say("Hi my name is muhammad Shafay Amjad and i live in pakistan lahore, recently my teachers are against me")
# engine.runAndWait()
