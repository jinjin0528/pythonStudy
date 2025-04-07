arr = [list(map(int, input().split())) for _ in range(4)]
total = 0

for i in range(4):
    for j in range(i + 1):  # i >= j 인 부분만 더함
        total += arr[i][j]

print(total)
