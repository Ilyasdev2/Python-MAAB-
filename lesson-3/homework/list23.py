lst = list(map(int, input().split()))
lst1 = []
for i in lst:
    if i % 2: lst1.append(i)
print(lst1)