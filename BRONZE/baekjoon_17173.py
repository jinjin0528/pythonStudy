n,m = map(int, input().split())
k = list(map(int, input().split()))

multiples = set()   # 중복을 피하기 위해 set 사용

# 각 Ki에 대해 1부터 N까지의 배수를 찾음
for ki in k:
    for i in range(ki, n + 1, ki):
        multiples.add(i)

print(sum(multiples))