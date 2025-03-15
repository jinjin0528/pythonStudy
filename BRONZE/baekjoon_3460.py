n = int(input())

for _ in range(n):
    t =int(input())
    result = []

    i = 0
    while t > 0:
        if t%2 == 1:
            result.append(i)
        t //= 2
        i += 1
    print(" ".join(map(str, result)))
