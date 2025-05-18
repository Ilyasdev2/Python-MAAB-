dc1 = {'a': 1, 'b': 2, 'c': 3}
value = int(input())
count = 0
for i in dc1.values():
    if i == value: count += 1
print(count)