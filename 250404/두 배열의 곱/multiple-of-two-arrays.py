import sys

a = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

# 빈 줄 스킵
sys.stdin.readline()

b = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

# 곱셈 결과 출력
for i in range(3):
    for j in range(3):
        print(a[i][j] * b[i][j], end=" ")
    print()
