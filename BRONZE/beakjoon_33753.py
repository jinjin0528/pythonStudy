a,b,c = map(int, input().split())
t = int(input())
if t <= 30:
    print(a)
else:
    overtime = t - 30
    over_charge_count = (overtime + b - 1) // b

    print(a + (over_charge_count * c))