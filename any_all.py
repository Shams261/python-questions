## by any_all function we check the list is int or float 
# if condition is satisfy the print the avg otherwise print error

def avg(*args):
    if all([(type(arg)==int or type(arg)== float) for arg in args]):
        for num in args:
            total += num
        return total
    else:
        return "wrong input"

print(avg(1,5,3,6,'shams'))
