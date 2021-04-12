## ask user for input add all the number in a systamatic way 
# ex 1234 add= 1+2+3+4=10

user = input("enter the number:")
sum = 0
i = 0
while i < len(user):
    sum += int(user[i])
    i += 1
print("sum of number is :",sum)    
    
