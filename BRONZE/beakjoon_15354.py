def solve():
    n = int(input())
    for _ in range(n):
        s = input()
        count = 1
        if len(s) > 0:
            prev = s[0]
            for i in range(1, len(s)):
                if s[i] != prev:
                    count += 1
                    prev = s[i]
        print(count)

solve()