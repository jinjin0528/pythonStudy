n,m = map(int, input().split())
print(n * m - 1 if n % 2 and m % 2 else n * m)
