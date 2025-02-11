def group_word(word):
    n = set()
    u = ''
    for i in word:
        if i != u and i in n:
            return False
        n.add(i)
        u = i
    return True

t = int(input())
cnt = 0

for i in range(t):
    word = input().strip()
    if group_word(word):
        cnt += 1

print(cnt)