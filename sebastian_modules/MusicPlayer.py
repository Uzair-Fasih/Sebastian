# /usr/bin/env Python3

import pygame
from tkinter.filedialog import askopenfilename
import os, random


class MusicPlayer(object):

    @staticmethod
    def play_music(voice, gui_object, string):
        speech = voice
        query = string
        if voice == 1:
            gui_object.tts_var.say('Which song should I play? ')
        gui_object.screen_updater('Sebastian:  ' + 'Which song should I play? ')
        filename = askopenfilename()
        x = filename.split('/')
        if voice == 1:
            gui_object.tts_var.say('Playing - ' + x[len(x)-1])
        gui_object.screen_updater('Sebastian:  ' +' Playing - ' + x[len(x)-1])
        gui_object.screen.update()
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

    def stop_music(voice, gui_object, string):
        try:
            pygame.quit()
        except:
            if voice == 1:
                gui_object.tts_var.say('Nothing is playing anymore')
        gui_object.screen_updater('Sebastian:  ' +'Nothing is playing anymore')

    def play_random_music(voice, gui_object, string):
        speech = voice
        query = string
        filename = random.choice(os.listdir("E:\\Uzair\\Music\\"))
        x = filename
        filename = "E:\\Uzair\\Music\\" + filename
        if voice == 1:
            gui_object.tts_var.say('Playing - ' + x)
        gui_object.screen_updater('Sebastian:  ' +' Playing - ' + x)
        gui_object.screen.update()
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        
