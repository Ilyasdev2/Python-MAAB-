tple = tuple(map(int, input().split()))
start, end = int(input()), int(input())
print(max(tple[slice(start, end)]))