import numpy as np
matrix = np.array([[1,2,3],
                   [1,5,4],
                   [4,5,6]])
print (matrix.diagonal())
print (matrix.diagonal(offset = 1))
print (matrix.diagonal(offset = -2))
print (matrix.trace())
