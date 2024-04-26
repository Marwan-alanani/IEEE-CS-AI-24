import numpy as np
def main():
    rows = input("insert number of rows: ")
    while not rows.isdigit():
        print("invalid number must enter an integer")
        rows = input("insert number of rows: ")
    rows = int(rows)
    cols = input("insert number of columns: ")
    while not cols.isdigit():
        print("invalid number must enter an integer")
        cols = input("insert number of columns: ")
    rows = int(rows)
    arr = np.empty((rows,cols),dtype='str')
    for i in range(rows):
        row = input("Enter picture colors seperated by a space: ").split()
        while len(row) != cols:
            print("number of columns don't match the number of columns you have given")
        row = input("Enter picture colors seperated by a space: ").split()
        arr[i] = row
    
    for color in np.nditer(arr):
        if not (color == 'B' or color == 'W' or color == 'G'):
            print("#Color")
            return
    print("#Black&White")

main()    