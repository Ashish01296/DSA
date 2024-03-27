#Important question as per FAANG, MAANG Company or Product Based Company...

#Q.1.  Merge Two Sorted Arrays..


a = [1 ,3 ,3 ,3 ,3, 4]
b = [9,11]

def mergearray(a,b):
    i = 0
    j = 0
    c= []
    len_a = len(a)
    len_b = len(b)
    while(i<len_a and j<len_b):
        if(a[i]<b[j]):
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    while(i<len_a):
        c.append(a[i])
        i+=1
        
    while(j<len_b):
        c.append(b[j])
        j+=1
    
    return c
            




print(mergearray(a,b))


#[1, 3, 3, 3, 3, 4, 9, 11]



#Approache 2:

"""
m = len(a)
n = len(b)

a[0:m+n] = sorted(a[:m]+b[:n])

print(a)

"""