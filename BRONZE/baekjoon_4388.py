import sys
from itertools import zip_longest

def count_carries(a, b):    # 문자열을 뒤집어 일의 자리부터 순서대로 더한다.
    a, b = str(a)[::-1], str(b)[::-1]  # 숫자를 문자열로 변환 후 뒤집기
    carry = 0  # 받아올림 값
    carry_count = 0  # 받아올림 발생 횟수

    for x, y in zip_longest(a, b, fillvalue='0'):  # 짧은 숫자는 '0'으로 채움
        sum_digits = int(x) + int(y) + carry
        if sum_digits >= 10:
            carry = 1
            carry_count += 1
        else:
            carry = 0

    return carry_count

# 입력 받기
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    print(count_carries(a, b))
