## write a decorators function in which we want to add the function and return the output like this....

# you are calling addition function
#this function takes two number as parameter and return their sum
# sum is ....

from functools import wraps

def decorator_function(any_function): # yahan pr function name kuch bhi daal sakte hain and any_function ke jagan bhi kuch bhi
    @wraps (any_function)
    def wrapper_function(*args ,**kwargs):
        print(f"you are calling {any_function.__name__} function ")
        print(any_function.__doc__)
        return any_function(*args ,**kwargs)
    return wrapper_function

@ decorator_function
def additon(a , b):
    '''this function takes two number as parameter and return their sum'''
    return  a+b
print(additon(5,9))   