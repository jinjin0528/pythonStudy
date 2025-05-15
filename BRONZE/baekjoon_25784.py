a, b, c = map(int, input().split())

# 조건 검사
if a + b == c or a + c == b or b + c == a:
    print(1)
elif a * b == c or a * c == b or b * c == a:
    print(2)
else:
    print(3)