
import json
from colorama import *

from  utils.functions import hasElemant


with open('data/words.json',encoding="utf8") as f:
    words = json.load(f)



init()
b = input(" yek harf hads beyanid  : ")
#a = print(b.split())

kalame = "آبان"


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
    

printColored ("hhsuhde","f")

deinit()
