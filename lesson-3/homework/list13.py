lst = list(map(int, input().split()))
element = int(input())
try:
    print(lst.index(element))
except:
    print(False)