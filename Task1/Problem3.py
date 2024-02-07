import math
def main():
    num = int(input())
    factorial = math.factorial(num)
    print(f"The factorial of {num} is {factorial} (",end='')
    for i in range(num,1,-1):
        print(i,end=" * ")
    print("1).")
main()