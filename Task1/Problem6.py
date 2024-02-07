def main():
    num = int(input())
    sum = (num//2)*(num//2 + 1)
    print(f"The sum of even numbers from 1 to {num} is {sum} (",end='')
    for i in range(2,num,2):
        print(i,end=" + ")
    if num%2 == 0:
        print(num,end=").\n")
    else:
        print(num-1,end=").\n") 
main()
    