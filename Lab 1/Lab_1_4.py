import numpy as np
from scipy import sparse
matrix_large = np.array([[0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,1,0,0,1,0,0,0],
                         [3,0,2,4,0,0,0,0,0,0]])
matrix_large_sparse = sparse.csc_matrix(matrix_large)
print (matrix_large)
print (matrix_large_sparse)
