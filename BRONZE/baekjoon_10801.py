a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_win = 0
b_win = 0

for r in range(10):
    if a[r] > b[r]:
        a_win += 1
    elif a[r] < b[r]:
        b_win += 1

if a_win > b_win:
    print('A')
elif a_win < b_win:
    print('B')
else:
    print('D')