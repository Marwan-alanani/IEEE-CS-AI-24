import math
def main():
    num = int(input())
    if num == sumOfDivisors(num):
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is not a perfect number")  


def sumOfDivisors(num):
    sum = 1
    squareRoot = math.sqrt(num)

    for i in range(2,int(squareRoot)):
        if num%i == 0 :
            sum += i + num//i

    if squareRoot.is_integer():
        sum += squareRoot
            
    return sum


main()