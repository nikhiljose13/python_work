f=open("C:\\Users\\NJ\\Desktop\\python_work\\input_output\\test.txt","r")
lst=[line.rstrip("\n") for line in f]
print(lst)
long_word=max(lst,key=lambda w:len(w))
print(long_word)