
import json

# with open('data/words.json',"r",encoding="utf8") as f:
#     words = json.load(f)


words = []

with open('data/words.txt',"r",encoding="utf8") as f:
    a=f.readline()
    for line in f:
         w, n = (line.split())
         if  int(n) >= 1000 and "\u200c" not in w:
             words.append(w)



for w in words:        
    print(w)



L5Words = []
L4Words = []

for w in words:
    if len (w) == 4 :
        L4Words.append( w )
    if len (w) == 5 :
        L5Words.append( w )


with open( 'data/5_char_words.json' , 'w' , encoding='utf8') as f:
    json.dump(L5Words,f,ensure_ascii=False,indent=4)

with open( 'data/4_char_words.json' , 'w' , encoding='utf8') as f:
    json.dump(L4Words,f,ensure_ascii=False,indent=4)






