

def gcdCalculator(n1,n2):
    if n1==0 or n2==0:
        return "Provide a Value which is Greater then 0"
    else:
        for i in range(min(n1,n2),0,-1):
            if n1%i==0 or n2%i==0:
                return i
    return 1


print(gcdCalculator(5,10))


