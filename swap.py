# swap two numbers without using thrird variable

a = 5
b = 6

# by using third variable we can do it like this

temp = a
a = b
b = temp
print(a)
print(b)

# without using third variable

a = a+b
b= a-b
a= a-b
print(a)
print(b)

# M-2 best approach because it use less memory .  not wasting extra memory

a = a^b
b = a^b
a = a^b
print(a)

#M -3 here it uses stack method to solve the problem

a,b = b,a
print(a)
print(b)
