#print patern like this
#****
#****
#****
#****

i = 1
while i <=4:
    print('*',end="")
    j = 1
    while j <=4:
        print('*',end="" )
        j +=1
    i+=1
    print()

#METHOD 2

for i in range(4):
    for j in range(4):
        print("#",end="")
    print()
