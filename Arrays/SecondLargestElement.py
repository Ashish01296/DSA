

def LargestElemet(arr):
    if arr is None:
        return None

    largest = float('-inf')
    for i in range(len(arr)):
        if arr[i]> largest:
            largest = arr[i]
    
    return largest
             

def SecondLargest(arr):
    if len(arr) < 2:
            return
    largest = float('-inf')
    sec_largest = float('-inf')
    for i in range(len(arr)):
        if arr[i]>largest:
            sec_largest = largest
            largest = arr[i]
        elif arr[i]>sec_largest and arr[i]!=largest:
             sec_largest = arr[i]
    return sec_largest


a = [1,2,4,7,7,5]
print(LargestElemet(a))
print(SecondLargest(a))
          