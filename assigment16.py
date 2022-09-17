#tuple-chapter

#answer-1
a=('java','python','sql','c')
print(type(a))
#answer-2
b=('ankit',)
print(type(b))
#answer-3
print(a[::-1])
#answer-4
d=int(input("Enter the no:"))
e=int(input("Enter the no:"))
(d,e)=(e,d)
print("d=",d,"E=",e)

#answer-5
f=(2,4,5,5.6)
result=f.count(f[0])== len(f)
if (result):
        print("ALL are equal")
else:
    print("not equal")      


#answer-6
t=(100,200,300,400)
print(t[0])
print(t[1])
print(t[2])
print(t[3])

#answer-7
x=(1,2,3,4,5,6)
x1=x[3:5]
print(x1)

#answer-9
u=("python",[10,20,30],(2,4,6))
print(u[1][1])
#answer-10
#tuple is immutable (not changable)
