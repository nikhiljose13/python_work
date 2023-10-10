from re import*
f=open("C:\\Users\\NJ\\Desktop\\python_work\\regular_exp\\number&mail.txt")

phone_rule="\d{10}"

mail_rule="[\w]+@gmail.com"

phone_number=open("C:\\Users\\NJ\\Desktop\\python_work\\regular_exp\\phone.txt","w")
e_mail=open("C:\\Users\\NJ\\Desktop\\python_work\\regular_exp\\email.txt","w")

for line in f:
    word=line.rstrip("\n").rsplit()
    for w in word:
      matcher=fullmatch(phone_rule,w)
      email_matcher=fullmatch(mail_rule,w)
      if matcher!=None:
         phone_number.write(str(w)+"\n")
      elif email_matcher!=None:
         e_mail.write(str(w)+"\n")

