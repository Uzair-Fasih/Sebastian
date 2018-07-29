import wolframalpha
import wikipedia

def wiki_wolfram():
    query=input("question:")

    try:

        #give the registered id from wolframalpha
        app_id = "3E6X9K-K5PTR98A9R"

        #create client
        client=wolframalpha.Client(app_id)

        #print res

        res =client.query(query)

        answer = next(res.results).text

        print(answer)

    except:
         print(wikipedia.summary(query,sentences=5))



if __name__== '__main__':
    while True:
        wiki_wolfram()
         
