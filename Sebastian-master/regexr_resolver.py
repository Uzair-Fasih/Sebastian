'This is for testing purposes. Please ignore.\
Modeule name: regexr_resolver'

import re
import no_internet_modules as nim

def sebastian(string_cont):

    i=0
    if string_cont == None:
        string = input("What can I do for you?\n").lower()
    else:
        string = string_cont
    nim_m1 = re.search('day|DAY|Day',string)
    nim_m2 = re.search('Month|month|MONTH',string)
    nim_m3 = re.search('year|Year|Year',string)
    nim_m4 = re.search('date|Date|DATE',string)
    nim_m5 = re.search('time|Time|TIME',string)

    
    if nim_m1 is not None:
        nim.day()
        i+=1
    if nim_m2 is not None:
        nim.month()
        i+=1
    if nim_m3 is not None:
        nim.year()
        i+=1
    if nim_m4 is not None:
        nim.date()
        i+=1
    if nim_m5 is not None:
        nim.time()
        i+=1

    if i==0:
        print('I am afraid I don\'t understand')

if __name__ == '__main__':

    
    '''
    print("\n\
    This module was accessed directly.\n\
    If you are lost, it's best if you leave.\n\
    Executing functions and classes intended for testing purposes.\n")
    print('\n\n\n\n')
    test.check()
    
    '''
    sebastian(None)
    
    while(True):
        string = input('Anything else?\n').lower()
        sebs = re.search('No|no|Nothing|Thanks|Thank you|Goodbye|nothing|thanks|goodbye|nope|Nope|Nah|nah',string)
        if sebs is not None:
            print('Very well')
            break
        else:
            sebastian(string)
            
   
    
