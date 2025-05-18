dc1 = {'a': 1, 'b': 2, 'c': 3}
value = int(input())
lst = []
for i, j in dc1.items():
    if j == value:
        lst.append(i)
print(lst)