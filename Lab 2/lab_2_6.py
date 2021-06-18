import numpy as np
Z = np.diag(1+np.arange(4),k=-1)
print(Z)
Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)
print(np.unravel_index(99,(6,7,8)))
Z = np.tile(np.array([[0,1],[1,0]]), (4,4))
print(Z)
