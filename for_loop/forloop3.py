## take user name and count the words of the name
# ex :shams tabrez
# s= 2, h= 1, a= 2 ,m=1 , t = 1 , b =1, r= 1,e=1,z=1

user = input("enter your name:")
temp_var = ""
for i in range (len(user)):
    if user[i] not in temp_var:
        temp_var += user[i] 
        print(f"{user[i]}:{user.count(user[i])}")


## EXAMPLE  OF BREAK STATEMENT
for letter in 'geeksforgeeks':#
   if letter == 'e' or letter == 's':#
        break
print("\ncurrent letter is",letter)#

## EXAMPLE OF CONTINUE STATEMENT

 #Prints all letters except 'e' and 's' 
for letter in 'geeksforgeeks':  #
    if letter == 'e' or letter == 's': #
         continue#
    print ('\nCurrent Letter :', letter) #
    var = 10#