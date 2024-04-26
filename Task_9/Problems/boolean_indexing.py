import numpy as np
arr = np.arange(2,33,2)
mean = np.mean(arr)
STD = np.std(arr)
print(arr[(mean-0.5*STD<=arr)&(arr<=mean+0.5*STD)])