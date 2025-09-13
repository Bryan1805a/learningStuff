import numpy as np

array_1 = np.arange(1, 10).reshape((3, 3))
array_2 = np.arange(11, 20).reshape((3, 3))


print(np.stack((array_1, array_2), axis=1))