dc = {'b': 3, 'a': 2, 'c': 1}
print({key: value for key, value in sorted(dc.items(), key = lambda item: item[1])})