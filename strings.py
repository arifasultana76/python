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
ch = str [ :len(str)]        ## Here's [ :len(str)] dedicated to ending letter or last index 
print(ch)

str ="Arifa Sultana"
ch = str[0:13]
print(ch)

str ="Arifa Sultana"         ## This program is not run ##
ch = str[:0]                 ## Cause end position a "0" not work
print(ch)

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


## String Function ##

## String.endswith("") Function:

str = "I'm a coder"
print(str.endswith("er"))     ## Ans will be True

str = "I'm a coder"
print(str.endswith("cod"))    ## Ans will be False

## string.capitalize() Function:

str = "i am studying python from youtube"
str = str.capitalize()
print(str)

str = "i am studying python from Youtube"
print(str.capitalize())


## String.replace(old,new) Function:

str = "I am studying python from youtube"
print(str.replace("python","Java"))

str = "I am studying python from youtube"
print(str.replace("o","a"))

# ## String Find (word) Function:

str = "I am studying python from youtube"
print(str.find("o"))

str = "I am studying python from youtube"
print(str.find("python"))                   ## str count will be "0" so ans will be 14 

str = "I am studying python from youtube"
print(str.find("W"))                         ## Ans will be -1 cause "W" not in str


# ## String.count("am") Function:

str = "I am from studying python from youtube"
print(str.count("from"))                          ## Here's from have 2 places so ans will be 2


str = "I am from studying python from youtube"
print(str.count("o"))                              ## Here;s letter "o" exist 4 places so ans will be 4


#Practice:

## WAP to input user's first name & print its length.

name = input("enter user name:")
print("length of your name is:", len(name))

##WAP to find the occurance of '$' in a string.

str = "Oneday i will earn $ and $ more $. $ symbol $20,0000"
print(str.count("$"))









