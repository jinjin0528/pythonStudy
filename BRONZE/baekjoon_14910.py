n = list(map(int, input().split()))
t = True

for i in range(1, len(n)):
    if n[i - 1] > n[i]:
        t = False
        break

if t:
    print("Good")
else:
    print("Bad")