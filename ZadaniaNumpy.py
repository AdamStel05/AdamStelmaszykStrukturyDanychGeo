import numpy as np
import random

np_array_a = np.random.randint(1,100,15)
print(min(np_array_a))
print(max(np_array_a))
print(np.std(np_array_a))

np_array_b = np.random.randint(10, size=(4,4))
print(np_array_b)
np_columns_b = np.sum(np_array_b, axis=0)
np_rows_b = np.sum(np_array_b, axis=1)
print(np_columns_b)
print(np_rows_b)

np_array_c = np.asarray(
                [0, 3, 6, 12, 15]
                [18, 21, 24, 27, 30]
                [33, 36, 39, 42, 45]
                [48, 51, 54, 57, 60]
                [63, 66, 69, 72, 75]
                )

for i in np_array_c:
    if i > 10 and i%%2 = 0:
        print(id[i])