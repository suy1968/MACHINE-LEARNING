import numpy as np
from scipy import sparse
matrix = np.array([[0,0],[1,0],[3,0]])
matrix_sparse = sparse.csr_matrix(matrix)
print (matrix)
print (matrix_sparse)
