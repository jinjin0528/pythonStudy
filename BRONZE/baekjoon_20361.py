n, x, k = map(int, input().split())
cup = [0] * (n+1)   # cup 리스트를 만들어, 각 컵의 위치를 저장, 컵 번호를 1번부터 사용
cup[x] = 1  # 공이 있는 컵 = 1, 결과는 0아니면 1 중 공이 있는 컵은 1이기 때문에

for _ in range(k):
    a, b = map(int, input().split())
    cup[a], cup[b] = cup[b], cup[a]
print(cup.index(1))