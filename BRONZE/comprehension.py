# 리스트 컴프리헨션
nums = []

for n in range(1, 10+1):
    if n % 2 == 0:
        nums.append(n)
        print(nums)

# >>> 컴프리헨션 적용
num = [n for n in range(1, 10 + 1) if n % 2 == 0]
print(num)

z = [ (x, y) for x in ['포도', '딸기', '토마토'] for y in ['사과', '바나나', '파인애플']]
print(z)

v = [ (x,y,z) for x in ['포도', '딸기', '토마토'] for y in ['사과','바나나', '파인애플'] for z in ['배달 시키기', '가서 먹기']]
print(v)

# 딕셔너리 컴프리헨션
students = ['철수', '영희', '길동', '순희']
{ student: 0 for student in students }
{'철수': 0, '영희': 0, '길동': 0, '순희': 0}

scores = {'철수': 50, '영희': 80, '길동': 90, '순희': 60, '전학생': 100}
scores = { name: score for name, score in scores.items() if name != '전학생'}
print(scores)

grades = { name: 'PASS' if value > 70 else 'No-PASS' for name, value in scores.items()}
print(grades)