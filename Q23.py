num=int(input("Enter 1 to convert from C to F and 2 for vice-versa "))
if num==1:
    a=int(input("Enter temprature in C: "))
    print("Temp in F:", (a*9/5)+32)
elif num==2:
    a=int(input("Enter temprature in F: "))
    print("Temp in C:", (a-32)*5/9)
else:
    print("Invalid number entered.")