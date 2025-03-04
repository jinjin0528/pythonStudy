X = int(input())  # X번째 분수 찾기

# 1. 몇 번째 그룹(n)에 속하는지 찾기
n = 1
while (n * (n + 1)) // 2 < X:  # n(n+1)/2 >= X가 될 때까지 증가
    n += 1

# 2. 그룹 내에서 몇 번째인지 찾기
start_index = (n * (n - 1)) // 2 + 1  # 현재 그룹의 첫 번째 인덱스
position = X - start_index  # 그룹 내 위치 (0부터 시작)

# 3. 분수 계산
if n % 2 == 0:  # 짝수 그룹은 위에서 아래로 진행
    numerator = 1 + position
    denominator = n - position
else:  # 홀수 그룹은 아래에서 위로 진행
    numerator = n - position
    denominator = 1 + position

print(f"{numerator}/{denominator}")
