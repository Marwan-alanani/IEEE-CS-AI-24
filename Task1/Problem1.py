def main():
    while(True):
        arr =[int(i) for i in input().split()]
        maxNum = arr[0]
        minNum = arr[0]
        flag = False
        for num in arr:
            if num==-1:
                flag = True
                break
            if num>maxNum:
                maxNum = num
            if num<minNum:
                minNum = num
        print(f"{maxNum} {minNum}")
        if flag:
            break
main()