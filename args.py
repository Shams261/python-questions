#IN THIS  EXAMPLE WE DEFIINE A FUNCTION AND ITS OUTPUT WILL BE THE CUBE OF THAT NUMBER 
# EX: NUMS = [3,4,,5] ------> TOPOWER(3,*NUMS)
# OUTPUT = (9,16,25)
# IF USER DIDI NOT PASS ANY ARGUMENT THEN IT SAY IT DIID NOT PASS ANY THING
# 

# 
# HOW TO CHECK THE LIAT IS EMPTY OR NOT
my = [2,5,8,9,6]
if my:
    print("not empty")
else:
    print("empty")


## main code

def power_of(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return "you did not type any args"
num = [6,9,8]
print(power_of(3,*num))
