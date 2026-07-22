"""
*
**
***
****
*****



"""

number = int(input("Enter a Number: "))

for i in range(number):
    for j in range(i+1):
        print("*",end="")
    print()