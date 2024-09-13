def CheckPrimeNumber(Number):
    count = 0
    for i in range(1,Number+1):
        if Number%i==0:
            count+=1
    
    if count==2:
        return True
    else:
        return False
    



print(CheckPrimeNumber(10))



# T.C:  O(N)
#S.C: O(1)