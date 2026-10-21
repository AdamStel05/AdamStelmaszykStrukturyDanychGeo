import numpy as np
import random

# Zadanie a
np_array_a = np.random.randint(1,100,15)
print(np_array_a)

print(min(np_array_a))

print(max(np_array_a))

print(np.std(np_array_a))

# Zadanie b
np_array_b = np.random.randint(10, size=(4,4))
print(np_array_b)

np_columns_b = np.sum(np_array_b, axis=0)
print(np_columns_b)

np_rows_b = np.sum(np_array_b, axis=1)
print(np_rows_b)

# Zadanie c
np_array_c = np.asarray([
                [0, 3, 6, 12, 15],
                [18, 21, 24, 27, 30],
                [33, 36, 39, 42, 45],
                [48, 51, 54, 57, 60],
                [63, 66, 69, 72, 75]
                ])
print(np_array_c)

for indeksR, R in enumerate(np_array_c):
    W = indeksR
    for indeksC, C in enumerate(R):
        K = indeksC
        if C > 10 and C%2 == 0:
            print(W, K)