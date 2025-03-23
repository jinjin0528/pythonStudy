def count_seconds(N):
    time = 0  # 걸린 시간
    K = 1  # 처음 부를 숫자

    while N > 0:  # 모든 새가 날아갈 때까지 반복
        if N < K:  # 불러야 할 숫자(K)보다 새가 적으면 다시 1부터 시작
            K = 1
        N -= K  # K마리의 새가 날아감
        K += 1  # 다음 숫자로 증가
        time += 1  # 1초 경과

    return time

N = int(input())
print(count_seconds(N))