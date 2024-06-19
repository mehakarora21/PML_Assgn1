import csv
fileObj=open(r"C:\Users\hp\Desktop\PML Internship Projects\Demo.csv.txt",'r')
a=csv.reader(fileObj, delimiter=',')
for i in a:
    print(i)
