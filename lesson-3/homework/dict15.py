keys = list(map(str, input().split()))
values = list(map(str, input().split()))
dc = {}
for i in range(len(keys)):
    dc.update({keys[i]: values[i]})
print(dc)