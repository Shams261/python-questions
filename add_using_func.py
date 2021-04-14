# define a function take any number of list containing number
# [1,2,3] ,[4,5,3],[9,4,8]
# return average
# (1+4+9)/3 , (2+5+4)/3 ,(3+3+8)

def average_num(l1,l2):
    average = []
    for pair in zip(l1,l2):
        average.append(sum(pair)/len(pair))
    return average
print(average_num([1,2,3],[6,8,4]))


# OR we can do this for any number of list

def average_num(*args):
    average = []
    for pair in zip(*args):
        average.append(sum(pair)/len(pair))
    return average
print(average_num([1,2,3],[6,8,8],[5,8,9]))    

##OR BY USING LIST COMOREHENSION

average_num = lambda *args :[sum(pair)/len(pair)for pair in zip(*args)]
print(average_num([1,2,3],[6,8,8],[5,8,9,]))


