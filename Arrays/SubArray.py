
#Printing SubArray


#0(n)^3 

a = [5,4,-1,7,8]



for i in range(len(a)): #Working as Starting index of Subarray
    for j in range(i,len(a)): #Ending Index of subarray.
        for k in range(i,j+1): #Priting subArray
            print(a[k],end=" ")
        print()

