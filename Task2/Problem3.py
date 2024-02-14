n = int(input())
arr = [int(i) for i in input().split()]
scores = set(arr)
scores = list(sorted(scores))
print(scores[len(scores) - 2])
