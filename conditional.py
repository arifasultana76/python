light = input ("light color:")

if (light == "red"):
    print ("stop")
elif (light == "yellow"):
    print ("look")  
elif (light == "green"):             
    print ( "go")
else:                            ## else is work when all above condition is false or not work
    print ("light is broken")   

age = 23

if (age >= 18):
    print("can vote")        ## before print space ( 4 space) called Indentation 
else:
    print("can not vote")

age = 23
if(age >=18):
   print("can vote and apply for lisence")   ## If condition is True then ans will come.

age = 15
if(age >=18):
    print("can vote and apply for lisence")    ## If condition is not true then ans will not come.

age = 23
if(True):                    ## If i write True in if condition then ans will be True.
    print("can vote")
    print("can drive")
    
age = 23
if(False):                    ## If i write False in if condition then ans will not come.
    print("can vote")
    print("can drive")

num = 5
if(num>2):
    print("greater than 2")
if(num>3):                        ## Here's ans will come both statement cause both condition is if condition
    print("greater than 3")     

num = 5
if(num>2):
    print("greater than 2")
elif(num>3):                        ## elif condition is work when if condition ans will be false.
    print("greater than 3")         ## Otherwise elif condition is not work.

marks = int (input("enter student marks: "))
if (marks >=90):
    grade = "A"
elif(marks >=80 and marks <90):
    grade = "B"
elif(marks >= 70 and marks <80):
    grade = "C"
else:
    grade = "D"

print("Grade of the student ->", grade)

# Nesting: ( two statements within a single statement are called nesting.)

age = 5
if ("age>=18"):
    if("age>=80"):
       print("can not drive")  ## this 2 statement are false then ans can not drive.
    else:                      ## this 2 statement if one statement is True and 2nd one is false
       print("can drive")      ## then go to else statement
else:
    print("can not drive")

# Practice:

# WAP to check if a number entered by the user is odd or even.
num = int (input("enter number:"))
rem = num % 2
if(rem == 0):
    print("Even")
else:
    print("odd")    

# WAP to find the greatest of 3 numbers entered by the user.
a = int (input("enter first number: "))
b = int (input("enter second number: "))
c = int (input("enter third number: "))

if(a>=b and a>=c):
    print("first number is largest", a)
elif(b>=c):
    print("second number is largest", b)
else:
    print("third number is largest", c)

## WAP to check if a number is a multiple of 7 or not.
x = int(input("enter number: "))

if(x % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple")
