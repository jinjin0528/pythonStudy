t = int(input())
leng = list(map(float, input().split()))
total = 0
for i in leng:
    total += i**3
print(total**(1/3))
