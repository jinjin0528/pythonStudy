n = int(input())
num = []

for i in range(1, n+1):
    if i%2 == 0 :
        continue
    elif i%3 == 0 :
        continue
    elif i%5 == 0:
        continue
    else:
        num.append(i)

print(len(num))