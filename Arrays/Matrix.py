# Define the matrices
a = [[1, 2],
     [3, 4]]

b = [[4, 3],
     [2, 1],
     ]

# Initialize the result matrix with zeros
result = [[0, 0],
          [0, 0]]

# Perform matrix multiplication
for i in range(len(a)):  # Iterate over the rows of the first matrix   # 2 (0,1)
    for j in range(0,len(b[0])):  # Iterate over the columns of the second matrix  # 4,3 2
        for k in range(len(b)):  # Iterate over the rows of the second matrix  2.. (0,1)
            result[i][j] += a[i][k]  *  b[k][j]

# Print the result
for row in result:
    print(row)


print(result[1][0])

