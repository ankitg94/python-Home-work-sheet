#answer-1
a=int(input("Enter the number : "))
if a>0:
    print("positive")
else:
    print("non-positive")    

#answer-2
b=int(input("Enter the number :"))
if b%5==0:
    print(b,"is divisble by 5 ")
else:
    print(b,"is not divisble by 5")        

#answer-3
c= int(input("Enter the number :"))
if c%2==0:
    print(c,":is an even number") 
else:
    print(c,":is a odd number")       

#answer-4
d=int(input("Enter the number :"))
e=int(input("Enter the number :"))
if d>e:
    print(d," : 1st no is greater")
elif d==e:
    print("Both are same") 
else:
    print(e," : 2nd no is greater")       

#answer-6
f=int(input("Enter the number :"))
if f>99 and f<1000:
    print(f,"Is the Three digit no") 
else:
    print(f,"Is not Three digit no")      

#answer-7
g= int(input("Enter the number :"))
if g>0:
    print(g," is a positive no")
elif g==0:
    print(g," is a zero no ")
else:
    print(g,"is negative no ")            

#answer-9
h=int(input("Enter the number "))
if h%4==0:
    print(h," is leap year")
else:
    print(h,"is not leap year")        

#answer-10
i=int(input("Enter the 1st no:"))
j=int(input("Enter the 2nd no:"))
k=int(input("Enter the 3rd no:"))
if i>j>k:
    print(i,"1st no is greater")
elif j>i>k:
    print(j,"2nd  no is greater")
elif i==j==k:
    print("All are same")     
else:
    print(k,"3rd no is greater")

#answer-11
m=eval(input("Enter the month no :"))
if (m==1):
    print(m,"month have 31 Days")
elif (m==3):
    print(m,"month have 31 Days")
elif (m==5):
    print(m,"month have 31 Days")
elif (m==7):
    print(m,"month have 31 Days") 
elif (m==8):
    print(m,"month have 31 Days")
elif (m==10):
    print(m,"month have 31 Days")
elif (m==12):
    print(m,"month have 31 Days")   
elif (m==2):
    print(m,"month have 28 Days")
elif (m==4):
    print(m,"month have 30 Days")
elif (m==6):
    print(m,"month have 30 Days")      
elif (m==9):
    print(m,"month have 30 Days")      
elif (m==11):
    print(m,"month have 30 Days")                        
else:
    print("Wrong input")          