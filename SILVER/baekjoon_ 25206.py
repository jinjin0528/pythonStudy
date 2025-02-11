import sys

grade_dict = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}

total_score = 0 # (학점*과목평점)의 합
total_credit = 0    # 학점의 총합

for _ in range(20):
    sub, score, grade = sys.stdin.readline().split()
    score = float(score)

    if grade == 'P':
        continue    # 계산에서 제외

    total_score += score * grade_dict[grade]
    total_credit += score

print(total_score /total_credit)

