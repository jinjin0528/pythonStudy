# 입력 받기
s = input()

# 등급-학점 매핑 딕셔너리 (공백 제거)
grades = {
    "A+": 4.5, "A": 4.0,
    "B+": 3.5, "B": 3.0,
    "C+": 2.5, "C": 2.0,
    "D+": 1.5, "D": 1.0,
    "F": 0.0
}

# 문자열을 2글자 단위로 나누어 학점 계산
subject = []
i = 0
while i < len(s):
    if i + 1 < len(s) and s[i + 1] == '+':  # A+ 같은 경우
        subject.append(s[i] + '+')
        i += 2
    else:  # A, B, C, D, F 같은 경우
        subject.append(s[i])
        i += 1

# 학점 평균 계산
total = sum(grades[grade] for grade in subject)
average = total / len(subject)

# 결과 출력 (소수점 네 자리까지 정확히)
print(f"{average:.4f}")
