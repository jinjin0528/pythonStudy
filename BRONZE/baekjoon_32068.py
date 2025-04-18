def find_treasure_step(L, R, S):
    pos = S
    step = 1
    delta = 1
    sign = 1  # 첫 이동은 +1 (오른쪽)

    while True:
        if L == pos or R == pos:
            return step
        pos += sign * delta
        delta += 1
        sign *= -1
        step += 1

T = int(input())
results = []

for _ in range(T):
    L, R, S = map(int, input().split())
    results.append(find_treasure_step(L, R, S))

for r in results:
    print(r)
