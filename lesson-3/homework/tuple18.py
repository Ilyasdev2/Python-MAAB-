tple = tuple(map(int, input().split()))
start, end = int(input()), int(input())
print(min(tple[slice(start, end)]))