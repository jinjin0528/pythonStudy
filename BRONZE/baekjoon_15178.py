n = int(input())

for _ in range(n):
    a,b,c = map(int, input().split())
    if a+b+c != 180:
        print(a, b, c, 'Check')
    else:
        print(a, b, c, "Seems OK")