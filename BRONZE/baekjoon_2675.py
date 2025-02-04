t = int(input())

for _ in range(t):
    r, s = input().split()
    for i in s:
        print(i*int(r), end='') # end가 없으면 자동 여러 줄로 출력이 됨
    print() # 없으면 출력값 옆에 입력해야 됨
