# Functions: Block of statements that perform a specific task.

def calc_sum (a,b):             #redundent method a work kore
    sum = a+b                   #def means define
    print(sum)
    return sum

calc_sum(5,10)

calc_sum(5,20)

calc_sum(50,30)

#code:#function_definition

def calc_sum(a,b):            #first braket er vitorer 2 ta digit k parameters
    return a+b              

sum = calc_sum(123,234)       # ae line k function call bole
print(sum)                    # first braket er vitorer 2 digit k argument bole


def print_hello():            #function a return value dite hobe must
    print("hello")

print_hello()


#average of 3 numbers:

def calc_avg(a,b,c):
                     
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg

calc_avg(55,66,77)

#another code:

def calc_avg(a,b,c):
    if(a == 0):                  # i can't understand
     sum = a+b+c
    avg = sum/3
    print(avg)
    return avg

calc_avg(55,66,77)


# Function 2 types. 1.Built in functions  2.User defined functions 
#Built function: print(),len(),type(),range()


print("Arifa","Sultana")

print("ArifaSultana", end=" ")   #space hocche na kno!

# Default parameters: Assigning a default value to parameter, which is used when no argument is passed.

def cal_prod(a=1,b=2):
    print(a*b)
    return a*b
cal_prod()

#another way:

def cal_prod(a,b=2):
    print(a*b)
    return a*b
cal_prod(2)

