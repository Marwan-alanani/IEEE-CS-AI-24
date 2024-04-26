n = input("Enter number of elements: ")
while not n.isdigit():
    print("Number must be an integer!")
    n = input("Enter number of elements: ")
n= int(n)
arr = input("Enter values seperated by a space").split()
while len(arr) != n:
    print("Mismatch between provided number of values and array entered !")
    arr = input("Enter values seperated by a space").split()
arr = list(map(int,arr))
sereja_points = 0
dima_points = 0
i = 0
j = n - 1
sereja_turn = True
while n:
    points = max(arr[i], arr[j])
    if points == arr[i]:
        i += 1
    else:
        j -= 1

    if sereja_turn:
        sereja_points += points
        sereja_turn = False
    else:
        dima_points += points
        sereja_turn = True
    n -= 1


print(f"{sereja_points} {dima_points}")
