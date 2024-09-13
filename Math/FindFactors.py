
# Find Factor of Number or Print all Divisors..

# def FindFactors(n):
#     d = []
#     for i in range(1,n+1):
#         if n%i==0:
#             d.append(i)
#     return d



# print(FindFactors(12))


def FindFactors(n):
    import math
    factors = []
    sqrt = int(math.sqrt(n))
    for i in range(1,sqrt+1):
        if n%i==0:
            factors.append(i)
        
        # To avoid Duplication or check if it different value or not
        if i != n//i:
            factors.append(n//i)
    return factors






print(FindFactors(12))

