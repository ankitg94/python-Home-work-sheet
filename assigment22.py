#Answer-1
def sum_n(a):
    if a==1:
        return 1
    return a+sum_n(a-1)
a=int(input("Enter the no:"))
print(sum_n(a))

#answer-2,3
#pending
def odd(s,l):
    s==0
    for i in range(1,l+1,+2):
        s+=i
l=int(input("Enter the no:"))
print(odd(l,s))
#print(count)              

#answer-4
def sum_square(e):
    if e==1:
        return 1
    return e*e+sum_square(e-1)
e=int(input("Enter the no:"))    
print(sum_square(e))        

#answer-5
def sum_cube(b):
    if b==1:
        return 1
    return b*b*b+sum_cube(b-1)
b=int(input("Enter the no:"))
print(sum_cube(b))

#answer-6
def factorial(c):
    if c==1:
        return 1
    return c*factorial(c-1) 
c=int(input("Enter the no:"))
print(factorial(c))       

#answer-7
def sum_digit(r):
    return 0 if r==0 else int(r%10)+sum_digit(int(r//10))
r=int(input("Enter the no:"))
print(sum_digit(r))    

#answer-10
def fabnocci(j):
    if j<=1:
        return j
    else:
        return (fabnocci(j-1) + fabnocci(j-2))
j=int(input("Enter the no:"))
print(fabnocci(j))            