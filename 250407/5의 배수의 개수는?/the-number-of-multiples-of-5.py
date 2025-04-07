cnt = 0
for _ in range(4):
    row = list(map(int, input().split()))
    for num in row:
        if num % 5 == 0:
            cnt += 1
print(cnt)
        