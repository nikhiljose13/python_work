year_write=open("C:\\Users\\NJ\\Desktop\\python_work\\input_output\\year.txt")
# [year_write.write(str(y)+"\n")for y in range(1800,2024)]
leap=open("C:\\Users\\NJ\\Desktop\\python_work\\input_output\\leap.txt","w")
not_leap=open("C:\\Users\\NJ\\Desktop\\python_work\\input_output\\not_leap.txt","w")
for y in year_write:
    year=int(y.rstrip("\n"))
    if(year%400==0)and(year%100==0):
        leap.write(str(year)+"\n")
    elif(year%4==0)and(year%100!=0):
        leap.write(str(year)+"\n") 
    else:
        not_leap.write(str(year)+"\n") 
         

    
