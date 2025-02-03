x = int(input())    # 영수증 총 금액
n = int(input())    # 구매한 물건 개수
sum = 0
for i in range(n):
    a,b = map(int, input().split()) # 각 물건의 금액과 개수
    sum += (a*b)

if x == sum:
    print('yes')
else:
    print('no')