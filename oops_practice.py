# Que: Define a circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define a perimeter() method of the class which allows you to calculate the perimeter of the circle.

#code:
#Note: area of the circle = pai r squre . perimeter = 2 pai r.

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2
    
#     def perimeter(self):
#         return 2 * 3.14 * self.radius

# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())

#Code:

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius ** 2     # can't understand. 22/7 kno dilo?
    
#     def perimeter(self):
#         return 2 * (22/7) * self.radius

# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())


#Que: Define a Employee class with attributes role, department & salary.This class also has a showDetails() method.

#Code:

# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("role =", self.role)
#         print("dept=", self.dept)
#         print("salary =", self.salary)

# e1 = Employee("accountant", "Finance", "60,000")
# e1.showDetails()


# Create an engineer class that inherits properties from Employee & has additional attributes:name & age.

#Code:

# class Employee:
#     def __init__(self, role, dept, salary):                  # this code is inheritance practice code.
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("role =", self.role)
#         print("dept=", self.dept)
#         print("salary =", self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer","IT","75,000")

# engineer1 = Engineer("Elon mask", 40)
# engineer1.showDetails()



# Creat a class called Order which stores item & its price.
# use Dunder function__gt__() to convey that:
# order1 > order2 if price of order1 > price of order2.

#code:

class Order:
    def __init__(self, item, price):
      self.item = item
      self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price

ord1 = Order("chips", 20)
ord2 = Order("tea", 15)  

print(ord1 > ord2)       #true


