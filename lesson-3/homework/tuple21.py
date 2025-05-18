tple = tuple(map(str, input().split()))
num = int(input())
tple1 = []
for i in range(len(tple)):
    tple1.extend([tple[i]] * num)
print(tuple(tple1))