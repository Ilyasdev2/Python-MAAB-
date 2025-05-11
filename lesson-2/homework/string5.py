vw = 'aouei'
s = input()
t, k = 0, 0
for i in range(len(s)):
    if s[i] in vw:
        t += 1
    else:
        k += 1
print(t, k)