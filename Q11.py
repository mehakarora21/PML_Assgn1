num=int(input("Enter the no. of terms required in fibonacci: "))
count=2
b=0
c=1
print(b,c, end=' ')
while count<num:
    d=b+c
    count+=1
    print(d, end=' ')
    b=c
    c=d

