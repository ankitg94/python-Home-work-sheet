#answer-1

n=int(input("How many data ?:"))
d3={}
for e in range(n):
   keys=input("Enter the no:")
   data=input("Enter the student name:")
   d3[keys]=data
print(d3)

#answer-2
a={1:"apple",2:"banana",3:"mango",4:"strawberry"}
print(list(a.keys()))
print(list(a.items()))

#answer-3
print(list(a.values()))

#answer-4
b={10:"apple",12:"banana",13:"mango",14:"strawberry"}
updatedict={1:"dragon",12:"pineapple"}
b.update(updatedict)
print(b)

#answer-5
print(list(b.keys()))

#answer-8
k=[1,2,3,4]
v=["ank","que","wer","zyan"]
print(str(k))
print(str(v))
dict={}
for key in k:
    for value in v:
        dict[key]=value
print(str(dict))

#answer-9     
z={1:"a",2:"b",3:"c",4:"d",5:"e"}
u={6:"f",7:"g",8:"h"}
z.update(u)
print(z)

#answer-10
k={'c':92,'java':66,'python':85}
print(min(k))