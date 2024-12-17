# create a new file "Practice.txt" using python. Add the following data in it.

# with open("practice.txt","w") as f:
#     f.write("Hlw everyone\nwe are learning File I/O\n")
#     f.write("using Java.\ni like programming in Java.")

#WAF that replace all occurrences of "java" with "python" in above file.

# with open("practice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("java","python")     #replace hoyni kno!
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)


#Search if the word "learning" exists in the file or not.

word = "learning"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("not found")