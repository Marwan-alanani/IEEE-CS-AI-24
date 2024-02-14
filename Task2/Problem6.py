inp = input()
while not inp.isnumeric():
    print("String must be a numeric value")
    inp = input()
print(inp)