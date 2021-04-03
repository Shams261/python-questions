##Write a program to check if a year is leap year or not.

year  = eval(input("enter the year you want to check"))

if year % 4 ==0:
    print("leap year")
else:
    print("not leap year")