lst = list(map(int, input().split()))
sm = 0
for i in lst: 
    if sm < 0: sm += i
print(sm)