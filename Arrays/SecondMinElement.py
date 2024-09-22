

def MinElem(arr):
    if arr is None:
        return -1
    mini = float('inf')
    for i in range(len(arr)):
        if arr[i] < mini:
            mini = arr[i]
    return mini
        
def SecondMinEle(arr):
    if len(arr) < 2:
        return

    min_ele = float('inf')
    second_min = float('inf')
    for i in range(len(arr)):
        if arr[i] < min_ele :
            second_min = min_ele
            min_ele = arr[i]
        elif arr[i] <  second_min and arr[i] != min_ele:
            second_min = arr[i]
    
    return second_min


a = [1,2,4,7,7,5]
print(MinElem(a))
print(SecondMinEle(a))

