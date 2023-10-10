all_user=["nikhil","femi","diya","amal","delma"]
nikhil=["femi","diya","delma"]
suggestion_lst=[]
for i in all_user:
    if i not in nikhil:
        suggestion_lst.append(i)
suggestion_lst.pop(suggestion_lst.index("nikhil"))
print(suggestion_lst)