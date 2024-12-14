# WAP to print the length of a list.(list is the parameter)

cities = ["dhaka","ctg","khulna","rajshahi","cumilla"]
heroes =["salam","rofik","shofik","jobbar"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

# WAP to print the elements of a list in a single line.(list is the parameter)

cities = ["dhaka","ctg","khulna","rajshahi","cumilla"]
heroes =["salam","rofik","shofik","jobbar"]

print(heroes[0])
print(heroes[1])

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

#another code:

cities = ["dhaka","ctg","khulna","rajshahi","cumilla"]
heroes =["salam","rofik","shofik","jobbar"]

print(heroes[0], end=" ")          #space er jonno end use kora hoyeche
print(heroes[1], end=" ")

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

#another code:

cities = ["dhaka","ctg","khulna","rajshahi","cumilla"]
heroes =["salam","rofik","shofik","jobbar"]


def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heroes)
print()                   #here's print() use na korleo hoy tahole kno use koreche


# WAP to find the factorial of n.(n is the parameter)

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(6)


# WAP to covert USD to INR.

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USD =", inr_val,"INR")

converter(1)