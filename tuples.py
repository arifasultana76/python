# Tuples: Tuples means a built-in data type that lets us create immutable sequences of values.
# List = mutable
# Strings & Tuple = immutable

tup =(2,1,3,1)
print(type(tup))

tup =(2,1,3,1)
print(tup[0])
print(tup[1])

tup =(2,1,3,1)
print(tup[0])
print(tup[1])

tup = ("Arifa")
print(type(tup))

tup = ("Arifa")
print(tup[1:3])

tup = (1,2,3,4,5)
print(tup[2:3])

tup = (1,2,3,4,5)
print(tup[1:3])

tup =(1,2,3,4,5)        ## Don't understand this
print=(tup[-1:-2])

tup =(1,2,3,4,5)
print(tup[:-1])

tup =(1,2,3,4,5)
print(tup[-2:])

tup =(1,2,3,4,5)
print(tup[-3:-1])

# Tuple_Method:

tup =(1,2,3,4,5)
print(tup.index(2))       ## 2 er index 1 so ans will be 1

tup =(1,2,3,2,2,3)          ## 2 element koto bar ache seta hobe ans
print(tup.count(2))

#Practice:
# WAp to ask the user to enter names of their 3 favorite movies & store them in a list.

movies =[]
mov1 = input("enter 1st movie: ")
mov2 = input("enter 2nd movie: ")
mov3 = input("enter 3rd movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

##another method:

movies =[]
mov = input("enter 1st movie: ")
movies.append(mov)
mov = input("enter 2nd movie: ")
movies.append(mov)
mov = input("enter 3rd movie: ")
movies.append(mov)

print(movies)

##another method:

movies =[]
movies.append(input("enter 1st movie: "))
movies.append(input("enter 2nd movie: "))
movies.append(input("enter 3rd movie: "))

print(movies)

# WAp to check if a list contains a palindrome of elements.(Hint:use copy()method)

list1 =[1, 2, 1]
list2 =[1, 2, 3]

copy_list1 =list1.copy()    ##palindrome num ber korte hole always reverse() statement use korte hobe
copy_list1.reverse()         

if(copy_list1 == list1):
   print("palindrome")
else:
   print("Not palindrome")


list1 =[1, 2, 1]

copy_list1 =list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
   print("palindrome")
else:
   print("Not palindrome")



list1 =["m", "a", "a", "m"]

copy_list1 =list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
   print("palindrome")
else:
   print("Not palindrome")

# WAP to count the number of students with the "A" grade in the following tuple.
 
grade = ["C", "D", "A", "A", "B", "B" ,"A"]
print(grade.count("A"))


# Store the above values in a list & sort them from "A" to "D"

grade = ["C", "D", "A", "A", "B", "B" ,"A"]
grade.sort()
print(grade)







