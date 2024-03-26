#Q.4... merge two sorted subarray..

a = [3, 3, 9 ,11 ,1 ,3 ,3 ,4]


length = len(a)

arr1_size =int(input("Enter size"))
final_length = arr1_size+1

arr1 = []

arr2 =  []
for i in range(final_length):
    arr1.append(a[i])
for j in range(final_length,length):
    arr2.append(a[j])


print(arr1)
print(arr2)



"""
Enter size 5
[3, 3, 9, 11, 1, 3]
[3, 4]
"""