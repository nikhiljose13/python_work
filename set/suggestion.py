all_user=["nikhil","femi","diya","amal","delma"]
all_user.pop(0)
nikhil=["femi","diya","delma"]
# all=set(all_user)
# nik=set(nikhil)
# suggestion=all.difference(nik)
# print(suggestion)
suggestion=set(all_user).difference(set(nikhil))
print(suggestion)