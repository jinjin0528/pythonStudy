import math

# 입력 받기
n = int(input())
numbers = list(map(int, input().split()))

# 2개 또는 3개 숫자의 GCD 구하기
gcd_value = numbers[0]
for num in numbers[1:]:
    gcd_value = math.gcd(gcd_value, num)

# GCD의 모든 약수 구해서 출력
divisors = []
for i in range(1, int(gcd_value**0.5) + 1):
    if gcd_value % i == 0:
        divisors.append(i)
        if i != gcd_value // i:
            divisors.append(gcd_value // i)

for divisor in sorted(divisors):
    print(divisor)