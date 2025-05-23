n, x = map(int, input().split())
t = list(map(int, input().split()))

current_volume = x
turn = 0

while True:
    person = turn % n
    if current_volume > t[person]:
        print(person + 1)  # 사람 번호는 1번부터 시작
        break
    current_volume += 1
    turn += 1