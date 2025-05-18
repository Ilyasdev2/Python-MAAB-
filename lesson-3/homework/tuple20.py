tple = tuple(map(int, input().split()))
num = int(input())
tple1 = [tple[i:i + num] for i in range(0, len(tple), num)]
print(tuple(tple1))