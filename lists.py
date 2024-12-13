marks =[90.2,60.3,50.55,80.66,70.22]
print(marks)
print(marks[0])
print(marks[1])
print(len(marks))

student = ["Arifa",85,50.22,"Dhaka"]    ##String = immutable(unchangeable ##mutable = mutable(changeable)
print(student[0])

student = ["Arifa",85,50.22,"Dhaka"]      ##list 0,1,2,3.... evabe count hobe
print(student[3])                         ## Ans will be Dhaka

# List Slicing:

marks = 55,85,70,95,80
print(marks[0:5])


marks = 55,85,70,95,80
print(marks[0:])


marks = 55,85,70,95,80
print(marks[2:])


marks = 55,85,70,95,80
print(marks[-3:-1])


marks = 55,85,70,95,80
print(marks[-5:-1])


marks = 55,85,70,95,80
print(marks[-5:])

## List Method:
##list.append():

list =[1,2,3]
list.append(4)
print(list)

list =[1,2,4]
list.append(2)               ## list.append means input element adding in list
print(list)

## List.sort():

# sorting 2 type ascending & descending
# Ascending means small to big (0,1,2..)
# Descending means big to small (2,1,0....)

list =[1,2,3]
print(list.sort())   ## Result will be none

list =[1,2,3]
print(list.sort())     ## Print(list) dileo reverse result not come
print(list)    


list =["banana","litchi","mango"]
print(list.sort("banana"))          ## sort er vitore string hobe na


list =["banana","litchi","mango"]
print(list.sort(reverse=True))
print(list)


list =["banana","litchi","mango"]
print(list.sort(reverse=False))
print(list)

list =['a','d','e','f','c','b']
print(list.sort())
print(list)

list =['Arifa','Rakib']
print(list.sort(reverse=True))
print(list)

## List.reverse():

list =['a','d','e','f','c','b']
list.reverse()
print(list)

## List.insert(idx,el):

list = [2,1,3]
list.insert(1,5)      ## insert means element add. ans will be 2,5,1,3
print(list)

## List.remove(1):

list = [2,1,3]
list.remove(1)     ##Jeta remove korte chai seta braket er moddhe likhle seta remove hobe    
print(list)

list =["Arifa"]
list.remove("Arifa")       
print(list)

## List.pop(idx):

list =[1,2,3,4]      ##List.pop braket a index position num dile that position remove hobe.
list.pop(2)          ## Here's 2 means index position 3 will be remove  
print(list)  
































