from re import*

text="aAIEj7h8j9@k0hc".casefold()
# Pattern="\d"
# Pattern="\D"
# Pattern="\w"
Pattern="\W"
matcher=finditer(Pattern,text)

for m in matcher:
    
    print(f"group={m.group()}\npos={m.start()}")
    