text="hi hai hi hai"
word=text.split(" ")
wc={}
for ch in word:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
print(wc)