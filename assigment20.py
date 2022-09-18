
#answer-1
#pending
#answer-2
def prime():
       a=int(input("Enter the no:"))
       if a<2 :
          print("Not prime")
       else:
          for i in range(2,a):
             if a%i==0:
                print("Not prime")
                break
          else:
            print("Prime")   
prime()
   
#answer-3
#pending
#def  even_no():
b=(int[1,2,3,4,5,6,7,8,9])
for i in range(b):
    if i%2==0:
      print(i)       

#answwr-4
n=int(input("Enter the no:"))
t=n
rev=0

while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
print(rev)       
if (t==rev):
    print("polindrome")
else:
    print("no polidrome")              

#answer-5
def f5():
    a=int(input("Enter the no:"))
    b=int(input("Enter the no:"))
    c=int(input("Enter the no:"))

    if a>b and a>c  :
         print("this is greater=A",a)
    elif b>a and b>c :
         print("this is greater =B",b)
    else :
         print("this is greater =C",c)
    
f5()         

#answer-6
def f6():
    for i in range(1,31):
        print(i*i)
f6()        

#answer-7
#nested function
def mainf():
    print("main function")
    def childf():
        print("child function")
    childf()
mainf()        

#answer-8
def f8():
    str="Ankit Gupta"
    lower=0
    upper=0
    for i in str:
        if (i.islower()):
            lower+=1
        else:
            upper +=1
    print(lower)
    print(upper)            
(f8())            

#answer-9
import string
def ispangram(str):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
    return True
string ="th quick brown fox jump over the lazy dog" 
if (ispangram(string)==True):
    print("yes")
else:
    print("no")               

#answer-10
def f10(s,x):
    if(sorted(s)==sorted(x)):
        print("yes:")
    else:
        print("no")
s="ankit"
x="tikna"            
f10(s,x)