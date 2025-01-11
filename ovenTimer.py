H, M = map(int, input().split())
timer = int(input())

# 타이머 시간을 60으로 나눠서 나머지는 시에, 몫은 분에 더해줌.
H += timer // 60
M += timer % 60

# 분이 60이 넘어가면 시에 1을 더하고 분에 60을 뺴주고
if M >= 60:
    H += 1
    M -= 60
# 시가 24 이상이면 시에 24를 빼준다.
if H >= 24:
    H -= 24

print(H,M)