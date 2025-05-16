n = int(input())  # 데이터셋의 수

for _ in range(n):
    a, b = map(float, input().split())  # 두 값을 실수형으로 입력 받음
    distance = abs(a - b)  # 절대값 거리 계산
    print(f"{distance:.1f}")  # 소수점 1자리까지 반올림 후 출력