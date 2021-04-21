# how to use enamurate function
#ex 1: find out the position of the string

names = ['zain','neha',"laare",'eav']
for pos ,name in enumerate(names):
    print(f"{pos} is ---->{name}")

# ex 2:def a function that take two argument list containing string and targeted string whose pos we want
#if present the string print the string else return -1

def string_pre(l , target):
    for pos ,name in enumerate(l):
        if name == target:
            return pos
    return -1
print(string_pre(names,'zain'))