"""
Leviathon for Sebastian.
It is the core of Sebastian's intent recognizing algorithm.
This module employs both Levenstein Edit Distance and Munkres Algorithm.
Needless to say uses their dictionaries.
Use the Update_xxx.py files for updating the dictionaries.
"""
import json


class leviathon(object):
    def __init__(self,voicestring):
        self.step1 = levenstein(voicestring)
        self.step2 = munkres(self.step1)

    def function(self):
        return self.step2


def levenstein(voice):
    fi = open("Leviathon\Levenstein's_Dictionary", "r")
    list2 = json.load(fi)
    fi.close()

    list1 = voice.split()
    decoded_list = []

    for word in list1:
        scores = []
        word1 = list(word)
        for dictionary_word in list2:
            word2 = list(dictionary_word)
            score = 0
            for a, b in zip(word1, word2):

                if a == b:
                    score = score + 2
                elif a == '':
                    score = score - 0
                elif b == '':
                    score = score + 0
                elif a != b:
                    score = score + 0
            scores.append(score)
        if max(scores) > len(word1):
            decoded_list.append(list2[scores.index(max(scores))])
    return decoded_list


def munkres(decoded):
    fi = open("Leviathon\Munkres's_Dictionary", "r")
    list2 = json.load(fi)
    fi.close()
    scores = []
    # list1 is obtained from Levenstein
    list1 = decoded
    increments = 0
    for lists in list2:
        score = 0

        for term1 in list1:
            for terms in lists:
                if term1 == terms:
                    score = score + 1
        if score >= 2:
            score = score + increments
            increments = increments + 1
        scores.append(score)
    functions = []
    for score in scores:
        if score >= 2:
            functions.append(list2[scores.index(score)])

    return functions

if __name__ == '__main__':
    levi = leviathon("Hey what are twitter notifications also facebook")
    print(levi.function())
