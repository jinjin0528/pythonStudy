import sys

s,n,m = map(int,sys.stdin.readline().split())
u = 0
max_s = s

for _ in range(n+m):
    command = int(sys.stdin.readline().strip())
    
    if command == 1:
        if u == s:
            s *= 2
        u += 1
        max_s = max(max_s,s)
    elif command == 0:
        u -= 1
print(max_s)