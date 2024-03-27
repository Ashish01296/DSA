

#Positive Cumulative Sum

a = [1 ,-1, -1, -1, 1]

sum = 0 

b = []
for i in a:
    sum+=i
    if(sum==-1 or sum==0):
        continue
    else:
        if(sum==-2):
            continue
    
    b.append(sum)

print(b)




# [1]