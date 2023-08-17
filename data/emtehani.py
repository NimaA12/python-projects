from colorama import *

import json
with open('data/words.json',encoding="utf8") as f:
    words = json.load(f)

def hasElement(,char) : 


init()
b = input(" yek harf hads beyanid  : ")
#a = print(b.split())

kalame = "آبان"



print(Style.DIM)
for i in (range(len(b))) :
    j = (len(b)) - i -1
    if (b[j]) == kalame[j] :
        print(Back.GREEN,(b[j]),Back.GREEN,end="")
    elif b[j] in kalame :
        print(Back.YELLOW,(b[j]),Back.GREEN,end="")
    else :
        print(Back.RED,(b[j]),Back.RED,end="" )
    print(Back.BLACK,"",end="")
   

deinit()
