T = int(input())  # 테스트 케이스 수

for _ in range(T):
    N, D = map(int, input().split())  # 우주선 수 N, 거리 D
    count = 0  # 도달 가능한 우주선 수
    for _ in range(N):
        v, f, c = map(int, input().split())
        time_needed = D / v  # 도착에 필요한 시간
        fuel_needed = time_needed * c  # 필요한 연료량
        if fuel_needed <= f:  # 도달 가능한 경우
            count += 1
    print(count)