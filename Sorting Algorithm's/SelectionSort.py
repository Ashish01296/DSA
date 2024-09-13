def selectionSort(arr):

    for i in range(len(arr)):
        minindex = i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[minindex]):
                minindex = j
        arr[i],arr[minindex] = arr[minindex],arr[i]
    
    return arr




d = [5,4,3,2,1]

a = selectionSort(d)

print(a)