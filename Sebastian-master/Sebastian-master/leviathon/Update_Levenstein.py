
'Add words to Leviathon Levenstein\'s Dictionary \
&sep&                                               \
twitter&sep&notifications                               \
'
import json

def entry(string):

    entryList = string.split('&sep&')
    fi = open("Levenstein's_Dictionary", "r")
    existList = json.load(fi)
    fi.close()
    existList = existList + entryList
    f = open("Levenstein's_Dictionary","w")
    json.dump(existList, f)
    f.close()

if __name__ == '__main__':

    print("Manual Entry to Levenstein's Dictionary\n\n\n")
    print("Please refrain from entering words one by one \n\
          Rather use a word editor to spell check and ensure that your wording is correct \n\
          Copy and paste your code into the interpreter/terminal separating each word with the string\n\
          \'&sep&\' without the quotes."
          )
    entrystring = input("Please enter the words now.\n")
    entry(entrystring)