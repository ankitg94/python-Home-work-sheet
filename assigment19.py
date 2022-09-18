#answer-1

def f1():
    print('"mysirg"')

f1()    

#answer-2
def f2(a,b):
    return a,b
print(f2(2,3))    

#answer-3
def f3():
    a=int(input("Enter the no:"))
    b=int(input("Enter the no:"))
    
    return a,b
print(f3())    

#answer-4
def f4(a,b):
    return a,b
print(f4(b=2,a=5))    

#answer-5
def f5(*t):
    return t
print(f5(2,4,6,5))    

#answer-6
def f6():
    a=int(input("Enter the no:"))
    b=int(input("Enter the no:"))
    c=int(input("Enter the no:"))
    d=int(input("Enter the no:"))
    if a>b and a>c and a>d  :
         print("this is A",a)
    elif b>a and b>c and a>d :
         print("this is B",b)
    elif c>a and c>b and c>d:
         print("this is C",c)
    else:
         print("this is D",d)
f6()        

#answer-7
def  f7(*t):
    f=sum(t)
    return f
print(f7(2,6,7,8,9))

#answer-8
def f8(t,y):
    g=t*y
    return g
print(f8(3,4))
#answer-9
def f9():
    x=int(input("Enter the no:"))
    for i in range(1,100):
        if i==x:
            print("avail")
            break
    else:
        print("abs")

f9()
#answer-10
def f10():
    j=int(input("enter the no:"))
    if j%2==0:
        print(j,"is even")
    else:
        print(j,"is odd")
f10()            










