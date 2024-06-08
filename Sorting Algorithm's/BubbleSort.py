
def bubblesort(my_array):
    n = len(my_array)
    for i in range(n-1):
        for j in range(n-i-1):
            if my_array[j] > my_array[j+1]:
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
    
    return my_array



a = [50,25,35,45,2]

sorted_array = bubblesort(a)

print(sorted_array)