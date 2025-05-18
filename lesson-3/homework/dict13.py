dc1 = {'a': 1, 'b': 2, 'c': 3}
new_dc = {value: key for key, value in dc1.items()}
print(new_dc)