n = int(input())
m = input()
k = int(input())

if int(m) == 0:
    print('YES')
    exit(0)
x = -1
cnt = 0
while m[x] == '0':
    x -= 1
    cnt += 1
    if cnt ==n:
        break
# print(cnt)
if cnt >= k:
    print('YES')
else:
    print('NO')