import math

k = input().strip()
if '.' in k:
    integer_part, fractional_part = k.split('.')
    p = int(fractional_part)
    q = 10 ** len(fractional_part)
else:
    p = int(k)
    q = 1

# 약분
g = math.gcd(p, q)
p //= g
q //= g

# 오차 확인
k_val = float(k)
frac_val = p / q
abs_error = abs(k_val - frac_val)
rel_error = abs_error / k_val if k_val != 0 else 0

if abs_error <= 1e-6 or rel_error <= 1e-6:
    print("YES")
    print(p, q)
else:
    print("NO")
