
#answer-1
a=int(input("Enter the no : "))
rev=0
while a>0:
    rev=(rev*10)+a%10
    a=a//10
print("Reverse of no:",rev)    

#answer-2
b=int(input("Enter the no : "))
if b<2:
    print("not prime")
else:
    for i in range(2,b):
        if b%i==0:
            print("Not prime")
            break
    else:
        print("prime")
#answer-3
for n in range(2,101):
    if n>1:
        for i in range(2,n):
            if(n%i)==0:
                break
        else:
            print(n)        

#answer-4
e=int(input("Enter the start no:"))
f= int(input("Enter the end no:"))
for n in range(e,f+1):
        if n>1:
          for i in range(2,n):
             if(n%i)==0:
                break
          else:
            print(n)        
            
#answer-5
def nextprime(n):
  while True:  
    n+=1
    for i in range(2,n):
        if(n%2==0):
            break
    else:
        return n
print(nextprime())
             
#answer-6
h= int(input("Enter the end no:"))
for n in range(2,h+1):
        if n>1:
          for i in range(2,n):
             if(n%i)==0:
                break
          else:
            print(n)
                    
#answer-7
#pending
import math
n1 =int(input("Enter no :"))
n2 =int(input("Enter no:"))
res=math.gcd(n1,n2)
    if res==1:
        print("co-prime")
    else:
        print("not co prime")  
        
#answer-8
k=int(input("Enter the number :"))
x=0
y=1
z=0
while(z<=k):
    print(z)
    x=y
    y=z
    z=x+y        

#answer -9
x=int(input("Enter the no:"))
y=int(input("Enter the no :"))
maxnum = max(x,y)
while(True):
    if (maxnum%x==0 and maxnum%y==0):
        break
    maxnum = maxnum+1
print(f"The lcm of {x} and {y} is {maxnum}")            

#answer-10
x1=int(input("Enter the 1st no :"))
y1=int(input("Enter the 2nd no :"))
if x1>y1:
    mx=x1
else:
    mx=y1    
for i in range(1,mx+1):
    if x1%i==0 and y1%i==0:
        hcf =i
print("Hcf of two no: ",hcf)        
