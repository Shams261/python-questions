#METHODS OF LIST

numbers = [5,9,8,7,4]
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)

##LOOPING INSIDE LIST

matrix= [[1,5,3],[6,5,8],[3,7,9]]  #2d list
for sublist in matrix:
    for i in sublist:
        print(i)


print(matrix[2][2])