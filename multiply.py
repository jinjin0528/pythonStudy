# 세자리 수 곱셈 계산 방식에서 한자리씩 계산 값 구하기

a = int(input())
b = input() # b값의 한자릿 수씩 계산해야 하므로 인덱스로 한 자리씩 계산하기 위해 문자열로 입력받음

print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b)) # 총 값을 구하기 위해 int로 변환해주어야 숫자 계산 결과가 나옴. 아니면 숫자*문자열 계산임
