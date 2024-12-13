# Loop are used for sequential traversal.For traversing list,
#     string,tuples etc.
## For loop:

# for el in list:
#   some work

# for loop with else
# for el in list:
#  some work
# else:
#   works when loops end

##code:

# nums =[1,2,3,4,5]      ##list a for loop er use

# for val in nums:
#     print(val)

#Code:

# vegetables = ["potato","cucumber","carrot"]               ##String a for loop er use
 
# for val in vegetables:
#     print(val)


# tup =(1,2,3,4,2,8,9)   ##tuple a loop er use

# for num in tup:
#     print(num)

#Code:

# str = "Arifa"

# for char in str:
#     print(char)

#code:

# str = "Arifa"

# for char in str:            
#     print(char)
# print("End")


#code:

# str = "ArifaSultana"              ## i can't understand

# for char in str:
#     if(char == 'a'):
#         print("a found")
       
#     print(char)
# else:
#     print("end")

#if i remove letter a then :

str = "ArifaSultana"
new_str = ''
for char in str:
    if(char != 'a'):
        new_str += char

print(new_str)


##practice:

##print the element of the following list using a loop
#(1,4,9,16,25,36,49,64,81,100,)

#Ans:

# nums = [1,4,9,16,25,36,49,64,81,100]

# for el in nums:
#     print(el)



##Search for a number x in this tuple using loop.

#Ans:

# nums = [1,4,9,16,25,36,49,64,81,100,49]
# x = 49
# idx = 0
# for el in nums:
#     if(el == x):
#        print("number found of idx", idx)
#     idx += 1

#code:

# nums = [1,4,9,16,25,36,49,64,81,100,49]
# x = 49
# idx = 0
# for el in nums:
#     if(el == x):
#        print("number found of idx", idx)   #break use korle tokhn ekbar e idx ashbe
#        break
#     idx += 1



