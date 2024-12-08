## Set: Set is the collection of the unordered items. Sets mutable
## Each elements in the set must be unique & immutable.

# nums = {1,2,3,4}
# set2 = {1,2,2,2}

##repeated elements stored only once,so it resolved to(1,2)

# null_set = set()  #empty set syntex

collection ={1,2,3,4}

print(collection)
print(type(collection))


collection ={1,2,3,4,"Hello!","Rimi"}

print(collection)
print(type(collection))


collection ={1,2,3,4,"Hello!","Rimi"}
print(collection)


collection ={1,2,2,3,4,"Hello!","Rimi","Rimi","Arifa"}   ## Set duplicate value ignore kore
print(collection)


collection ={1,2,2,3,4,"Hello!","Rimi","Rimi","Arifa"}   
print(len(collection))          ##Total num of items


collection = {}  # Empty dictionary
print(type(collection))

collection = set()   #This is Empty Set

## Set Method:

##set.add(el):  #add an element

collection = set()
collection.add(1)
collection.add(2)
collection.add(2)

print(collection)

#set.remove(el):  #remove the element

collection = set()
collection.add(1)
collection.add(2)
collection.add(2)

collection.remove(1)
print(collection)

#OR

collection = set()
collection.add(1)
collection.add(2)
collection.add(2)

collection.remove(2)
print(collection)

#OR

collection = set()
collection.add(1)
collection.add("Arifa")
collection.add((1,2,3))
collection.add([1,2,3])    ## Unhashable type list

collection.remove(1)       ##Result will be not come
print(collection)

#OR

collection = set()
collection.add(1)
collection.add("Arifa")
collection.add((1,2,3))
collection.add("a,b")    

collection.remove(1)         ##Result will be come
print(collection)

#OR

##set.clear():  #emties the set

collection = set()

collection.add(1)
collection.add(2)
collection.add("Arifa")
collection.add((1,2,3))

collection.clear()            ##Ans will be "0"
print(len(collection))


##set.pop():    #removes a random value

collection = ["Hello","Arifa","World","coding","python"]       
print(collection.pop())


collection = {"Hello","Arifa","World","coding","python"}       
print(collection.pop())


collection = {"Hello","Arifa","World","coding","python"}         
print(collection.pop())
print(collection.pop())


##et.union(set2):  #combines both set values & returns new

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))   # ans will be{1,2,3,4}
print(set1)
print(set2)

##set.intersection(set2):   #combines common values & return new

set1 = {1,2,3}
set2 = {2,3,4}

# print(set1.intersection(set2))   #ans will be {2,3}

##Practice:

##Store following word meanings in a python dictionary:
#table: "a" piece of furniture",list of facts & figures"
#cat: "a small animal"

##Ans:

dictionary = {
    "cat" : "a small animal",
    "table" :["piece of furniture","list of facts & figures"]
    
}
print(dictionary)

#You are given a list of subjects for students.
#Assume one classroom is required for 1 subject.
#How many classrooms are needed by all students.

##Ans:

subjects = {
    "python","java","c++","python","java","python","java","c++","c"
    
}
print(len(subjects))            #Total 5 ta classroom lagbe


## WAP to enter marks of 3 subjects from the user and store them in a dictionary.
#start with an empty dictionary & add one by one.Use subject name as key & marks as value.

marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

x = int(input("enter math : "))
marks.update({"math" : x})

print(marks)

# Figure out a way to store 9 & 9.0 as separate values in the set.
# (you can take help of built in data types)

values = {9, 9.0}    ##Ans will be 9 only
print(values)

#Or

values ={9,"9.0"}     ##Ans will be 9 &9.0
print(values)

#Or

values = {
    ("float", 9.0),
    ("int",9)
}
print(values)



