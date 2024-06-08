

#find out correct pivot position



#pivot as first position
def pivot_place(arr,first,last):
    pivot = arr[first]
    left = first + 1
    right = last


    while True:

        while left<=right and arr[left]<=pivot:
            left+=1
        
        while left<=right and arr[right]>= pivot:
            right-=1

        
        if right < left :
            break
        else:
            arr[left],arr[right] = arr[right],arr[left]
    
    arr[first],arr[right] = arr[right],arr[first]
    return right


def Quicksort(arr,first,last):

    if first<last:

        p = pivot_place(arr,first,last)
        Quicksort(arr,first,p-1)
        Quicksort(arr,p+1,last)
    


    


                  
a = [5,4,3,2,1]
length = len(a) - 1
Quicksort(a,0,length)
print(a)



