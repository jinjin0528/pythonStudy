fruit = ["apple","banana","grape","blueberry","orange"]
inp = input()
matching_fruits = []

for i in fruit:
    # 세 번째 문자와 네 번째 문자가 존재하는지 확인 후 비교
    if (len(i) > 2 and i[2] == inp) or (len(i) > 3 and i[3] == inp):
        matching_fruits.append(i)  # 조건 만족하는 문자열 저장

# 결과 출력
for i in matching_fruits:
    print(i)
print(len(matching_fruits))