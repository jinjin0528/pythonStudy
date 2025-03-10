import sys

n, q = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# 누적 합 배열 생성
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + arr[i - 1]

# 쿼리 처리
for _ in range(q):
    query = list(map(int, sys.stdin.readline().split()))

    if query[0] == 1:  # 1 a b -> 구간 합 계산 후 swap
        a, b = query[1], query[2]

        # 구간 합 출력
        result = prefix[b] - prefix[a - 1]
        print(result)

        # Swap 수행 (1-based index)
        arr[a - 1], arr[b - 1] = arr[b - 1], arr[a - 1]

        # 두 개의 원소만 누적 합 업데이트
        for i in range(a, b + 1):
            prefix[i] = prefix[i - 1] + arr[i - 1]

    else:  # 2 a b c d -> 두 구간의 차 출력
        a, b, c, d = query[1], query[2], query[3], query[4]
        result = (prefix[b] - prefix[a - 1]) - (prefix[d] - prefix[c - 1])
        print(result)
