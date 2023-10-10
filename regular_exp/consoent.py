from re import*

text="aAIEjhjk@@hc".casefold()

matcher=finditer("[^aeiou]",text)
for m in matcher:
   if m.group().isalpha():
    print(f"group={m.group()}")
   
