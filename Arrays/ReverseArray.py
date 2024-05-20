a = [10,100,1000,10000]
 



start = 0
end = len(a)-1

while(start<=end):
    a[start],a[end] =a[end],a[start]
    start+=1
    end-=1









