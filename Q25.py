num1=int(input("Enter number1: "))
num2=int(input("Enter number2: "))
op=input("Enter a valid operator: ")
if op=='+':
    print("Sum is:", num1+num2)
elif op=='-':
    print("Difference is:", num1-num2)
elif op=='*':
    print("Product:", num1*num2)
elif op=='/':
    print("Quotient:", num1/num2)
else:
    print("Invalid operator.")
