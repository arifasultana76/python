# Del keyword: Used to object properties or object itself.

# del s1.name
# del s1

# Code:

# class student:
#     def __init__(self, name):
#         self.name = name

# s1 = student("Arifa")
# print(s1.name)                   # can't understand
# del s1.name
# print(s1.name)

# Private (like) attributes & methods:
# conceptual implementations in python

# private attributes & methods are meant to be used only within the class and are not
# accessible from outside the class.

#code:

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass   #acc_pass er age 2 ta under score lagiye dile secure hoye jabe.
    
#     def reset_pass(self):           #ae 2 line under class
#         print(self.__acc_pass)


# acc1 = Account("12345","abcd")

# print(acc1.acc_no)             #ae function class er bahire. ekhane __acc__no ae ta kaj korbe na.
# print(acc1.reset_pass())      #account obj no attribute account password

#code:

# class person:
#     __name = "anonymous"

#     def __hello(self):
#         print("hello person!")

#     def welcome(self):
#         self.__hello()

# p1 = person()

# print(p1.welcome())

# Inheritance: when one(child/drived) derives the properties & methods of another class(parent/base).
# Inheritance 3 types. 1. Single inheritance 2. Multi-level inheritance 3. Multiple inheritance


# class car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class ToyotaCar(car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# car1 = ToyotaCar("prius")

# print(car1.name)

#code:

# class car:
   
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class ToyotaCar(car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# car1 = ToyotaCar("prius")

# print(car1.start())

#Single inheritance: like parent & child

#code:

# class car:
#     color = "Black"
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class ToyotaCar(car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# car1 = ToyotaCar("prius")

# print(car1.color)

# Multi level inheritance: like parents ,child thn child.
#(car,toyotacar,fortune)
# code:

# class car:
   
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class ToyotaCar(car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("diesel")
# car1.start()

# Multiple inheritance: parent 1, parent 2 thn child.

#code:

# class A:
#     varA = "Welcome to class A"

# class B:
#     varB = "Welcome to class B"

# class C(A,B):
#     varC = "Welcom to class C"

# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)


# Super method: super () method is used access methods of the parent class.
#parent class
#code:

# class car:
#     def __init__(self, type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class ToyotaCar(car):
#     def __init__(self, name, type):
#         super().__init__(type)          
#         self.name = name
#         super().start()
       

# car1= ToyotaCar("prius","electric")
# print(car1.type)

# Class method: A class method is bound to the class & receives the class as an implicit first argument.

# Note: static method can't access or modify class state & generally for utility.

# class Student:
#     @classmethod #decorator
#     def college(cls):
#         pass

#code:

# class Person:
#     name = "anonymous"

#     def changeName(self, name):
#         self.name = name

# p1 = Person()
# p1.changeName("Arifa sultana")
# print(p1.name)      

#code:

# class Person:
#     name = "anonymous"

#     def changeName(self, name):
#         self.name = name

# p1 = Person()
# p1.changeName("Arifa sultana")
# print(p1.name) 
# print(Person.name)

#code:

# class Person:
#     name = "anonymous"

#     def changeName(self, name):
#         Person.name = name

# p1 = Person()
# p1.changeName("Arifa sultana")
# print(p1.name) 
# print(Person.name)

#code:

# class Person:
#     name = "anonymous"

#     def changeName(self, name):  #self hocche obj
#        self.__class__.name = "Arifa"

# p1 = Person()
# p1.changeName("Arifa sultana")
# print(p1.name) 
# print(Person.name)

#Code:

# class Person:
#     name = "anonymous"

    # def changeName(self, name):
    #    self.__class__.name = "Arifa"

# @classmethod
# def changeName(cls, name):
#     cls.name = name


# p1 = Person()
# p1.changeName("Arifa sultana")
# print(p1.name) 
# print(Person.name)

#Note: 
#class attributor k use korle class method hobe.
#class jodi intrance k or er properties k touch na kore tokhn static method hobe.
#self intrance properties use korle tokhn intrance method hobe.

# Property decorator: We use property decorator on any method in the class to use the method as a property.

#code:

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
  

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

Stu1 = Student(98,95,90)           # can't understand                      #attributes er valu depends on function.
print(Stu1.percentage)

Stu1.phy = 85
print(Stu1.percentage)


