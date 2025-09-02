n = int(input())

res = 0
for i in range(n):
    res += 1
    if str(i).find("50") > -1:
        res += 1
print(res)