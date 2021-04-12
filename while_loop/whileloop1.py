# adding natural number by user input

# 5
#0
#0+1=1
#1+1=2
#2+1=3
#3+1=4
#
#
#
user= int(input("enter a number:"))
sum = 0 
i = 1
while i <= user:
    sum += i
    i += 1
print("sum of the number is :",sum)
