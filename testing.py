import numpy as np
arr = np.arange(8)
arr_reshaped = np.reshape(arr, (4,2))
transposed = np.transpose(arr_reshaped)
print(repr(arr))
print(repr(arr_reshaped))
print(repr(transposed))