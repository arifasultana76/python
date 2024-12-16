# WAP to find the sum of first n numbers.(using while)

n = 5

for i in range(1, n+1):
    print(i)


n = 5

sum = 0
for i in range(1, n+1):
    sum += i

print("total sum =", sum)

# 1+2+3+4+5
n = 5

sum = 0                         ##While loop diye korte bolche
for i in range(1, n+1,1):        
    sum += i
print("total sum =", sum)

#code:

n = 5
sum = 0
i = 1                       
while i <= n:
    sum += i 
    i += 1   

print("total sum =", sum)

#WAP to find the factorial of first n numbers.(using for)
#Ans:

n = 5
fact = 1
i = 1                       
while i <= n:             #While loop diye code
    fact *= i 
    i += 1   

print("factorial =", fact)

#or

n = 5
fact = 1
                      
for i in range(1, n+1):                ## For loop diye code
    fact *= i 
    i += 1   

print("factorial = ",fact)
