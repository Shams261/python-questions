# DEFINE A LIST PASS A NUMBER RERTURN THE SQUARE OF NUMBER
# EX: [1,2,3,4]
#  OUTPUT = [1,4,9,16]
# list kabhi bhi function ke parameter mein pass nahi karenge kyunkim wo ek keyword hai,str bhi nahi


def square_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square
numbers = list(range(1,221))
print(square_list(numbers))

#NOTE : YE PROGRAM RUN KRNE KE LIYE HUM NE EK FUNCTION SQUARE LIST LIYA USKE BAAD EK EMPTY LIST LIYA
# US EMPTY LIST MEIN HUM KO APPEND KRNA HAI SQURE US NUMBER KA TO HUM EK LOOP LENGE US LOOP KO RUN KRNE KE LIYE
#   US LOOP KO SPPEND KRNEGE EMPTY LIST KE SAATH  US KE BAAD HUM RETURN KRLENGE US EMPTY LIST KO KYUNKI HUMNE SQUARE
# LIST MEIN HI APPEND KIYA HAI USKE BAAD EK NUMBERES VARIABLE LENGE USMEIN RANGE DENGE JITNA KA 
# SQUARE CHAHIYE USKE BAAD APNE FUNCTION KO CALL KRLENGE VARIABLE KE SAATH . 