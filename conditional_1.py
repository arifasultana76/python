while True:
    age = int(input("age: ")) 
    if age <= 13:
        print("You are a kid")
       
    elif age < 18:
        print("You are a teenager")
       
    elif age >= 18:
        print("You are an adult")