n, m = map(int, input().split())

a, b = n, m  # 원래 값 저장

# 최대공약수 구하기 (유클리드 호제법)
while m != 0:
    n, m = m, n % m

gcd = n
lcm = (a * b) // gcd

print(lcm)