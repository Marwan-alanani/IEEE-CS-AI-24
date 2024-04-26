def main():
    rows, cols = map(int, input().split())
    arr = [None] * rows
    for i in range(rows):
        arr[i] = input().split()
    for i in range(rows):
        for j in range(cols):
            if arr[i][j]  not in "BWG":
                print("#Color")
                return
    print("#Black&White")


main()