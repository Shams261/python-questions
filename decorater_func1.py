## write a decorators function in which we want to findout the time run between two code and return the output like this....
# calcalate time 
# we have to import time module


from functools import wraps
import time

def time_calculation(any_function):
    @wraps (any_function)
    def wrapper_function(*args ,**kwargs):
        print(f"you are executing ...{any_function.__name__} function ")
        t1 = time.time()
        return_value = any_function(*args , **kwargs)
        t2 = time.time()
        total_time = t2 -t1
        print(f"this function took {total_time} sec to run.")
        return return_value
    return wrapper_function    

@time_calculation
def cal_power(n):
    return [i**2 for i in range(1,n+1)]
print(cal_power(15))


