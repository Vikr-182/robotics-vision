import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

b = np.array([[9, 8, 7], [6, 5, 4]])

c = np.concatenate((a, b))

print(c)
