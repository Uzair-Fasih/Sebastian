# /usr/bin/env Python3

import EventDispatcher as ed
from sebastian_modules import TTS_Module as tts, STT_Module as stt
from AnimatedGif import *
import tkinter as gui


class SebastianInterface(object):
    def __init__(self):
        # Required Global Variables
        self.listener = stt.stt_engine()
        self.i = 0  # Used in screen_updater
        self.tts_var = tts.tts_engine()

        # Root properties
        self.root = gui.Tk()
        self.root.configure(background='#212121')
        self.root.resizable(False, False)
        self.root.title('Sebastian - Your Personal Assistant')
        self.root.geometry('390x520')

        # Label for opening Transition
        self.Animation = AnimatedGif(self.root, 'icons/loading_transition.gif', 0.001)
        self.Animation.pack()
        self.Animation.start()
        self.root.after(4000, self.test_function)

    def test_function(self):
        print('Loading animation Ended')  # --------------------------------------------------
        self.Animation.destroy()

    def initialize(self):

        # Logo Image Banner properties

        logo = gui.PhotoImage(file='icons/logo_img.png')
        self.sebastian_banner = gui.Canvas(self.root, width=390, height=30, background='#212121')
        self.sebastian_banner.pack()
        self.sebastian_banner.create_image(0, 0, image=logo, anchor=gui.NW)

        # Input - Output Display Screen
        self.screen = gui.Listbox(self.root, background='#212121', foreground='#ffffff', font=('Helvetica', 10)
                                  , height=25)
        self.screen.pack(expand=gui.TRUE, fill=gui.X)
        # Frame
        self.bottomFrame = gui.Frame(self.root)

        search_image = gui.PhotoImage(file='icons/search.png')
        self.search = gui.Label(self.bottomFrame, image=search_image, width=30)
        self.search.place(x=0, y=0, relwidth=1, relheight=1)
        self.search.pack(side=gui.LEFT)

        self.entryBox = gui.Entry(self.bottomFrame, width=25, font=('Helvetica', 15))
        self.entryBox.bind('<Return>', self.entry_updater)
        self.entryBox.pack(expand=gui.TRUE, side=gui.LEFT)

        x_image = gui.PhotoImage(file='icons/x_image.png')
        self.removeEntry = gui.Button(self.bottomFrame, image=x_image, width=30, command=self.entry_clearer)
        self.removeEntry.place(x=0, y=0, relwidth=1, relheight=1)
        self.removeEntry.pack(side=gui.LEFT)

        mic_image = gui.PhotoImage(file='icons/mic.png')
        self.speak = gui.Button(self.bottomFrame, image=mic_image, width=30, command=self.mic_updater)
        self.speak.place(x=0, y=0, relwidth=1, relheight=1)
        self.speak.pack(side=gui.RIGHT)
        self.bottomFrame.pack(fill=gui.X, side=gui.BOTTOM)
        gui.mainloop()

    def entry_updater(self, evmode = None):
        temporary_entry = self.entryBox.get()
        self.screen_updater('User: ' + temporary_entry)
        self.screen.update()
        self.process(temporary_entry)

    def screen_updater(self, input_string):
        self.screen.update()
        if self.i > 12 and len(input_string) > 250:
            self.i = 0
            self.screen.delete(0, last=50)
        if len(input_string) > 1000:
            self.i = self.i + 1
            self.screen.insert(self.i, 'Query too long to display')
        else:
            no_of_chars = 60
            no_of_lines = len(input_string) / no_of_chars
            st_1 = 0
            st_2 = no_of_chars
            line_count = 0
            while line_count < no_of_lines:
                self.i += 1
                self.screen.insert(self.i, ' ' + input_string[st_1:st_2])
                st_1 += no_of_chars
                st_2 += no_of_chars
                line_count += 1
        self.entry_clearer()

    def entry_clearer(self):
        self.entryBox.delete(0, 300)

    def mic_updater(self):
        slst = 'stop listening'
        self.screen_updater('Sebastian: Sebastian at your service. How can I help?')
        self.tts_var.say('Sebastian at your service. How can I help?')
        while True:
            self.screen_updater("........Speak Now")
            self.screen.update()
            self.listener.listen()
            decoded = self.listener.voiceBox
            self.screen_updater('User: ' + decoded + "\n")
            self.screen.update()
            if slst not in decoded:
                self.process(decoded, 1)
                self.tts_var.say("Anything Else?")
                self.screen_updater("Sebastian: Anything Else?")

            elif slst in decoded:
                self.tts_var.say("Alright then. Good bye.")
                self.screen_updater("Sebastian: Alright then. Good bye.")
                break

    @staticmethod
    def process(string, voice=0):
        ed.EventDispatch().executor(voice, boot, string)

boot = SebastianInterface()
boot.initialize()
