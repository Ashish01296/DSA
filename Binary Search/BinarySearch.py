def BinarySearch(arr,key):
    start = 0 
    end = len(arr) - 1

    while start<=end:
        mid = (start  + (end-start) )// 2

        if arr[mid]==key:
            return mid
        elif key > arr[mid]:
            end = mid + 1
        
        else:
            start = mid -1
    
    if mid :
        return mid
    else:
        return -1





a = [1,2,3,4,5,6]

print(BinarySearch(a,30))

