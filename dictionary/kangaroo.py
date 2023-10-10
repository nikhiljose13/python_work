sorceword="decreased"
targetword="dress"
wc={}

for ch in sorceword:

    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
# print(wc)

for ch in targetword:
    if ch in wc and wc.get(ch)>0:
        # curv=wc[ch]
        wc[ch]-=1
        
    else:
        is_kangaru=False
        break
print(is_kangaru)

