# print star in such way #
#
# #
# # #
# # # #

for i in range(4):#row
     for j in range(i+1):#column
         print("#",end="")
     print()

print('\n')

# print star in such way #
# # # #
# # #
# #
#

for i in range(4):
    for j in range(4-i):
        print("#",end="")
    print()
