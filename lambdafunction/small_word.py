text="hi hai hi hai goodmorning"
word=text.split(" ")
small_word=min(word,key=lambda w:len(w))
print(small_word)

