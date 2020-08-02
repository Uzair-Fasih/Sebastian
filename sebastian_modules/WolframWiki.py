# /usr/bin/env Python3

import webbrowser
import wolframalpha
import wikipedia


class WolframClass(object):

    @staticmethod
    def wiki_wolfram(voice, gui_object, string):
        speech = voice
        query = string
        try:
            # give the registered id from wolframalpha
            app_id = "3E6X9K-K5PTR98A9R"

            # create client
            client = wolframalpha.Client(app_id)

            # print res

            res = client.query(query)

            answer = next(res.results).text

            gui_object.screen_updater('Sebastian:  ' + answer)
            if speech == 1:
                gui_object.tts_var.say(answer)
        except:
            try:
                gui_object.screen_updater('Sebastian:  ' + wikipedia.summary(query, sentences=2) + '- From Wikipedia')
                gui_object.screen.update()
                
                if speech == 1:
                    gui_object.tts_var.say(wikipedia.summary(query, sentences=1))
            except:
                
                if speech == 1:
                    gui_object.tts_var.say("I am afraid I don't understand. You might wanna phrase that properly")
                gui_object.screen_updater('Sebastian:  ' + "I am afraid I don't understand. You might wanna phrase that properly")



