## take user name and count the words of the name

user = input("enter your name:")
temp_var = ""
i = 0
while i < len(user):
    if user[i] not in temp_var:
        temp_var += user[i] 
        print(f"{user[i]}:{user.count(user[i])}")

    i += 1
