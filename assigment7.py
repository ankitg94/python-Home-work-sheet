
#answer-1
a=int(input("Enter the month no :"))
match a:
   case 1:
      print(a,"have 31 days")
   case 2:
      print(a,"have 28 days")  
   case 3:
       print(a,"have 31 days")
   case 4 :
       print(a,"have 30 days")
   case 5:
       print(a,"have 31 days") 
   case 6:
       print(a,"have 30 days")
   case 7:
       print(a,"have 31 days")
   case 8:
       print(a,"have 31 days")
   case 9:
       print(a,"have 30 days") 
   case 10:
       print(a,"have 31 days") 
   case 11:
       print(a,"have 30 days")
   case 12:
       print(a,"have 31 days")
 #  case__:
  #     print("default")
 
#answer-2 
b=int(input("Enter the 1st no:"))
c=int(input("Enter the 2nd no:"))
d=(input("Enter the operation code:,add,sub,mul,div: = "))
if d=="add":
    print("Sum of two no is: ",b+c)
elif d=="sub":
    print("Sub of two no is:",b-c) 
elif d=="mul":
    print("Mul of two no is :",b*c)
elif d=="div":
    print("Div of two no is :",b/c)
else:
    print("wrong input")    

#answer-3
e=int(input("Enter the side of 1st triangle :"))
f=int(input("Enter the side of 2nd triangle :"))
g=int(input("Enter the side of 3rd triangle :"))
if f!=0 and g!=0 and e!=0 and  e!=f and f!=g :
    print("Triangle is isoscless") 
elif f!=0 and g!=0 and e!=0 and e==f and f==g  :
    print("Equilateral Triangle")
elif  f!=0 and g!=0 and e!=0 and e==f or f==g :
    print("right angle triangle") 
else:
    print("Exit")       

#answer-4
h=int(input("Enter the  Age number :"))
if h<=10:
    print("Kids")
elif h<=20:
    print("Teen")
elif h<=40: 
    print("Young")
elif h<=60:
    print("Experince") 
elif h<=100:
    print("Senior citizen")  
else :
     print("Wrong input")                

#answer-5
i=int(input("Enter the number : "))
if i>0 and  i%2==0:
    print("Saurabh Shukla")
elif i>0 and i%2!=0:
    print("aditya chaudry")    
elif i<=0 and i%2!=0:
    print("prateek jain")   
else:
    print("wrong input")    

#answer-9
k=int(input("Enter the year :"))
if  k<100 and k%4==0:
    print("Non century leap year")
elif k>100 and k%4==0:
    print("Century leap year")
elif k<100  and k%4!=0:
    print("Not Century no leap year") 
elif k>100 and k%4!=0:              
    print("Century non leap year")

#answer-10
l =input("Enter the colour of the day:")
match l:
    case "yellow":
         print("I like yellow colour = monday")
    case "blue":
         print("I like Blue colour = Tuesday")
    case "orange":
         print("I like orange colour = Wednesday")
    case "white":
         print("I like white colour =Thursday")
    case "black":
         print("I like Black colour = Friday")
    case "red":
         print("I like red colour = saturday")
    case "rest colour ":
          print("I like ",restcolour,"sunday")                         
