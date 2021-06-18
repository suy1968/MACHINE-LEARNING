import numpy as np
matrix_a = np.array([[1,7,4],
                     [1,1,3],
                     [3,4,9]])
matrix_b = np.array([[1,2,1],
                     [5,9,0],
                     [1,2,1]])
print (np.add(matrix_a, matrix_b))
print (np.subtract(matrix_a,matrix_b))
print (np.dot(matrix_a, matrix_b))
print (matrix_a@matrix_b)
print (np.linalg.inv(matrix_a))
print (matrix_a@np.linalg.inv(matrix_a))
