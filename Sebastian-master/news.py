#! python 3

import requests,json
import pprint
from termcolor import colored
from unidecode import unidecode
import colorama

def news_api(source):
    colorama.init()
    newsSource=source
    url = "https://newsapi.org/v1/articles?apiKey=<use your key>&source=" + newsSource
    response = requests.get(url)
    data = response.json()
    #print(data)
    #pprint.pprint(data)

    if data["status"] != "error":
        articles=data["articles"]
        for article in articles:
            print(colored("#"+article['title'],'green',attrs=['bold'])+colored("    by "+data['source'],'magenta'))
            print(colored("Description:\n"+article['description'],'yellow'))
            print(colored("URL:"+article['url'],'blue',attrs=['bold']))
            if article['publishedAt'] is not None:
                print(colored("Published at : "+article['publishedAt']+"\n",'red'))


    else:
        print(colored("Invalid news resource",'red'))
        
















if __name__=='__main__':
    news_api("bbc-news")
