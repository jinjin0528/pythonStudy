n = int(input())
for i in range(1,10):
    if n > 10**i:
        n = int(round(n+0.0001,-i))
    else:
        break
print(n)