n = int(input())  # 첫 줄에서 N 입력받기
numbers = list(map(int, input().split()))  # 두 번째 줄에서 N개의 숫자 입력받기

even_numbers = [num for num in numbers if num % 2 == 0]  # 짝수만 골라서 리스트에 저장

print(*even_numbers[::-1])  # 짝수 리스트를 역순으로 출력
