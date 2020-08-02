#! python 3

import requests,json
import pprint
from termcolor import colored
from unidecode import unidecode
import colorama

class NewsModule(object):
    @staticmethod
    def news_api(voice, gui_object, string):
        colorama.init()
        newsSource="bbc-news"
        url = "https://newsapi.org/v1/articles?apiKey=b9034b9b68034690ba896d5a1330f029&source=" + newsSource
        response = requests.get(url)
        data = response.json()

        if data["status"] != "error":
            articles=data["articles"]
            if voice == 1:
                gui_object.tts_var.say('Showing top news headlines from today')
            gui_object.screen_updater('Sebastian:  ' +'Showing top news headlines from today')

            for article in articles:
                print(article['title'])
                gui_object.screen_updater('#'+article['title'])
                

        else:
            #print(colored("Invalid news resource",'red'))
            gui_object.screen_updater("Invalid news resource")
        

if __name__=='__main__':
    news_api("bbc-news")
