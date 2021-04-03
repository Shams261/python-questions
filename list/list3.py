# DEF A LIST IN WHICH RETURN A ARGUMENT IN WHICH TOTAL LIST REVERSE ITSELF
# EX: ['abd','mnj','tyg'] = ['dba','jnm','gyt']

def reverse_list(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements
numbers = ['abs','mnk','nty']
print(reverse_list(numbers))        


##BY USING LIST COMPREHENSION


def reverse_string(l):
    return [name [::-1] for name in l]
print(reverse_string(['abs','mnk','nty']))