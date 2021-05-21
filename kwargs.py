## define a function in which we return the list and each first case of list should capital
# if reverse it ,it reverse list as same manner

def fun(l,**kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title for name in l] 
    else:
        return [name.title for name in l] 

names = ['shams','tabrez']
print(fun(names))
