dc = {'b': 3, 'a': 2, 'c': 1}
new_dc = {}
for i, j in dc.items():
    if j > 1:
        new_dc.update({i: j})
print(new_dc)