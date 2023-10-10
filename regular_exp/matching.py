from re import*

text="abababa5bababc"

# matcher=finditer("ab",text)

# count=0
# for m in matcher:
#     print(m.start())
#     print(m.group())
#     count+=1
# print(f"count={count}")
matcher=finditer("[0-9]",text)
for m in matcher:
    print(f"location={m.start()}")
    print(f"group={m.group()}")