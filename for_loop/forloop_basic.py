# syntax for i in range():
             #statements
             # means var in iterables
             #10:   +1+2+3+4+5+6+7+8+9

user = int(input("enter a number:"))
sum = 0
for i in range(1,user+1):
    sum += i
print("sum of the nummber:",sum)