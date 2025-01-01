
#* Args: Arbitrary argument.
#* Kwargs: Keyword arbitrary argument.

#? args k 1 ti * diye lekha hoy r kwargs k 2 ti * diye lekha hoy.
#* args = allows you to pass multiple non-key arguments.
#* kwargs = allows you to pass multiple keyword-arguments.

#* unpacking operator:
#? 1. positional 2. default 3. keyword 4.Arbitrary

#? Args = tuple hisebe hoy
#? kwargs = dictionary function hisebe hoy.

#? Args code:

# def add(*args):
#     print(type(args))   # it's tuple type

# add(1, 2, 3)

#code:

# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total

# print(add(1))

#code:

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("spongebob", "squarepants")

#code:

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Dr.", "Spongebob", "harold", "Squarepants","III")

#? Kwargs code:

# def print_address(**kwargs):
#     print(type(kwargs))        #it's dictionary type

# print_address(street="123 fake st.",
#               city="Detroit", 
#               state="MI",
#               zip="54321")

#code:

# def print_address(**kwargs):
#     for key in kwargs.keys():
#         print(key)

# print_address(street="123 fake st.",
#               city="Detroit", 
#               state="MI",
#               zip="54321")

#code:

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_address(street="123 fake st.",
#               apt="100",
#               city="Detroit", 
#               state="MI",
#               zip="54321")

#code:

# def shipping_label(*args,**kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
#     for value in kwargs.values():
#         print(value, end=" ")

# shipping_label("Dr.","Spongebob","Squarepants","III",   # it's arbitrary positional argument
#                street="123 fake st.",                  # It's arbitrary key words argument
#                apt="100",
#                city="Detroit",
#                state="MI",
#                zip="54321")

#code:

# def shipping_label(*args,**kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
    
#     print(f"{kwargs.get("street")}")

# shipping_label("Dr.","Spongebob","Squarepants",   # it's arbitrary positional argument
#                street="123 fake st.",                  # It's arbitrary key words argument
#                apt="100",
#                city="Detroit",
#                state="MI",
#                zip="54321")

#code:


# def shipping_label(*args,**kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
    
#     print(f"{kwargs.get('street')}")
#     print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

# shipping_label("Dr.","Spongebob","Squarepants",        # it's arbitrary positional argument
#                street="123 fake st.",                  # It's arbitrary key words argument
#                apt="100",
#                city="Detroit",
#                state="MI",
#                zip="54321")

#code:

# def shipping_label(*args,**kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()

#     if "apt" in kwargs:
#         print(f"{kwargs.get('street')} {kwargs.get('apt')}")
#     else:
#          print(f"{kwargs.get('street')}")

#     print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

# shipping_label("Dr.","Spongebob","Squarepants",        
#                street="123 fake st.",                 
#                apt="#100",
#                city="Detroit",
#                state="MI",
#                zip="54321")

#code:

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")



    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.","Spongebob","Squarepants",        
               street="123 fake st.",                 
               pobox="po box #1001",
               city="Detroit",
               state="MI",
               zip="54321")


#another lecture:


# nums = [2, 5, 7, 1, 9]
# print(nums)
# print(*nums)    # ? when i used this way it's called unpacking operator


# def order_pizza(size, *toppings):              # ? can't understand. ans not correct
#     print(f"Ordered a (size) pizza.")
#     print(toppings)

# order_pizza ("large","pepperoni","olives")

# def order_pizza(size, *toppings):
#     print(f"Ordered a (size) pizza with the following toppings:")       # ? ans not correct
#     for topping in toppings:
#         print(f"- (toppings)")

# order_pizza ("large","pepperoni","olives")

# def order_pizza(size, *toppings, **details):
#     print(f"Ordered a (size) pizza with the following toppings:")       # ? ans not correct
#     for topping in toppings:
#         print(f"- (toppings)")
#     print(details)

# order_pizza ("large","pepperoni","olives", delivery=True, tip=5) 