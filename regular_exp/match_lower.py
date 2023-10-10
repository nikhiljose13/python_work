from re import*

text="aAIEjhjkhc".casefold()
# matcher=finditer("[a-z,0-9]",text)
# matcher=finditer("[^0-9]",text)
matcher=finditer("[aeiou]",text)
count=0
for m in matcher:
    # print(f"location={m.start()}")
    print(f"group={m.group()}")
    count+=1
print(f"count={count}")