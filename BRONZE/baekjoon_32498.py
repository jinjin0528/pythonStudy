n = int(input())
excluded_count = 0  # 제외된 문제 개수 초기화

for _ in range(n):
    a = int(input())
    if a % 2 == 1:  # 홀수라면
        excluded_count += 1  # 제외된 문제 개수 증가

print(excluded_count)