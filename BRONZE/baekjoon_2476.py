n = int(input())
dice = []
for _ in range(n):
    a,b,c = map(int, input().split())
    if a == b == c :
        t = 10000+a*1000
    elif a == b or a == c :
        t = 1000+a*100
    elif b == c:
        t = 1000+b*100
    else:
        t = max(a,b,c)*100
    dice.append(t)
print(max(dice))