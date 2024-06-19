string="tranquility disrupted"
strList=list(string)
uniqueList=[]
countList=[]
for i in strList:
    if i not in uniqueList:
        count=0
        uniqueList.append(i)
        for j in strList:
            if j==i:
                count+=1
        countList.append(count)

for i in range(len(uniqueList)):
    print(uniqueList[i], ":", countList[i])

