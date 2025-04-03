matrix = [list(map(int, input().split())) for _ in range(3)]

# 모든 원소를 3배로 변환
for row in matrix:
    for i in range(3):
        row[i] *= 3

for row in matrix:
    print(*row)