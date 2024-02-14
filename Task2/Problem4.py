list1 = []
N = int(input())
for _ in range(N):
    inp = input().split()
    match inp[0]:
        case "insert":
            list1.insert(int(inp[1]), int(inp[2]))
        case "pop":
            list1.pop()
        case "print":
            print(list1)
        case "remove":
            list1.remove(int(inp[1]))
        case "append":
            list1.append(int(inp[1]))
        case "sort":
            list1.sort()
        case "reverse":
            list1.reverse()
