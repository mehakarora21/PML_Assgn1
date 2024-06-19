prefix=input("Enter prefix(press \\n if none to be checked) ")
print(prefix)
suffix=input("Enter suffix(press \\n if none to be checked) ")
string="This day is beautiful."
if prefix!='\\n':
    if prefix==string[0]:
        print("String starts with prefix.")
    else:
        print("String doesn't start with prefix.")
if suffix!='\\n':
    if suffix==string[len(string)-1]:
        print("String ends with suffix.")
    else:
        print("String doesn't end with suffix.")