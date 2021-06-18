import numpy as np
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
add_1000 = lambda i: i + 1000
vectorized_add_1000 = np.vectorize(add_1000)
print(vectorized_add_1000(matrix))
print(np.max(matrix, axis = 0))
print(np.min(matrix, axis = 1))

