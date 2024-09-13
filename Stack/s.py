# import itertools



# def subsets_of_size(arr, size):
#     subsets = list(itertools.combinations(arr, size))
#     sums = [sum(combo) for combo in subsets]  # Sum each combination
#     return sums



# print(subsets_of_size([1,2,3],50))










# for i in range(4):
#     if(i%2==0):
#         print("python")


n = 2446
count = 0
for digit in str(n):
    if digit != '0': 
        if n % int(digit) == 0:
            count += 1


print(count)