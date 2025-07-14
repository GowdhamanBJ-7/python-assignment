import numpy as np

def min_max(arr):
    col = np.min(arr, axis=1)
    return np.max(col)
