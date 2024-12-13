# Range(): Range function returns a sequence of numbers, starting from 0 by defult, and increments by 1 (by default), and stops before a specified number.

# range(start?,stop,step?)
      
for el in range(5):
    print(el)
for el in range(1, 5):
    print(el)
for el in range(1,5,2):
    print(el)

#code:

for i in range(1,100,2):     ##@ ghor kore digit print hobe 100 porjonto
    print(i)

for i in range(1,100,3):    #3 3 ghor kore digit print hobe 100 porjonto
    print(i)

# Practice:

# Print numbers from 1 to 100.
# ans:

for i in range(1, 101):
    print(i)


# Print numbers from 100 to 1.
# ans:

for i in range(100,0,-1):    ## boro theke choto chaile tokhn minus ashbe
    print(i)


# print the multiplication table of a number n.
# ans:

n = int (input("enter number : "))

for i in range(1, 11):
    print(n*i)

