## FUNCTION RETURNING FUNCTION 
# WE WILL CREATE A FUNCTION IN WHICH WE WANT TO CREATE   sub functon ND FIND OUT THE VALUE
#CUBE
# SQUARE....ETC

def power(x):
    def cal_power(n):
        return n**x
    return cal_power
cal = power(3)
print(cal(5))

cal = power(2)
print(cal(2))
