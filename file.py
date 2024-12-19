# File I/O: python can be used to perform operations on a file.(read & write data)

# Types of all files:

# 1. Text files: .txt, .docx, .log etc.
# 2. Binary files: .mp4, .mov, .png, .jpeg etc.

#Text file: characteristic 
#Binary file: memory(bit wise)

# f = open ("file_name","mode")  #mode 2 rokom. read mode,write mode.

# Reading a file:

#Code:

f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

#code:

f = open("demo.txt", "r")

data = f.read(5)      #reads entire file
print(data)
print(type(data))

f.close()

#code: 

f = open("demo.txt", "r")
line1 = f.readline()       #reads one line at a time
print(line1)

line2 = f.readline()       
print(line2)

f.close()

#code:

f = open("demo.txt", "r")

data = f.read()
print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()     
print(line2)

f.close()

#code:

f = open("demo.txt", "r")

data = f.read()
print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()     
print(line2)

line3 = f.readline()     
print(line3)

f.close()

# #Writing to a file:

f = open("demo.txt","w")
f.write("this is a new line")   #overwrites the entire file

f = open("demo.txt", "a")
f.write("this is a new line")    #adds to the file

#code:

f = open("demo.txt","a")

f.write("I want to learn JavaScript tomorrow.123")

f.close()

#code:

f = open("demo.txt","a")

f.write("\n after that html.")

f.close()

f = open("demo.txt","r")

#code:

f = open("sample.txt", "a")      #sample file open hoye jabe.
f.close()

#stackoverflow name er website ache for more info

f = open("demo.txt", "w+")

print(f.read())
f.write("abc")
f.close()

f = open("demo.txt", "a+")

print(f.read())
f.write("abc")
f.close()

#code:

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

with open("demo.txt", "r") as f:       #execute korbe na here's no function call.
    f.write("new data")
  


