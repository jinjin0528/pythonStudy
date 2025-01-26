t = int(input())

for i in range(t):
    n = list(map(int, input().split()))
    print(min(n), max(n))