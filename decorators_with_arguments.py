# jo data type pass krenge mein argument mein wahi print hoga
# ex:agar str diye to wahi print hoga warna error aayea

from functools import wraps
def only_data_types(data_type):
    def decorators(function):
        @wraps(function)
        def wrapper_function(*args , **kwargs):
            if all ((type(arg)==data_type for arg in args)):
                return function(*args , **kwargs)
            print("invalid arguments")
        return wrapper_function
    return decorators

@ only_data_types(str)
def string_join(*args):
    string = ''
    for i in args:
        string += i
    return string
print(string_join('shams','tabrez'))        

##3 it shows error 

print(string_join('shams','tabrez',52))    
