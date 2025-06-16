t = int(input())

for i in range(1, t+1):
    n,m = map(int, input().split())
    removable = m-(n-1)
    print(f"Case {i}: {removable}")
