# COMMON FIND VALUE METHOD 
# TAKING TWO LIST AND FIND OUT THE COMMMON BETWEEN THEM 
# [2,5,8,6,3,5,8] AND [4,2,1,5,8,6,9,6] = [2,6,8]

def common_list(l1,l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output

print(common_list([1,2,4,5,7,8,9],[1,5,7,8,10,32,2]))            


