n = int(input())
problems = list(map(int, input().split()))  # 한 줄 입력을 리스트로 변환

max_streak = 0  # 최장 스트릭
current_streak = 0  # 현재 스트릭

for p in problems:
    if p > 0:  # 문제를 풀었으면 스트릭 증가
        current_streak += 1
        max_streak = max(max_streak, current_streak)  # 최장 스트릭 갱신
    else:  # 문제를 안 풀었으면 스트릭 초기화
        current_streak = 0

print(max_streak)
