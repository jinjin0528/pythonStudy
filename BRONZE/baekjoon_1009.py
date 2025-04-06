import sys
t = int(sys.stdin.readline())
for _ in range(t):
    a,b = map(int,sys.stdin.readline().split())
    n = a**b
    if n % 10 == 0:
        print(10)
    else:
        print(n % 10)
print()

'''import sys
t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    a = a % 10  # 끝자리만 중요함

    if a == 0:
        print(10)
        continue

    # 끝자리 패턴 테이블 (0은 예외 처리함)
    pattern_dict = {
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]
    }

    pattern = pattern_dict[a]
    index = (b - 1) % len(pattern)
    print(pattern[index])
'''
