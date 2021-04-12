## IF WE RETURN TWO VALUE FROM FUNCTION THE VALUE IN TUPLE WILL PRINT
# ADN IF WE HAVE TO SEPERATE THE VALUE  IN DIFFERENT VARIABLE THEN WE HAVE T TAKE TWO OTHERS VARIABLE

# EX:

def func(int1 , int2):
    add= int1+int2
    multiply= int1*int2
    return add,multiply
print(func(3,5))
## and if we want to print this in seperate variable then we will take two different variable to store it

add , multiply = func(3,5)
print(add)
print(multiply)