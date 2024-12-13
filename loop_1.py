
Loops: loops are used to repeat instructions.
loops 2 type: *while loops *for loops

While loops: 

while condition: #some work

count = 1
while count <= 5 :
   print("Hello")        ## Hello print hote thakbe
   count <= 1
print(count)

count = 1
while count <= 5 :
   print("Hello")        
   count += 1

i = 1
while i<= 5:
   print("Yes i'm strong, I can.", i)   ## 5 time print hobe
   i+=1

i = 1
while i <= 100000:
   print("yes,I'm Strong!")
   i+=1

i = 1
while i <= 100000:
   print("yes,I'm Strong!", i)
   i+=1


i = 1
while i <= 5:                    ## 5 time will be print
   print("yes,I'm Strong!", i)
   i+=1


i = 1
while i <= 5:              
   print("yes,I'm Strong!", i)   
   i +=1
print(i)


i = 5
while i <= 6:                   ## print number from 5 & 6     
   print("yes,I'm Strong!", i)
   i +=1
print(i)


i = 5
while i <= 6:      ## infinate print 

  print(i)
  i -= 1


i = 5
while i <= 6:       

  print(i)
  i += 1

#Practice:
# Print numbers from 1 to 100.

i = 1
while i <= 100:         ## ans will be 100
   print(i)
   i += 1

i = 1
while i <= 100:      ## ans will be 101  
   i += 1            ## i can't understand this
   print(i)


#print numbers from 100 to 1.

i = 100
while i >= 1:   ##stopping condition
   print(i)
   i -= 1

#print the multiplication table of a number n.

i = 1
while i <= 10:    
   print(3*i)
   i += 1

another example:

n = int(input("enter num:"))   ## je digit dibo sei digit er multiple tabel er ans ashbe
i = 1
while i <= 10:    
   print(n*i)
   i += 1
   
practice:

Print the elements of the following list using a loop.
[1,4,9,16,25,36,49,64.81,100]

nums = [1,4,9,16,25,36,49,64,81,100]

idx = 0                    ## idx er bodole jekono varible nileo hobe
while idx < len(nums):     ##traverse bole bar bar check kore tai
   print(nums[idx])  
   idx += 1


Search for a number x in this tuple using loop.

nums = (1,4,9,16,25,36,49,64,81,100)

i = 0                   
while i < len(nums):     
   print(nums[i])  
   i += 1

another method:

nums = (1,4,9,16,25,36,49,64,81,100)
x = 36
i = 0                   
while i < len(nums):
   if(nums[i] == x):
      print("FOUND at idx", i)
   i += 1

another method:

nums = (1,4,9,16,25,36,49,64,81,100,36)
x = 36
i = 0                   
while i < len(nums):
   if(nums[i] == x):
      print("FOUND at idx", i)

   else:
      print("finding..")
   i += 1


Break & continue: (this are keys)

Break: used to terminate the loop when encountered.
Continue: Terminates execution in the current iteration & continues execution 
of the loop with the next iteration.

i = 1
while 1 <= 5:
   print(i)
   if(i==3):
      break
   i += 1
print("end of loop")


nums = (1,4,9,16,25,36,49,64,81,100,36)
x = 36
i = 0                   
while i < len(nums):
   if(nums[i] == x):
      print("FOUND at idx", i)
      break                    ## break porjontoi work korbe
   else:
      print("finding..")
   i += 1

print("end of loop")


another:

i = 0
while i<= 5:
   if(i == 3):     ## jodi ami continue e dei tahole kno if condition use korbo!!
      i +=1
      continue
   print(i)
   i +=1

another:

i = 0
while i<= 5:
   if(i%2 == 0):   #ODD Num er jonno
      i += 1    
      continue     #skip
   print(i)
i +=1


i = 0
while i<= 10:
   if(i%2 != 0):   #EVEN num er jonno
      i += 1    
      continue     
   print(i)
   i +=1








 






