# Cummulative Sum

#The cumulative sum of an array at index i is defined as the sum of all elements of the array from index 0 to index i.

a = [1,2,3,4]

end = len(a)

sum = 0

b = []

for i in a:
    sum+=i
    b.append(sum)


print(b)
    
# o/p:   [1,3,6,10]