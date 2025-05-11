vw = 'aouei'
s = input()
# t, k = 0, 0
for i in range(len(s)):
    if s[i] in vw:
        print('*', end='')
    else:
        print(s[i], end='')
# print(t, k)