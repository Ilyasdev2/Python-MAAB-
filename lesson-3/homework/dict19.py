dc = {'a': 1, 'b': 2, 'c': 3}
lst = []
for i in dc.values():
    if i not in lst: lst += [i]
print(len(lst))