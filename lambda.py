## USE OF LAMBDA FUNCTION

add = lambda a,b : a+b
print(add(5,4))

# print reversre charater with lambda
#
reverse_char = lambda a:a[::-1] 
print(reverse_char("shams"))

# print last chahrecter of letter
last_char = lambda a : a[-1] 
print(last_char("shoaib"))

#lambda with if else 

count_char = lambda s: True if len(s) > 5 else False
print(count_char("sdfjks"))

## print even or odd
# 
even_odd = lambda a : a % 2 ==0
num = int(input("enter a number :"))
print(even_odd(num)) 