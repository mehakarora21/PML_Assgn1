num=20645
sum=0
multiplier=10
while True:
    quo=num//multiplier
    remain=num%multiplier
    bufferMultiplier=multiplier//10
    digit=remain//bufferMultiplier
    sum+=digit
    if quo==0:
        break
    else:
        multiplier*=10
print("Sum of digits in num: ", sum)
