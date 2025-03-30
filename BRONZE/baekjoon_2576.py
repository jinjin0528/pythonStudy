odd_numbers = []  # 홀수를 저장할 리스트

for _ in range(7):
    n = int(input())
    if n % 2 == 1:  # 홀수라면 리스트에 추가
        odd_numbers.append(n)

if odd_numbers:  # 리스트에 값이 있으면 (홀수가 있으면)
    print(sum(odd_numbers))  # 홀수들의 합
    print(min(odd_numbers))  # 홀수 중 최솟값
else:  # 홀수가 없으면
    print(-1)