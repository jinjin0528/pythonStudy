N, M = map(int, input().split())  # 바구니 수 N, 교환 작업 수 M
baskets = [i for i in range(1, N + 1)]  # 초기 바구니 상태 [1, 2, ..., N]
# 리스트 컴프리헨션

# M번 교환 작업 처리
for _ in range(M):
    i, j = map(int, input().split())  # 교환할 바구니 번호
    # 바구니는 1번부터 시작하므로 인덱스를 맞추기 위해 -1
    baskets[i-1], baskets[j-1] = baskets[j-1], baskets[i-1]

print(" ".join(map(str, baskets)))
