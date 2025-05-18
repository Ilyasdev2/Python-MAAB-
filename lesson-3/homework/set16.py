set1 = set(map(int, input().split()))
set2 = set()
for i in set1:
    if i % 2 == 0: set2.add(i)
print(set2)