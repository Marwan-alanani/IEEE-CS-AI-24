import numpy as np
n = int(input())
arr = np.zeros((n,n),'int32')
arr += np.arange(1,n+1)
print(arr)