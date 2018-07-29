import speech_recognition as sr
import gtts
import pyttsx3

def listen():
    eng=pyttsx3.init()
    voices = eng.getProperty('voices')
    eng.setProperty('voice', voices[1].id)
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('whatsup, say something')
        a=r.listen(source)
        
    try:
        r = r.recognize_google(a)
        print (r)
        eng.say(r)
        eng.runAndWait()
        return r;
    except sr.UnknownValueError:
        print ('could not understand audio')
    except sr.RequestError as e:
        print ('recog error',format(e))
    return ""

if __name__ == '__main__':

    while True:    
     print("say what u like to say")
     listen()
