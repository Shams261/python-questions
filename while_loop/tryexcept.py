## def a function in which we perform divide operation
#divide(a,b)
# if any ine divide the number by 0 then print the error message

def divide(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError : 
        print("number cannot divide by zero")
    except TypeError :
        print("value should be in int or in float")

num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
print(divide(num1,num2))
