# FIBONACCI SERIES 
# 0, 1.1,2,3,5,8,13,21,34,55,89,144
# 0=0
#0+1=1
#1+1=2
#1+2=3
#2+3=5.....SO ON

# always a=0  and b=1

def fibonacci_series(n):
    a = 0
    b =1
    if n==1:
        print (a)
    elif n==2:
        print (a,b)
    else:
        print(a, b ,end =" ")
        for i in range(n-2):
            c = a+b
            a = b
            b = c
            print(b, end =" \n")
num = int(input("enter the number:"))
n = num            
fibonacci_series(n)


