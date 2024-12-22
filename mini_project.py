
# ! Mini project name: Guess the number

# ? random num --> target num
# ? your num < target

# * project:

# import random 

# randNum = random.randint(1,5)          #jotobar run korbo random num ashbe.
# print(randNum)



# import random 

# target = random.randint(1, 100) 

# while True:
#     userChoice = int(input("Guess the target: "))
#     if(userChoice == target):
#         print("Success : Correct Guess!!")
#         break
#     elif(userChoice < target):
#         print("Your number was too small. Take a bigger guess....")
#     else:
#         print("Your number was too big. Take a smaller guess...")


# print("______GAME OVER______")


# Code:

# import random 

# target = random.randint(1, 100) 

# while True:
#     userChoice = input("Guess the target or Quit(Q): ")
#     if(userChoice == "Q"):
#         break

#     userChoice = int(userChoice)
#     if(userChoice == target):
#         print("Success : Correct Guess!!")
#         break
#     elif(userChoice < target):
#         print("Your number was too small. Take a bigger guess....")
#     else:
#         print("Your number was too big. Take a smaller guess...")


# print("______GAME OVER______")


#Code:

import random 

target = random.randint(1, 100) 

while True:
    userChoice = input("Guess the target or Quit: ")
    if(userChoice == "Quit"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("Your number was too small. Take a bigger guess....")
    else:
        print("Your number was too big. Take a smaller guess...")


print("______GAME OVER______")

