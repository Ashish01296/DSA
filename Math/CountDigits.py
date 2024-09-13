#Count Digits



#Brute Force Approach

def CountDigits(N):
    count = 0
    for digit in str(N):
        if digit != '0':  # For Skipping zero
            if N % int(digit) == 0:
                count+=1
    return count




print(CountDigits(122))


# Optimal Approach


import math
n = 12
cnt = math.log10(n) + 1
print(int(cnt))