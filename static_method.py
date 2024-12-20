# Static methods: Methods that don't use the self parameter(work at class level)

# class student:
#     @staticmethod   #decorator
#     def college():
#         print("ABC College")

# code:

class student:

    def __init__(self,name, marks):    # can't find mistake
        self.name = name
        self.marks = marks   

    @staticmethod
    def hello():
        print("hello") 

    def get_avg(self): 
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name,"your avg score is: sum/3")

s1 = student("Arifa", [90,95,98])
s1 = get_avg()
s1.hello()


