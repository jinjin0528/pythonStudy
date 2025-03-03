n = int(input())
k = 1   # 1층 = 1, 2층 = 2-7, 3층 = 8-19... +1층 = +6
lastNum = 1

while lastNum < n:
    lastNum += 6*k
    k += 1
print(k)