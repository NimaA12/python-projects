
import json
from colorama import *
import random
from  utils.functions import hasElemant


def printColored (kalame,guess):
    if len(kalame) != len(guess):
        raise RuntimeError("[error]: b and kalame don't have same length")
    # print(Style.DIM)
    for i in (range(len(guess))) :
        j = (len(guess)) - i -1
        if (guess[j]) == kalame[j] :
            print(Back.GREEN,(guess[j]),Back.GREEN,end="")
        elif hasElemant(kalame,guess[j]) :
            print(Back.YELLOW,(guess[j]),Back.GREEN,end="")
        else :
            print(Back.RED,(guess[j]),Back.RED,end="" )
        print(Back.BLACK,"",end="")



with open('data/5_char_words.json',encoding="utf8") as f:
    words = json.load(f)

init()
#a = print(b.split())

kalame = random.choice(words)

print("taghalob",kalame)


for i in range(4):
    b = input(" yek harf hads beyanid  : ")
    printColored (kalame=kalame,guess=b)
    print()
    print()


deinit()
