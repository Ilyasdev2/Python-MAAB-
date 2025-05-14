lst = list(map(int, input().split()))
sublst = list(map(int, input().split()))
sublst, lst = str(sublst)[1:-1], str(lst)[1:-1]
print(sublst in lst)