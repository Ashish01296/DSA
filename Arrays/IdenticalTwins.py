# Identical Twins

a = [1,1,1,1]


count_twins = 0

end = len(a)+1

for i in range(0,len(a)+1):
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            count_twins+=1;


print("Total Twins Counts are: ",count_twins)



#  Total Twins Counts are:  6