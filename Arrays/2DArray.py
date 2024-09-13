# Matrix Multiply

a  =[[50,60],[3,4]]
b = [[10,20],[30,40]]

# result = [[0 for j in range(2)]]*2

# print(result)

'''
[[2300 3400] 
 [ 150  220]]
'''


import numpy as np

matrix1 = [[1, 2, 3],[4,5,6]]

matrix2 = [[10,20,30],[40,50,60]]


for row in range(len(matrix1)):
    for column in range(len(matrix1[0])):
        print(matrix1[row][column],end=" ")
    print()


# Matrix Addition
result = [[matrix1[i][j]+ matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

print(result)



#Matrix Multiplication

'''
[[ 920 1480]
 [  75  120]]
'''



#sum of all elements


total = 0 

for row in range(len(a)):
    for column in range(len(a[row])):
        total  += a[row][column]



# Finding Maximum Element in 2D


d = float('-inf')


for row in range(len(a)):
    for col in range(len(a[row])):
        if a[row][col] > d:
            d = a[row][col]

print(d)


#Finding Minimum Element in 2D


m = float('inf')

for row in range(len(a)):
    for col in range(len(a[row])):
        if(a[row][col]<m):
            m = a[row][col]


# Matrix Multiplication


m = 4
p = 6



# def matrix_multiplication(A,B):
#     m = len(A)
#     n = len(A[0])
#     p = len(B[0])
#     result = [[0 for row in range(p)] for col in range(m)] 
#     print(result)   

#     # Matrix Multiplication
#     for row in range(m):
#         for col in range(p):
#             for res in range(p):
#                 result[row][col] += A[row][res] * B[res][col]

#     return result

# a =[[50,60],[4,5]]
# b =[[10,20],[7,8]]

# print(matrix_multiplication(a,b))




def matrix_multiplication(A,B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    res = [[0 for _ in range(p)] for _ in range(m)]
    print(res)

    for row in range(m):
        for col in range(p):
            for res_row in range(n):
                res[row][col] += A[row][res_row] * B[res_row][col]
    print(res)
                


a =[[50,60],[4,5]]
b =[[10,20],[7,8]]


matrix_multiplication(a,b)