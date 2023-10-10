text=input("enter the word :").casefold()
v_count=0
c_count=0
for ch in text:
  if ch in  ["a","e","i","o","u"]:
    v_count+=1
  elif ch!=" ":
    c_count+=1
print(f"the vowel count is:",v_count)
print(f"the consonant count is:{c_count}")
    