
# ? Random Password Generator:

# import random

# val = random.choice([1,2,3])
# print(val)


#code:

# import random

# val = random.choice(['a', 'b', 'c'])  #random character
# print(val)

# ! punctuators: A-z , a-z, 0-9,!,/,\,-,?
# ! list --> generate --> 12 random character

#Code:

# import random
# import string

# print(string.ascii_letters)   # unique num hole ascii value

#code:

# import random
# import string

# print(string.ascii_uppercase) 

#code:

# import random
# import string

# print(string.punctuation) 

#code:

# import random
# import string

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation) 

#code:

# import random
# import string

# print(random.choice("Hello"))

#code:

# import random
# import string

# charValues = string.ascii_letters + string.digits + string.punctuation

# print(charValues)


#code:

# import random
# import string

# charValues = string.ascii_letters + string.digits + string.punctuation

# print(random.choice(charValues))

#code:


# import random
# import string

# pass_len = 12
# charValues = string.ascii_letters + string.digits + string.punctuation

# password = ""
# for i in range(pass_len):
#     print(random.choice(charValues))

#code:

# import random
# import string

# pass_len = 12
# charValues = string.ascii_letters + string.digits + string.punctuation

# password = ""
# for i in range(pass_len):
#     password += random.choice(charValues)          #This code different random password print korbe.

# print("Your random password is:", password)

#code:


# import random
# import string

# pass_len = 8
# charValues = string.ascii_letters + string.digits + string.punctuation

# password = ""
# for i in range(pass_len):
#     password += random.choice(charValues)          #This code different random password print korbe.

# print("Your random password is:", password)


# ! List comprehension: (function for i in range(n))

# import random
# import string

# pass_len = 12
# charValues = string.ascii_letters + string.digits + string.punctuation


# result = [random.choice(charValues) for i in range(pass_len)]
# print(result)

#code:

# import random
# import string

# pass_len = 12
# charValues = string.ascii_letters + string.digits + string.punctuation


# result = "A".join([random.choice(charValues) for i in range(pass_len)])
# print(result)

#code:

# import random
# import string

# pass_len = 12
# charValues = string.ascii_letters + string.digits + string.punctuation


# result = "*".join([random.choice(charValues) for i in range(pass_len)])
# print(result)


#code:

# import random
# import string

# pass_len = 12
# charValues = string.ascii_letters + string.digits + string.punctuation


# result = "".join([random.choice(charValues) for i in range(pass_len)])
# print(result)

#code:

import random
import string

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation


password = "".join([random.choice(charValues) for i in range(pass_len)])

print("Your random password is:",password)