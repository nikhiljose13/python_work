from re import*
text="bdhjsbchjcjhbckuihbuiahdczxujiosaaaodjcisjaa"
Pattern="a+"
matcher=finditer(Pattern,text)

for m in matcher:
    print(m.group(),m.start())