# FILTER ODD EVEN FROM LIST 
# EX : [1,2,3,6,8,4,9,7,6,12,13] = [[1,3,9,7,13],[2,6,8,4,6,12]]

def even_odd(l):
    even = []
    odd = []
    for i in l:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    output = [even ,odd]
    return output

numbers = [1,2,3,6,8,4,9,7,6,12,13] 
print(even_odd(numbers))               