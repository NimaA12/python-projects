
import json

kalame = (input("kalame ra hads bezanid"))

with open('data/words.json',encoding="utf8") as f:
    words = json.load(f)

L5Words = []
L4Words = []

for w in words:
    if len (w) == 4 :
        L4Words.append( w )
    if len (w) == 5 :
        L5Words.append( w )

#print (L5Words)

if kalame in words :
    print ("dorst")

