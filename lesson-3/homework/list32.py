lst = list(map(int, input().split()))
lst1 = list(map(int, input().split()))
for i in lst1: 
    if i not in lst: lst += [i]
print(sorted(lst))