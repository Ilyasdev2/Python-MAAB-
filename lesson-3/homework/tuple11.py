tple = tuple(map(str, input().split()))
element = input()
for i in range(len(tple)):
    if element == tple[i]:
        print(i, end=' ')