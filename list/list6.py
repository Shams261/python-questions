## INSIDE THE LIST OF LIST FIND OUT HOW MANY LIST IN THE LIST
## EX: [1,2,3,[8,5,6],[6,8,9]] --> 2(OUTPUT)
## EX :[1,2,5,4,3,[9,8,7]] --> 1(OUTPUT)
def mixed_list(l):
    count = 0
    for i in l:
        if type(i) == list:
            count =count+1
    return count

numbers = [45,[698,365,36256,987],[985,25,124]]
print(mixed_list(numbers))


