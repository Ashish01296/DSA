"""
*********
 *******
  *****
   ***
    *

"""


n = 5 

for i in range(n,0,-1):
    # Space
    for j in range(n-i):
        print(" ",end="")

    #Number
    for k in range(i*2-1):
        print("*",end="")
    print()