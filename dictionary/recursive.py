text="ABCDB"
wc={}
for ch in text:
    if ch in wc:
        print(ch,"is first recursive")
        break
    else:
        wc[ch]=1