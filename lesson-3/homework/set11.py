set1 = set(map(str, input().split()))
set2 = set(map(str, input().split()))
set3 = set1.symmetric_difference(set2)
print(set3)