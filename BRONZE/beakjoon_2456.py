n = int(input())
candidates = [[0, 0, 0] for _ in range(3)]  # [total, count_3, count_2]

for _ in range(n):
    scores = list(map(int, input().split()))
    for i in range(3):
        candidates[i][0] += scores[i]  # total score
        if scores[i] == 3:
            candidates[i][1] += 1
        elif scores[i] == 2:
            candidates[i][2] += 1

# 최고 점수 찾기
max_score = max(candidates, key=lambda x: x[0])[0]

# 최고 점수를 받은 후보들 찾기
top_candidates = []
for idx, (total, c3, c2) in enumerate(candidates):
    if total == max_score:
        top_candidates.append((idx + 1, total, c3, c2))  # 후보 번호는 1부터

if len(top_candidates) == 1:
    print(top_candidates[0][0], top_candidates[0][1])
else:
    # 3점 수 비교
    max_3 = max(top_candidates, key=lambda x: x[2])[2]
    top_3 = [x for x in top_candidates if x[2] == max_3]

    if len(top_3) == 1:
        print(top_3[0][0], top_3[0][1])
    else:
        # 2점 수 비교
        max_2 = max(top_3, key=lambda x: x[3])[3]
        top_2 = [x for x in top_3 if x[3] == max_2]

        if len(top_2) == 1:
            print(top_2[0][0], top_2[0][1])
        else:
            print(0, max_score)
