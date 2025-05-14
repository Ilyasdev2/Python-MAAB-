lst = list(map(int, input().split()))
element = int(input())
for i in range(len(lst)): 
    if lst[i] == element: print(i, end=' ')
