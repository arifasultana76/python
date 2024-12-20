#OOP: To map with real world scenarios,we started using objects in code.
#this is called object oriented programming.

# procedural vabe kaj kore mane sequencely program lekha.
#function er concept ashbe oop code a.Function use kora mandatory na.
#Returdencing(upor theke niche jaoa) & reusability(choto function ba code bar bar use kora)
#object => class
#list,string egulo object.

# a = 10
# b = 20

# sum = a+b
# print(sum)   #this is sequence 

# Class & Object in python:

# class is a blueprint for creating objects.
# Creating Class:

# class student:
#     name = "Arifa Sultana"


# Creating Object (instance) #instance means class

#code:

# s1 = student()
# print(s1.name)


# class student:
#     name = "Arifa Sultana"

# s1 = student()
# print(s1.name)

# s2 = student()
# print(s2.name)

#code:

# class car:
#     color ="blue"
#     brand = "Mercedes"
# car1 =car()
# print(car1.color)
# print(car1.brand)

#constructor:
# __init__Function:
# Constructor: All classes have a function called_init_(),which is always executed when the class is being initiated.
#function automatic init function create kore dibe.

#code:

# class student:
#     name = "Arifa"
#     def __init__(self):                   #self parameter means object nai tokhn self lekha lage 
#        print("Adding new student in Database..")
    
# s1 = student()

#code:

# class student:
#     name = "Arifa"
#     def __init__(self): 
#         print(self)
#         print("Adding new student in Database...")                  
    
# s1 = student()
# print(s1)

#code:

# class student:

#     def __init__(self, fullname):  
#        self.name = fullname                  
#        print("Adding new student in Database..")
    

# s1 = student("Arifa Sultana")
# print(s1.name)

#code:

# class student:

#     def __init__(abc, fullname):           #self likhte hobe na emon na.jekono nam lekha jabe.
#        abc.name = fullname                  
#        print("Adding new student in Database..")
    

# s1 = student("Arifa Sultana")
# print(s1.name)


# The self is the parameter is a reference to the current instance of the class, and is used to access variables
# that belongs to the class. and It is used to access variable.

#code:

# class student:

#     def __init__(self, fullname):    # Its constructor work korteche
#        self.name = fullname            #def theke full name porjonto constructor line bole.      
#        print("Adding new student in Database..")
    
# s1 = student("Arifa")
# print(s1.name)

# s2 = student("Sultana")
# print(s2.name)

#code:

# class student:

#     def __init__(self,name, marks):  
#        self.name = name
#        self.marks = marks                  
#        print("Adding new student in Database..")
   
# s1 = student("Arifa", 96)
# print(s1.name, s1.marks)

# s2 = student("Sultana", 88)
# print(s2.name, s2.marks)

#code:

    #parameterize_constructors: (def theke database porjonto)

# def __init__(self,name, marks):  
#     self.name = name
#     self.marks = marks                  
#     print("Adding new student in Database..")

#code:

# class student:

#     def __init__(self,name, marks):  
#         self.name = name
#         self.marks = marks                  
#         print("Adding new student in Database..")

# s1 = student("Arifa", 96)
# print(s1.name, s1.marks)

# s2 = student("Sultana", 88)
# print(s2.name, s2.marks)


# Class & Instance Attributes:

#code:

# class student:
#     college_name ="ABC college"
# def __init__(self,name, marks):  
#     self.name = name
#     self.marks = marks                  
#     print("Adding new student in Database..")

# s1 = student("Arifa", 96)
# print(s1.name, s1.marks)

# s2 = student("Sultana", 88)
# print(s2.name, s2.marks)

# print(s2.college_name)    #here's student.college_name dileo same print hobe.

#code:

# class student:
#     college_name ="ABC college"
#     name: "anonymous"      #class sttr

#     def __init__(self,name, marks):  
#         self.name = name      #obj attr > class attr
#         self.marks = marks                  
#         print("Adding new student in Database..")

# s1 = student(" ", 96)                # ae code tay bujhate cheyeche student nam na dileo by default anonymous hobe. but seta hocche na.
# print(s1.name)

# obj.attributes er priority beshi thake class atrributes er theke.

# Method: Methods are functions that belong to objects.

#Creating class:

# class Student:
#     def __init__(self,fullname):    # It  is constructor
#       self.name = fullname

#     def hello(self):     # It is method
#         print("hello",self.name)

#Creating object:

# s1 = Student("Arifa")
# s1.hello()  # here's s1 object r hello hocche method

#code:

# class student:
#     college_name ="ABC college"

#     def __init__(self,name, marks):  
#         self.name = name
#         self.marks = marks                  

#     def welcome():                      # error ashbe.
#         print("welcome student")

# s1 = student("Arifa", 96)
# s1.welcome()

#code:

# class student:
#     college_name ="ABC college"

#     def __init__(self,name, marks):  
#         self.name = name
#         self.marks = marks                  

#     def welcome(self):
#         print("welcome student")                      

# s1 = student("Arifa", 96)
# s1.welcome()

#Code:

# class student:
#     college_name ="ABC college"

#     def __init__(self,name, marks):  
#         self.name = name
#         self.marks = marks                  

#     def welcome(self):
#         print("welcome student", self.name) #welcome & name eksathe print hobe.                     

# s1 = student("Arifa", 96)
# s1.welcome()

#code:

# class student:
#     college_name ="ABC college"

#     def __init__(self,name, marks):  #constructor object k initialize kore.
#         self.name = name
#         self.marks = marks                  

#     def welcome(self):
#         print("welcome student,", self.name) 
#     def get_marks(self): 
#         return self.marks  

# s1 = student("Arifa", 96)
# s1.welcome()
# print(s1.get_marks())

#Code:

class student:
    college_name ="ABC college"

    def __init__(self,name, marks):  
        self.name = name
        self.marks = marks                  

    def welcome(self):
        print("welcome student,", self.name) 
    def get_marks(self): 
        return self.marks  

s1 = student("Arifa", 96)
s1.welcome()
print(s1.get_marks())

s2 = student("Rimi", 90)
s2.welcome()
print(s2.get_marks())