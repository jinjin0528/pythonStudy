t =  int(input())

for i in range(t+1):
    n,m = map(int, input().split())
    res = (m - n + 1) * (n + m) // 2
    print(f"Scenario #{i}:")
    print(f"{res}\n")