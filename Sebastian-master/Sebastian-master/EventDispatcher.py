# /usr/bin/env Python3

import sebastian_modules as sm
from leviathon import Leviathon


class EventDispatch(object):

    @staticmethod
    def executor(voice, gui_object, string):

        fun_list = Leviathon.leviathon(string).function()
        count = 1
        print(fun_list)
        gui_object.screen_updater('Working on it....')
        gui_object.screen.update()
        if ["google", "search"] in fun_list:
            sm.GoogleCrap.GoogleClass.google_search(voice, gui_object, string)
            count = 0

        if ["google", "image"] in fun_list:
            # self.google_search_image()
            count = 0
        elif ["image", "search"] in fun_list:
            # self.google_search_image()
            count = 0
        if ["news","latest"] in fun_list:
            sm.NewsModule.NewsModule.news_api(voice,gui_object,string)
            count=0

        if count == 1:
            sm.WolframWiki.WolframClass.wiki_wolfram(voice, gui_object, string)
