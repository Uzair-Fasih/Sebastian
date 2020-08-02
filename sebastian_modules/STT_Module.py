# /usr/bin/env Python3

import speech_recognition as sr
import winsound


class stt_engine(object):
    def __init__(self):
        # Required Global Variables
        self.voiceBox = ''
        print('STT Called')

    def listen(self):
            # Records Audio
            r = sr.Recognizer()
            with sr.Microphone() as source:
                winsound.PlaySound('audio/BeepStart.wav', winsound.SND_FILENAME)
                audio = r.listen(source, timeout=20)
                winsound.PlaySound('audio/BeepEnd.wav', winsound.SND_FILENAME)

            try:
                decoded = r.recognize_google(audio)
                self.voiceBox = decoded
    
            except sr.UnknownValueError:
                print("Listening to the magic words: 'search for' or 'stop listening'")
            # Speech Recognition using Google Speech API
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio" + "\n")

            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e) + "\n")

