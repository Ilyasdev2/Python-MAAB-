lst = list(map(int, input().split()))
lst1 = []
for i in lst:
    if i not in lst1: lst.append(i)
print(lst1)