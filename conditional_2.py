while True:
    marks = int(input(" marks: "))
    
    if (marks >= 90):
        print("A")
    elif (marks >= 80 and marks <90 ):
        print ("B")
    elif (marks >=70 and marks <80 ):
        print("c")
    elif (marks >=60 and marks <70 ):
        print("D")
    elif (marks >=50 and marks <60 ):
        print ("E")
    else: 
        print ("F")
