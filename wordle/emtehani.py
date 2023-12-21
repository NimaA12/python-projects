
import json
from colorama import *
import random
from  utils.functions import hasElemant
import sys

print()
print()



print(Back.GREEN, "hello welcome to wordle ")
print(Back.BLACK,"",end="")

print()
print()
print()


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
    b = input("\033[1;36;40m kalame ra hads bezanid : \033[0m")
    if b == kalame :
        print(Back.GREEN,"barande shodi........")
        print(Back.BLACK,"",end="")
        sys.exit()
    print(Back.BLACK,"",end="")
    if len(b) != 5 :
        b = input("faghat kaleme hay 5 harfi ghabool mishavad lotfan dobare talash konid ... : ")
   # if b in words :
      #  print("dar list hast")
    printColored (kalame=kalame,guess=b)
    print()
    print()


if b != kalame :
    print(Back.RED," bakhti ")
    print()
    print()
    print()

    print(Back.BLUE, "kalame : " ,kalame )    

print(Back.BLACK,"",end="")





deinit()
