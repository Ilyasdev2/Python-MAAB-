s = input('Input sentence: ').split()
s1 = input('Replace: ')
s2 = input('With: ')
for i in s:
    if i == s1:
        print(s2, end=' ')
    else:
        print(i, end=' ')