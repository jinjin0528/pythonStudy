K = int(input())  # 시작하는 사람의 번호
N = int(input())  # 질문 개수

time_elapsed = 0  # 누적 시간
cur = K  # 현재 폭탄을 가진 사람

for _ in range(N):
    T, Z = input().split()
    T = int(T)
    time_elapsed += T

    if time_elapsed > 210:
        print(cur)
        break

    if Z == 'T':  # 정답 맞히면 왼쪽으로 넘김
        cur = (cur % 8) + 1