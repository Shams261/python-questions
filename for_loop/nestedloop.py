#NESTED LOOP : ANY LOOP CAN BE PUT INSIDE ANOTHER LOOP


from __future__ import print_function 
for i in range(1,11):
    for j in range(i):
        print(i,end = '')
    print()    
