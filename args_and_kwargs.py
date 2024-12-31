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

def order_pizza(size, *toppings, **details):
    print(f"Ordered a (size) pizza with the following toppings:")       # ? ans not correct
    for topping in toppings:
        print(f"- (toppings)")
    print(details)

order_pizza ("large","pepperoni","olives", delivery=True, tip=5) 