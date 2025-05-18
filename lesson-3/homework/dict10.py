dc1 = {'a': 1, 'b': 2, 'c': 3}
key = input()
if key in dc1:
    print(f'{key}: {dc1.get(key)}')
else:
    print('Not found')