def max_word(*args):
   len_word=max(args,key=lambda w:len(w))
   return len_word
print(max_word("hi","hello","hai"))


