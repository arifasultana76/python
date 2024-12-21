#Polymorphism: Operator Overloading
# When the same operator is allowed to have different meaning according to the context.

# operators & Dunder functions

# a+b #addition         a._ _add_ _(b)
# a-b  #subtraction     a._ _sub_ _(b)
# a*b  #multiplication  a._ _mul_ _ _(b)
# a/b  #division        a._ _truediv_ _ _(b)
# a%b  #addition        a._ _mod_ _ _(b)

#poly means onek # mor means forms like face .Dunder means double under score.

#code:

# print(1+2)                  #3
# print("arifa" + "sultana")  #concatenate  #class str
# print([1,2,3] + [4,5,6])    #merge #this is type of polymorphism.

# print(type([1,2,3]))

#Complex num: i,j,k 
#complex num 2 part:

# 1i + 3j (here's 1i real part and 3j imagine part)

#        5i + 10j
#    +  -1i + 8j
#         4i +18j

#code:

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i+", self.img,"j")


# num1 = Complex(1,3)
# num1.showNumber()

#code:

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i+", self.img,"j")


# num1 = Complex(1,3)
# num1.showNumber()

# num2 = Complex(4,6)
# num2.showNumber()

#code:

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i+", self.img,"j")

#     def add(self, num2):
#         newReal = self.real + num2.real    #new num add korar jonno
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)
    

# num1 = Complex(1,3)
# num1.showNumber()                              

# num2 = Complex(4,6)
# num2.showNumber()

# num3 = num1.add(num2)
# num3.showNumber() 

#code:

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i+", self.img,"j")

#     def add(self, num2):
#         newReal = self.real + num2.real    
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)
    

# num1 = Complex(1,3)
# num1.showNumber()

# num2 = Complex(4,6)
# num2.showNumber()

# print(num1 + num2)               #Error ashbe. complex case a + use korte parbo na,


# num3 = num1.add(num2)
# print(num3)

#code:

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i+", self.img,"j")

#     def __add__(self, num2):                  #Dunder function (__add__)
#         newReal = self.real + num2.real    
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)
    

# num1 = Complex(1,3)
# num1.showNumber()

# num2 = Complex(4,6)
# num2.showNumber()

# num3 = num1 + num2                    #Dunder function use korate nw error ashbe na.
# num3.showNumber()

#code:

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i+", self.img,"j")

    def __add__(self, num2):                  
        newReal = self.real + num2.real    
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):                  #minus er jonno sub dunder function use hoyeche.      
        newReal = self.real - num2.real    
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1 - num2                  
num3.showNumber()