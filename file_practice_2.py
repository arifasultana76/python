#From a file containing numbers separately by comma,
# print the count of even numbers.

# with open("practice.txt","r") as f:
#     data = f.read()
#     print(data)

#individual number :

# num = ""
# for i in range(len(data)):
#     if(data[i] == ","):
#         print(num)
#         num = ""
#     else:
#         num += data[i]

#casting:

count = 0
with open("practice.txt","r") as f:
    data = f.read()
    
nums = data.split(",")             # can't understand
for val in nums:
  if(int(val)% 2 == 0):
        count += 1

print(count)