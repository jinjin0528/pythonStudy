n = int(input())
num = list(map(int, input().split()))
new_arr = [elem * elem for elem in num]

for i in range(n):
	print(new_arr[i], end=" ")