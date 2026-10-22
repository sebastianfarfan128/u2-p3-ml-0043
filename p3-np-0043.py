# Array Indexing in NumPy
import numpy as np
n0043 = np.array([10, 20, 30, 40, 50])
print(n0043)
print(n0043[0])
print(n0043[4])
print(n0043[-1])
print(n0043[-2])
print("-----------------------------------")
n0043 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(n0043)
print(n0043[0, 0])
print(n0043[1, 2])
print(n0043[-1, -1])
print(n0043[-2, -2])
print("-----------------------------------")
# 3D array 2x(2x3)
n0043 = np.array([
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])
#0 -2
#1 -1
print(n0043)
print(n0043[0, 0, 0])
print(n0043[1, 1, 2])
print(n0043[-1, -1, -2])
print("Sebastian Farfan NC = 0043")