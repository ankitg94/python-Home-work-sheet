
#answer-1
a=6
b=2
c=0
try:
    c=a/b
except ArithmeticError:   
    print("sahi no likho:") 

print(c)    

#answer-2
a=3
b=6 
c=0
try:
    b=int(input("Enter the letter:"))
    c=a/b
except ValueError:
    print("dont used this letter")  

print(c)          

#answer-3
c=9
d=0
try:
    b=int(input("Enter the no:"))
    d=c/b
except ArithmeticError:
    print(d)    

#answer-4
x="ankit"
z=" "
try:
    y=input("Enter the no: ")
    z=x+y    
except ValueError:
    print("error handle",z)    

#answer-5
a=3
c=0
try:
    b=int(input("Enter the no : "))
    c=a/b     
except ValueError:
    print("plese don't enter vlaue ...gadhe..")
except ArithmeticError:
    print("plese don't enter the zero no...gadhe.. ") 
except Exception:
    print("Enter the correct value...gadhe...")
print(c)           

#answer-6
c=0
try:
    a=int(input("Enter the 1st no : "))
    b=int(input("Enter the 2nd no : "))
    c=(input("Enter the sign (+ , - , * , / = "))
    if c == "+" :
        print(a+b)
    elif c == "-" :
        print(a-b)
    elif c =="*":
        print(a*b)
    elif c == "/":
        print(a//b)
except ArithmeticError:
    print("please Enter the non-zero") 
except ValueError:
    print("plese Enter the value-zero")           
except Exception:
    print("value Enter")
finally:    
    print(c) 

#answer-7
c=0
try:
    print("File opened")
    a=int(input("Enter the no :")) 
    b=int(input("Enter the no :")) 
    c=a/b
except ArithmeticError:
    print("this is arithemetic error")    
except Exception:
   print("this is exceptional error") 
finally:
    print("file closed ") 
print(c)      

#answer-8
a=6
c=0
try:
    b=int(input("Enter the no:"))
    c=a/b
except Exception:
    print("you have pass without error ::")

else:
    print(c)

#answer-9
a=3
c=0
try:
    b=int(input("Enter the no :"))
    c=a/b
except ValueError:
    print("don't write value....")

print(c)        

#answer-10
a=4
c=0
try:
    b=int(input("Enter the no :"))
    c=a/b
except ArithmeticError:
    try:
        print("ashu ")
    except Exception:
        print("utha")   
print(c)         
