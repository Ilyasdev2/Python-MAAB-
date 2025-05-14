lst = list(map(int, input().split()))
element = int(input())
element1 = int(input())
try:
    lst[lst.index(element)] = element1
    print(lst)
except:
    pass