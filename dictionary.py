##Dictionary: Dictionary are uused to store data values in key:value pairs.
            # they are unordered,muteable(changeable)& don't allow duplicate keys.

dict = {
    "name":"Arifa",
    "CGPA": 9.6,             ## {} braket porjonto puro ta dictionary
    "marks":[98, 97, 95]
}

dict = {
    "name":"Arifa",
    "CGPA": 9.6,            
    "marks":[98, 97, 95]
}

print(dict)


info = {
    "name": "Arifa",
    "address": "Dhaka",
    "Mobile": "01810000000"
}

print(info)


info = {
    "name": "Arifa",              ## dictionary te all type data neya jay.
    "address": "Dhaka",
    "Mobile": "01810000000",
    "learner": "coding",
    "age": 23,
    "is adult": True,
    "marks": 94.4
}

print(info)

info = {
    "name": "Arifa",
    "subject": ["python","c","java"],     ##Dictionary te strings,list,tuples use kora jay
    "Topics": ("dict", "set"),            ##Here's name,subject,topics,learner etc ke key bole.
    "learner": "coding",                  ##key word same howa jabe na.
    "age": 23,                            ##this code called information dictionary.
    "is adult": True,
    "marks": 94.4
}

print(info)

info = {
    "name": "Arifa",
    "subject": ["python","c","java"],     
    "Topics": ("dict", "set"),            
    "learner": "coding",                  
    "age": 23,                            
    "is adult": True,
    "marks": 94.4
}

print(info["name"])
print(info["subject"])
print(info["learner"])
print(info["age"])
print(info["is adult"])
print(info["marks"])

null_dict ={}                   ##Null_Dictionary te single value add kora jay.
null_dict["name"]= "Arifa"
print(null_dict)


## Nested_Dictionary: Ekti dictionary er moddhe arekta dictionary thakle seta nested_dictionary.

student = {

    "name": "Arifa",
    "sub":  {
        "phy": 97,
        "chem": 95,
        "math": 98
    }

}

print(student)

#OR

student = {

    "name": "Arifa",
    "subjects":  {
        "phy": 97,
        "chem": 95,
        "math": 98
    }

}

print(student["subjects"])    ##All subject will be come

student = {

    "name": "Arifa",
    "subjects":  {
        "phy": 97,
        "chem": 95,
        "math": 98
    }

}

print(student["subjects"]["chem"])       ##Wehn i want to single subject

## Dictionary Method:

## myDict.keys():

student = {

    "name": "Arifa",
    "subjects":  {
        "phy": 97,
        "chem": 95,
        "math": 98
    }

}

# print(student.keys())


student = {

    "name": "Arifa",
    "subjects":  {
        "phy": 97,
        "chem": 95,
        "math": 98
    }

}

# print(list(student.keys()))

student = {

    "name": "Arifa",
    "subjects":  {
        "phy": 97,
        "chem": 95,
        "math": 98
    }

}

print(len(student))
print(list(student.keys()))

student = {

    "name": "Arifa",             ## ans will be 2
    "subjects":  {
        "phy": 97,
        "chem": 95,
        "math": 98
    }

}

print(len(list(student.keys())))

student = {

    "name": "Arifa",             
    "subjects":  {
        "phy": 97,
        "chem": 95,
        "math": 98
    }

}


## myDict.values():

print((student.values()))

student = {

    "name": "Arifa",             
    "subjects":  {
        "phy": 97,
        "chem": 95,
        "math": 98
    }

}

print(list(student.values()))


##myDict.items():

student = {

    "name": "Arifa",             
    "subjects":  {
        "phy": 97,
        "chem": 95,
        "math": 98
    }

}

# print(student.items())

student = {

    "name": "Arifa",             
    "subjects":  {
        "phy": 97,
        "chem": 95,
        "math": 98
    }

}

print(list(student.items()))

student = {

    "name": "Arifa Sultana",             
    "subjects":  {
        "phy": 97,
        "chem": 95,
        "math": 98
    }

}
pairs = (list(student.items()))
print(pairs[0])

student = {

    "name": "Arifa Sultana",             
    "subjects":  {
        "phy": 97,
        "chem": 95,
        "math": 98
    }

}
pairs = (list(student.items()))
print(pairs[1])


##myDict.get("key"):

student = {

    "name": "Arifa Sultana",             
    "subjects":  {
        "phy": 97,
        "chem": 95,
        "math": 98
    }

}

print(student["name"])
print(student.get("name"))

##myDict.update(newDict):

student = {

    "name": "Arifa Sultana",             
    "subjects":  {
        "phy": 97,
        "chem": 95,
        "math": 98
    }

}
student.update({"city": "dhaka"})
print(student)


student = {

    "name": "Arifa Sultana",             
    "subjects":  {
        "phy": 97,
        "chem": 95,
        "math": 98
    }

}
new_dict =({"city": "dhaka", "age": 23})
student.update(new_dict)
print(student)

student = {

    "name": "Arifa Sultana",             
    "subjects":  {
        "phy": 97,
        "chem": 95,
        "math": 98
    }

}
new_dict =({"name": "Rimi", "age": 23})
student.update(new_dict)
print(student)












