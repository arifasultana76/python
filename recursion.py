# Recursion: when a function calls itself repeatedly.
# prints n to 1 backwords

def arifa(n):
    if(n == 0):       # base case
        return
    print(n)
    arifa(n-1)

arifa(5)

#another code:

def show(n):
    
    if(n == -1):       
        return
    print(n)
    show(n-1)

show(5)
 
#another code:

def show(n):
    
    if(n == 0):       
        return
    print(n)
    show(n-1)
    print("End")
show(3) 

#Another code:

#returns n!
# 0!=1  # 1!=1      (default value)
# n! = (n-1)! x n   (recurence relation)

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return fact(n-1) * n        
print(fact(5))