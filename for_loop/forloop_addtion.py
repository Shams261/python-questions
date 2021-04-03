## ask user for input add all the number in a systamatic way 
# ex 1234 add= 1+2+3+4=10

user = input("enter a number:")
sum = 0
for i in range(0,len(user)):
    sum += int(user[i])
print(sum,"is the total sum.")
