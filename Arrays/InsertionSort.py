#Q.3 Implemt a Insertion Sorting...

a = [11,4,200]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i]>a[j]):
            a[i],a[j] = a[j],a[i]


print(a)

#[4, 11, 200]