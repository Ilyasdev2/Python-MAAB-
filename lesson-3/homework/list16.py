lst = list(map(int, input().split()))
count = 0
for i in lst:
    if i % 2: count += 1
print(count)