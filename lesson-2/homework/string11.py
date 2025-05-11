s = input()
s1 = '123456789'
ok = 1
for i in s:
    if i in s1:
        print(True)
        ok = 0
if ok: print(False)