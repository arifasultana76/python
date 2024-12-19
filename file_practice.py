# create a new file "Practice.txt" using python. Add the following data in it.

# with open("practice.txt","w") as f:
#     f.write("Hlw everyone\nwe are learning File I/O\n")
#     f.write("using Java.\ni like programming in Java.")

#WAF that replace all occurrences of "java" with "python" in above file.

with open("practice.txt","r") as f:
    data = f.read()

new_data = data.replace("java","python")     
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)


# Search if the word "learning" exists in the file or not.

word = "learning"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("not found")

#another(function way):

def check_for_word():
    word = "learning"
    with open("practice.txt","r") as f:     
        data = f.read()
        print(data.find(word))
        if(data.find(word) != -1):   #khuje na pele -1 print korbe, pele first index or occurence return korbe
            print("Found")
        else:
            print("not found")

check_for_word()


#WAF to find in which line of the file does the word "learning" occur first.
#print -1 if word not found.

#code:

def check_for_word():
    word = "learning"
    with open("practice.txt","r") as f:    
        data = f.read()
        if(word in data):
            print("Found")
        else:
            print("not found")

def check_for_line(): 
    word ="learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)     # exist korle return # exist na korle -1 return
                return
            line_no += 1
    return -1 
check_for_line()

# programming word search korte chaile ae code hobe:
#code:

def check_for_line(): 
    word ="programming"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)   
                return
            line_no += 1
    return -1 
check_for_line()

