lst=[]
print("Enter the lines:")
while True:
    string=input()
    if len(string)==0:
        break
    else:
        lst.append(string)
for i in lst:
    print(i)
    
