t = int(input())

for _ in range(t):
    a,b,c = map(int, input().split())
    count = 0
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            for z in range(1, c + 1):
                r1 = x % y
                r2 = y % z
                r3 = z % x
                if r1 == r2 == r3:
                    count += 1
    print(count)