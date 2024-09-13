a = [10,100,1000,10000]



current_min = float('inf')

current_max = float('-inf')


for i in range(len(a)):
    if(a[i]<current_min):
        current_min = a[i]
    


for i in range(len(a)):
    if(a[i]>current_max):
        current_max = a[i]

print("Minimum Element is: ",current_min," ","Maximum element is: ",current_max)

