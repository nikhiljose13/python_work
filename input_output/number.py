f=open("C:\\Users\\NJ\\Desktop\\python_work\\input_output\\number.txt")
number=[line.rstrip("\n") for line in f  ]
kl=[n for n in number if n.startswith("kl")]
# print(number)
print(kl)