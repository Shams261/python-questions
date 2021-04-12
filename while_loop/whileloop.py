# example1

count = 0
while (count < 3):
    count = count+1
    print("shams")


    # example2

    a = [1, 2, 3, 4] 
while a: 
    print(a.pop()) 

## SINGLE STATEMENT WHILE LOOP

#count = 0
#while (count < 4) : print("hello geek")  ##this loop never end means it goes infinte time and we have to  forcefully terminate the compiler

## CONTINUE STATEMENT 

i = 0
a ='Shams tabrez'
while i < len(a):
    if a[i] == 'h' or a[i] == 'r':
        i += 1
        continue
    print("current letter:",a[i])
    i += 1

##  BREAK STATEMENT

i = 0
a ='Shams tabrez'
while i < len(a):
    if a[i] == 'h' or a[i] == 'r':
        i += 1
        break
    print("\ncurrent letter:",a[i])
    i += 1    

## PASS STATEMENT

i = 0
a ='Shams tabrez'
while i < len(a):
    #if a[i] == 'h' or a[i] == 'r':
        i += 1
        pass
print("\nvalue of i :",i)
    #i += 1   

## WHILE -ELSE LOOP 

i = 0
while i < 4:
    i += 1
    print(i)
else:
    print("No break\n")
    i = 0
    while i < 4:
        i +=1
        print(i)
        break
    else:
        print("No break")

    
