k = int(input())
for i in range(1,k+1):  # 데이터 셋 번호
    h = int(input())
    s = input()
    for j in s:
        if j == "c":
            h += 1
        else:
            h -= 1
    print(f'Data Set {i}:')
    print(h)
    print()