import sys

t = int(sys.stdin.readline().strip())  # sys를 덮어쓰지 않음!

for _ in range(t):
    coins = list(map(int, sys.stdin.readline().strip().split()))  # 매번 새로운 줄을 읽음
    d = coins[0]    # 동전 개수
    denominations = coins[1:]
    print(f"Denominations: {' '.join(map(str, denominations))}")

    # 조건 검사 (각 동전이 이전 동전의 최소 2배인지 확인)
    is_good = True
    for i in range(1, d):
        if denominations[i] < 2 * denominations[i - 1]:
            is_good = False
            break

    if is_good:
        print("Good coin denominations!")
    else:
        print("Bad coin denominations!")

    # 테스트 케이스 사이에 빈 줄 추가
    print()
