str1="This, is: a string!"
str2=""
for i in str1:
    if i.isalnum() or i==' ':
        str2+=i
    else:
        continue
print(str2)
    
