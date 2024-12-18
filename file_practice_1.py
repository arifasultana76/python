#WAF that replace all occurrences of "java" with "python" in above file.

with open("practice.txt","r") as f:
    data = f.read()

new_data = data.replace("java","python")     #replace hoyni
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)