n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_coins = 0

# 3x3 격자가 가능한 모든 시작 위치를 탐색
for i in range(n - 2):
    for j in range(n - 2):
        coin_sum = 0
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                coin_sum += grid[x][y]
        max_coins = max(max_coins, coin_sum)

print(max_coins)
