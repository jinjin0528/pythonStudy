s = list(map(int,input().split()))
num = 0
for i in s:
    num += i*i

print(num%10)

