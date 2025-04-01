a,b = map(int, input().split())
current = a
result = []

# B를 넘기지 않는 동안 반복
while current <= b:
    result.append(str(current))  # 현재 숫자 저장

    if current % 2 == 1:  # 홀수라면 2배
        current *= 2
    else:  # 짝수라면 +3
        current += 3

print(" ".join(result))