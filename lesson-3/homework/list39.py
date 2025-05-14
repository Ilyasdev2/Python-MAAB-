lst = list(map(int, input().split()))
num = int(input())
lst1 = [lst[i:i + num] for i in range(0, len(lst), num)]
print(lst1)