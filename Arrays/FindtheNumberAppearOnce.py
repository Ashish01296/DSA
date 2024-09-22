def FindtheNumberAppear(arr):
    xoring = 0

    for num in arr:
        xoring ^= num
    return xoring


a = [4,1,2,1,2]
print(FindtheNumberAppear(a))