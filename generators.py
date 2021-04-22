# define a generator function
# take a one number as argument 
#  print the even number sequence of even number from 1 to that number.
 
def nums(n):
    for num in range(1,n+1):
        if num % 2 == 0:
            yield num
        
even_nums = nums(20)
for num in even_nums:
    print(num)
    
for num in even_nums:
    print(num)
    