import numpy as np


def linearAlgebra(matrix):
        # Convert to numpy array
        arr = np.array(matrix)

        # Compute determinant
        det = np.linalg.det(arr)

        # Print rounded to 2 decimal places
        return round(det, 2)
