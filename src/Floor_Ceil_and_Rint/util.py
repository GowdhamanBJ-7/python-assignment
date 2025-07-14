import numpy as np
np.set_printoptions(legacy='1.13')

def floor_Ceil_Rint(input_array):
        result = []
        result.append(np.floor(input_array))
        result.append(np.ceil(input_array))
        result.append(np.rint(input_array))
        return result