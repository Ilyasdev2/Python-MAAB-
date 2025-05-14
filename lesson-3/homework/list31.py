lst = list(map(int, input().split()))
num = int(input())
lst1 = []
for i in lst:
    lst1 += [i] * num
print(lst1)