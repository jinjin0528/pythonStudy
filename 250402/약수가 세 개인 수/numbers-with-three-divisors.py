start, end = map(int, input().split())

# Please write your code here.
count = 0  # 조건을 만족하는 숫자의 개수

for num in range(start, end + 1):  # start부터 end까지 반복
    divisors = [i for i in range(1, num + 1) if num % i == 0]  # 약수 리스트 생성
    if len(divisors) == 3:  # 약수 개수가 정확히 3개인지 확인
        count += 1

print(count)