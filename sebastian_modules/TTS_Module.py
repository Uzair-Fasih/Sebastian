# /usr/bin/env Python3
import pyttsx3

class tts_engine(object):
    def __init__(self):
        # Required Global Variables

        self.eng = pyttsx3.init()
        self.voices = self.eng.getProperty('voices')
        self.eng.setProperty('voice', self.voices[1].id)
        print('TTS Called')

    def say(self, tts_output=None):
        if tts_output==None:
            self.eng.say('Hey Hello Listen')
            self.eng.runAndWait()
        else:
            self.eng.say(tts_output)
            self.eng.runAndWait()

