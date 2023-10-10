lst=['mohanlal', 'fahad', 'unny', 'mohanlal', 'unny', 'mamooty']
lst.sort()
dup_lst=[]
for i in range(0,len(lst)-1):
        currrent=lst[i]
        next=lst[i+1]
        if currrent==next:
               if currrent not in dup_lst:
                       dup_lst.append(currrent)
print(dup_lst)
