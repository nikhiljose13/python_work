alluser=["mohanlal","fahad","unny","mamooty","nivin","dq"]

nivin_friend=["mohanlal","fahad","unny"]
fahad_friend=["mohanlal","unny","mamooty"]
lst=nivin_friend+fahad_friend
lst.sort()
dup_lst=[]
for i in range(0,len(lst)-1):
        currrent=lst[i]
        next=lst[i+1]
        if currrent==next:
               if currrent not in dup_lst:
                       dup_lst.append(currrent)
print("mutual friend are :",dup_lst)
    