
def CheckAmrStrongNumber(N):
    sum = 0
    for i in str(N):
        d = int(i)**3
        sum+=d
    
    if sum==N:
        return True
    else:
        return False
    

n = 153
print(CheckAmrStrongNumber(n))
