f_read=open("C:\\Users\\NJ\\Desktop\\python_work\\input_output\\data.txt")
odd_f=open("C:\\Users\\NJ\\Desktop\\python_work\\input_output\\odd.txt","w")
even_f=open("C:\\Users\\NJ\\Desktop\\python_work\\input_output\\even.txt","w")

for line in f_read:
    num=int(line.rstrip("\n"))
    if num%2==0:
       even_f.write(str(num)+"\n")
    else:
        odd_f.write(str(num)+"\n") 


