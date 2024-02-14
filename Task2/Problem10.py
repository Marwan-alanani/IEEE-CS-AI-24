import random

tries = 3
num = random.randint(1, 100)
while tries:
    inp = input("Enter your guess of numbers between 1->100 (inclusive): ")
    while not inp.isdigit():
        print("input must be a number")
        inp = input("Enter your guess again: ")

    inp = int(inp)
    tries -= 1

    if inp == num:
        print("You got it!")
        break
    elif inp > num:
        print(f"Number is less than current guess...{tries} tries remaining")
    elif inp < num:
        print(f"Number is less than current guess...{tries} tries remaining")
