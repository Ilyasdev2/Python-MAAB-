tple = tuple(map(str, input().split()))
element = input()
idx = tple.index(element)
new_tple = tple[slice(0, idx)] + tple[slice(idx + 1, len(tple))]
print(new_tple)