n = int(input())

lowerR = ['r','o','y','g','b','i','v']
upperR = ['R','O','Y','G','B','I','V']

s=[]
r=[]

low = 0
upp = 0

x = input()

for i in x:
    if i.isupper():
        r.append(i)
    elif i.islower():
        s.append(i)

if all(str in s for str in lowerR):
    low = 1
if all(str in r for str in upperR):
    upp = 1

if low == 1 and upp == 1:
    print('YeS')
elif low == 1 and upp == 0:
    print('yes')
elif low == 0 and upp == 1:
    print('YES')
else:
    print('NO!')

# rainbow = 'roygbiv'
# if n == 7 :
#     for _ in range(n):
#         if s.islower():
#             print('yes')
#         else :
#             print('YES')
'''
n = int(input())  # 문자열 길이 입력
s = input()       # 문자열 입력

rainbow_lower = "roygbiv"
rainbow_upper = "ROYGBIV"

# 소문자로만 된 무지개 문자열을 만들 수 있는지 확인
can_make_lower = all(c in s for c in rainbow_lower) and rainbow_lower in s

# 대문자로만 된 무지개 문자열을 만들 수 있는지 확인
can_make_upper = all(c in s for c in rainbow_upper) and rainbow_upper in s

# 출력 조건에 맞춰 결과 출력
if can_make_lower and can_make_upper:
    print("YeS")
elif can_make_lower:
    print("yes")
elif can_make_upper:
    print("YES")
else:
    print("NO!") '''
