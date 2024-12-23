
# ? Create student class that takes name & marks of 3 subjects as arguments in constructor.
# ? then create a method to print the average.

#ans:

 
# class student:

def __init__(self, name, marks):  
        self.name = name
        self.marks = marks 

def get_avg(self):
    sum = 0
    for val in self.marks:
            sum += val
    print("Hi", self.name," your avg score is:", sum/3 )

    

s1 = student("Arifa", [95,98,94])
s1.get_avg()


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
s2.get_avg()           # ! marks na likhleo evabe arekta student er avg ashar kotha!


# ? Create Account class with 2 attributes - balance & account no.
# ? Create methods for debit, credit & printing the balance.

#Ans:

class Account:
    def __init__(self,bal, acc):
        self.balance = bal
        self.account_no = acc
      
     #debit_method

    def debit(self, account):
        self.balance -= account
        print("Rs.", account, "was debit")
        print("Total balance = ", self.get_balance())

    def credit(self, account):
        self.balance += account
        print("Rs.", account, "was credit")
        print("Total balance = ", self.get_balance())
    def get_balance(self):
        return self.balance
    
acc1 = Account(100000,12450)
print(acc1.balance)
print(acc1.account_no)

#code:


class Account:
    def __init__(self,bal, acc):
        self.balance = bal
        self.account_no = acc

     #debit_method
    def debit(self, account):
        self.balance -= account
        print("Rs.", account, "was debit")
        print("Total balance = ", self.get_balance())

    def credit(self, account):
        self.balance += account
        print("Rs.", account, "was credit")
        print("Total balance = ", self.get_balance())
    def get_balance(self):
        return self.balance
    
acc1 = Account(100000,12450)
acc1.debit(10000)
acc1.credit(500)
acc1.debit(5500)
acc1.credit(4000)


