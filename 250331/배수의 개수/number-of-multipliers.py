num, numm = 0,0

for _ in range(10):
    n = int(input())

    if n%3 == 0 :
        num+=1
    if n%5 == 0:
        numm+=1
print(num, numm)
