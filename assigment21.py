"""
#answer-1
def first_n(n):
    if n>0:
       first_n(n-1)   
       print(n,end='')
n=int(input("Enter the no :"))    
first_n(n)

#answer-2
def rev_n(n):
    for i in range(n,1,-1):
        print(i,end=' ')
n=int(input("Enter the no : "))
rev_n(n)        
"""
#answer-3
def odd(l):
    for i in range(1,l+1,+2):
      print(i)
    
l=int(input("Enter the no:"))
odd(l)             
"""
#answer-4
def odd_rev(n):
    if n%2==1:
       for i in range(n,0,-2):
              print(i)
    else:
        for i in range(n-1,0,-2):
              print(i)
n=int(input("Enter the no:"))
odd_rev(n)                  

#answer-5
def even_no(n):
    if n%2==0:
        for i in range(2,n+1,+2):
            print(i)
    else:
        for i in range(2,n,+2):
            print(i)
n=int(input("Enter the no:"))
even_no(n)                    
#answer-6
def even_rev(k):
    if k%2==0:
        for i in range(k+1,1,-2):
            print(i)
    else:
        for i in range(k-1,1,-2):
            print(i)
k=int(input("Enter the no:"))
even_rev(k)                    
#answer-7
def sum_square(a):
    if a==1:
        return 1
    return a*a+sum_square(a-1)
a=int(input("Enter the no:"))
print(sum_square(a))
    
#answer-8
def sum_cube(b):
    if b==1:
        return 1
    return b*b*b+sum_cube(b-1)
b=int(input("Enter the no:"))
print(sum_cube(b))

#answer-9
def n_mul(c):
    if c==1:
        return 1
    return c*n_mul(c-1)
c=int(input("Enter the no:"))
print(n_mul(c))                  

#answer-10
def rev_ord(d):
    if d==1:
        return 1
    return d,rev_ord(d-1) 
d=int(input("Enter the no:"))
print(rev_ord(d))       
"""