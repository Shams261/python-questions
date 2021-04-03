##Take values of length and breadth of a rectangle from user and check if it is square or not.

def rectangle(l,b): 

    if l == b:
        print("it is square") 
    else:
        print("not square")
    return 


l = int(input("enter the length:"))
b = int(input("enter the bredth:"))
print(rectangle(l,b))