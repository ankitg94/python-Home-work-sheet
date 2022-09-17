
#answer-1
l=["java","python","SQL","c"]
print(l)
#answer-2
print(type(l))
#answer-3
l1=["java","c","python"]
print(l1[-1])

#answer-4
l2=["java","SQl","c","reactnative","javascript","python"]
for i in range (len(l2)):
    if l2[i]=='SQl':
        l2[i]="No SQl"
    if l2[i]=="reactnative":
        l2[i]="Flutter"    
print(l2)
#answer-5
l3=["java","SQl","c","Reactnative"]
l3.append("python")
print(l3)

#answer-6
a=["java","python","Sql"]
b=["c","cpp","NoSql"]
a.extend(b)
print(a)

#answer-7
c=["java","SQl","C","Reactnative","javascript","python"]
print(c[0:6])

#answer-8
d=["jva","sQl","c","reactjs","javascript","python"]
d.sort()
print(d)

#answer-9
g=input("Enter your city name:")
g2=input("Enter your city name:")
g3=input("Enter your city name:")
h=[g,g2,g3]
print(h)