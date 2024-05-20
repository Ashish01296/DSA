a = [2,0,2,1,1,0]

left = 0
mid = 0
high = len(a) -1



while mid<=high:
    if(a[mid]==0):
        a[mid],a[left] =a[left], a[mid]
        left+=1
        mid+=1
    elif a[mid]==1:
        mid+=1
    else:
        a[mid],a[high] = a[high],a[mid]
        high-=1


print(a)      


















