
import json

with open('data/words.json') as f:
    words = json.load(f)

# print(words)
# print(len(words))


for word in words:
    print(word)



with open( 'data/5_char_words.json' , 'w' , encoding='utf8') as f:
    json.dump(words[:10],f,ensure_ascii=False,indent=4)
