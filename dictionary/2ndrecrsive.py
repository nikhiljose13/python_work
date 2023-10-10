text="ABCDBA"
wc={}
lst=[]
for ch in text:
    if ch in wc:
        lst.append(ch)        
    else:
        wc[ch]=1
print(lst[1])