#answer-1
"""
a=int(input("Enter the no :"))
count =0
while (a>0):
    count=count+a
     a=a-1
print("sum is",count)
#another method
b=int(input("Enter the no:"))
s=0
for  i in range (1,b+1):
   s+=i
print("sum is ",s)    

#answer-2
c=int(input("Enter the no :"))
s=0
for i in range(1,c+1):
   s+=i*i
print("sum of square is :",s)   

#answer-3
d=int(input("Enter the no:"))
s=0
for i in range(1,d+1):
   s+=i*i*i
print("sum of cube no :",s)

#answer-4
e=int(input("Enter the no :"))
s=0
for i in range(1,e+1,2):
   s+=i
print("sum of odd no :",s)

#answer-5
f=int(input("Enter the no :"))
s=0
for i in range (0,f+1,2):
   s+=i
print("Sum of Even no:",s)      
#answer-6
g=int(input("Enter the no :"))
s=1
for i in range(1,g+1):
   s*=i
print("factorial of",g,"is :",s)

#answer-7
h=int(input("Enter the given no :"))
s=0
while h>0:
   s=s+1
   h=h//10
print(s)   

#answer-8
j=int(input("Enter the no:"))
s=0
while j>0:
   s=s+(j%10)
   j=j//10
print(s)   
"""
#answer-9
#pending (binary conversion)
bnum=int(input("enter the no :"))
dnum = 0
i=1
while bnum !=0:
   rem = bnum%10
   dnum = dnum +(rem*i)
   i = i*2
   bnum = int(bnum/10)
print(dnum)   