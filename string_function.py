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
