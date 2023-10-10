text=" hello good  goodmorning"
words= text.split(" ")
srted_word= sorted(words, key= lambda w : len(w),reverse=True)
print(srted_word)