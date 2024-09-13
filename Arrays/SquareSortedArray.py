#  Square Sorted Array..


a = [ 6, -8, 3 ,-1 ,4]

length_a = int(len(a))

b= []

for i in range(length_a):
    b.append(a[i]**2)
    b.sort()

print(b)


#  [1, 9, 16, 36, 64]