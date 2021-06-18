import numpy as np
Z = np.random.random((5,5))
print(Z)
print(np.mean(Z))
print(np.std(Z))
Z = (Z - np.mean(Z)) / (np.std(Z))
print(Z)
