import math
def main():
    num = int(input())
    primeFactors = getPrimefactors(num)
    print("Prime factors: ",end='')
    for i in range(len(primeFactors)-1):
        print(primeFactors[i],end=', ')
    print(primeFactors[-1],end='')


def getPrimefactors(num):
    primeFactors = []
    squareRoot = math.sqrt(num)
    for i in range(2,int(squareRoot)):
        if num%i == 0:
            if isPrime(i):
                primeFactors.append(i)
            if isPrime(num//i):
                primeFactors.append(num//i)
    if squareRoot.is_integer():
        if(isPrime(squareRoot)):
            primeFactors.append(squareRoot)
    return primeFactors


def isPrime(num):
    for i in range(2,int(math.sqrt(num)) + 1):
        if num%i == 0:
            return False
    return True


main()