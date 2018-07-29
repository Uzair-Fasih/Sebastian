
'Add functions to Leviathon Munkres\'s Dictionary'
import json

def entry(string):

    entryList = string.split('&sep&')
    fi = open("Munkres's_Dictionary", "r")
    existList = json.load(fi)
    fi.close()
    print(existList)
    print(entryList)
    existList.append(entryList);
    print(existList)
    f = open("Munkres's_Dictionary","w")

    json.dump(existList,f)
    f.close()

if __name__ == '__main__':

    print("Manual Entry to Munkres\'s Dictionary\n\n\n")
    print("Please refrain from entering words one by one \n\
          Rather use a word editor to spell check and ensure that your wording is correct \n\
          Copy and paste your code into the interpreter/terminal separating each word with the string\n\
          \'&sep&\' without the quotes."
          )
    entrystring = input("Please enter the words of the functions now.\n")
    entry(entrystring)