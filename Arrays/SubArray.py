
#Printing SubArray


#0(n)^3 

a = [4,5,0,-2,-3,1]





for i in range(len(a)):
    for j in range(i,len(a)):
        total = 0
        for k in range(i,j+1):
            total += a[k]
        
        mod_sum = total % 5

        
print(mod_sum)


