text=str(input(" enter a text:")).casefold()
word=(text).split(" ")
vowel="a","i","o","u" 
for w in word:
    if w.startswith(vowel):
        print(w)
