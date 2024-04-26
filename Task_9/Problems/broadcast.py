import numpy as np
n = input("Enter dimensions: ")
while not n.isdigit():
    print("dimensions must be an integer!")
    n = input("Enter dimensions: ")
n = int(n)
arr = np.zeros((n,n),'int32')
arr += np.arange(1,n+1)
print(arr)