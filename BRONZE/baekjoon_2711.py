t = int(input())

for _ in range(t):
    line = input().split()
    pos = int(line[0])  # 오타 위치 (1-based)
    word = line[1]
    fixed = word[:pos - 1] + word[pos:]
    print(fixed)