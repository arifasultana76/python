# Create student class that takes name & marks of 3 subjects as arguments in constructor.
#then create a method to print the average.

#ans:

 
# class student:

#     def __init__(self,name, marks):  
#         self.name = name
#         self.marks = marks 

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name," your avg score is:", sum/3 )

    

# s1 = student("Arifa", [95,98,94])
# s1.get_avg()


#another code:

class student:

    def __init__(self,name, marks):  
        self.name = name
        self.marks = marks 

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name," your avg score is:", sum/3 )

    

s1 = student("Arifa", [95,98,94])
s1.get_avg()

s2 = student("Rimi")   
s2.get_avg()           # marks na likhleo evabe arekta student er avg ashar kotha!