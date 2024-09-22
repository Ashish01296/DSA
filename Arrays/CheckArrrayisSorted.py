a = [1,2,3,4,5]


def isSorted(arr, n):
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            return False
    return True



print(isSorted(a,len(a)))