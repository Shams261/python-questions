# DEFINE A LIST IN WHICH WE ARE DOING THE REVERSE OF THAT LIST 
# EX : [1,2,34,5,6,7] = [7,6,5,34,2,1] OR [WORD1,WORD3] = [WORD3,WORD1]

def reverse_list(l):
    empty_l = []
    for i in range(len (l)):
        popped_items=l.pop()
        empty_l.append(popped_items)
    return empty_l

numbers = [6,9,8,7,4,3,2,1]
print(reverse_list(numbers))    


#OR METHOD 2

def reverse_list(l):
    l.reverse()
    return l

numbers = [4,3,8,6,9]
print(reverse_list(numbers))


# OR METHOD 3
def reverse_list(l):
    return l[::-1]

numbers = [4,3,8,6,9]
print(reverse_list(numbers))
