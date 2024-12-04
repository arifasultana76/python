##Strings length:

str1 = "Arifa Sultana."
str2 = "This girl is unique"
len1 = len(str1)
len2 = len(str2)
print(len1)
print(len2)

final_str = str1+" "+str2
print(final_str)
print(len(final_str))

##Strings indexing:

str = "Arifa Sultana"
ch = str[0]
print(ch)

str = "Arifa Sultana"
ch = str[6]
print(ch)

str = "Arifa Sultana"
print(str[6])

##Slicing (Accessing part of a string):

str = "Arifa Sultana"
str = str[:13]
print(str)

str ="Arifa Sultana"
ch = str[0:13]
print(str)

str ="Arifa Sultana"      ## Here's string A means 0, starting letter count 0 and also ending letter count 0 ##
ch = str[:0]
print(str)

str = "Arifa"
ch = str [ :len(str)]        ## Here's [ :len(str)] dedicated to ending letter or last index ##
print(ch)

str ="Arifa Sultana"
ch = str[0:13]
print(ch)

str ="Arifa Sultana"         ## This program is not run ##
ch = str[:0]
print(ch)

str = "Arifa Sultana"          ## This program is not run ##
str = str[:0]
print(str)


str ="Arifa Sultana"
ch = str[0:]
print(ch)

str = "Arifa Sultana"
print(str[1:4])

str = "Arifa Sultana"
print(str[:13])         ## Here's starting and ending index not missing! ##
print(str[0:])          ## Another way: print(str[0:len(str)])

# Negative index:

str = "Apple"
print(str[-4:-1])

str = "Apple"
print(str[-4:-1])

## negative index right side theke count hoy like -1,-2,-3 ....  
## But last digit will be not count like -1                                                     






