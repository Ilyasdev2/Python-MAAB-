tple = tuple(map(str, input().split()))
tple1 = []
for i in range(len(tple)):
    if tple[i] not in tple1:
        tple1.append(tple[i])
print(tuple(tple1))