#DEFINE FUNCTION A DICT IN WHICH WE HAVE TO FINDOUT THE CUBE OF NUMBER 

def cube_find(n):
    dict={}
    for i in range (1,n+1):
        dict[i] = i**3
    return dict

num = int(input("enter a number:"))
print(cube_find(num))
