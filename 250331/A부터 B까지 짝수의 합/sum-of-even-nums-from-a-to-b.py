a,b = map(int, input().split())
total = 0
for i in range(a,b):
    if i%2 == 1:
        continue
    else:
        total += i
    
print(total)