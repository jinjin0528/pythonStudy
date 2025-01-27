# 입력 받기
N, M = map(int, input().split())
baskets = [0] * N  # 바구니 초기화

# 명령 처리
for _ in range(M):
    i, j, k = map(int, input().split())
    for idx in range(i - 1, j):  # i-1부터 j-1까지
        baskets[idx] = k  # k번 공을 넣음

# 출력
print(" ".join(map(str, baskets)))

