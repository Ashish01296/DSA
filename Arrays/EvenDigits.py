#Even number of Digits..

a = ["42", "564", "5775", "34", "123", "454", "1", "5", "45", "3556", "23442"]

b = []
for i in range(len(a)):
    if(len(a[i])==2 or len(a[i])==4):
        b.append(int(a[i]))

print(b)

# [42, 5775, 34, 45, 3556]