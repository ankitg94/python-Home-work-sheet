"""
#answer-1
l=[3,4,5,2,7,8]
it=iter(l)
while True:
    print(next(it),end=' ')
    
#answer-2
def oddgenerator(n):
    x=1
    while n:
        yield x
        x+=2
        n-=1    
for e in oddgenerator(10):
    print(e,end=' ')    

#answer-3:
def evengenerator(a):
   x=2
   while a:
     yield x
     x+=2
     a-=1
for e in evengenerator(10) :
    print(e,end=' ')   

#answer-4
def sum_nat(b):
    x=1
    while b:
        yield x*x
        x+=1
        b-=1   
for e in sum_nat(10):
    print(e,end=' ')         

#answer-5
def fib(n):
    a,b=0,1
    while n:
        yield a
        a,b=b,a+b
        n-=1
for e in fib(int(input("Enter no:"))):
    print(e,end=' ')           
"""
    