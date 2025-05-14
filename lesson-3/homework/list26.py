lst = list(map(int, input().split()))
length = len(lst)
if length % 2 == 0:
    print(lst[length // 2 - 1], lst[length // 2])
else:
    print(lst[length // 2])