k,n = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(k)]

cow_rank = []
for num in nums:
    rank = {}
    for pos, cow in enumerate(num):
        rank[cow] = pos
    cow_rank.append(rank)

count = 0

# 모든 소 쌍 (i, j) 검사
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            continue
        consistent = True
        for m in range(k):
            if cow_rank[m][i] >= cow_rank[m][j]:
                consistent = False
                break
        if consistent:
            count += 1

print(count)