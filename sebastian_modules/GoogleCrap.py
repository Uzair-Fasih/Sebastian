# /usr/bin/env Python3

import webbrowser
from autocorrect import spell

class GoogleClass(object):

    @staticmethod
    def google_search(voice, gui_object, string):
        speech = voice
        temp = string.split()
        i = 0
        str1 = ''
        if 'for' in temp:
            i = temp.index('for')
        elif 'fro' in temp:
            i = temp.index('fro')
        elif 'rfo' in temp:
            i = temp.index('rfo')
        elif 'search' in temp:
            i = temp.index('search')
        for words in temp[i + 1:]:
            str1 = str1 + ' ' + words

        if speech == 1:
            try:
                gui_object.screen_updater('Sebastian: I am looking for:  ' + str1)
                gui_object.tts_var.say('I am looking for:  ')
                gui_object.tts_var.say(str1)
                url = 'http://google.com/search?q='+str1
                webbrowser.open(url)

            except:
                gui_object.tts_var.say("I'm sorry, I couldn't reach google")
                gui_object.screen_updater('Sebastian: I\'m sorry, I couldn\'t reach google')

        else:
            gui_object.screen_updater("Sebastian: Searching for - " + str1)
            url = 'http://google.com/search?q=' + str1
            webbrowser.open(url)
