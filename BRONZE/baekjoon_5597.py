x = [i for i in range(1,31)]

for _ in range(28):
    applied = int(input())
    x.remove(applied)   # 제출한 번호 제거

print(min(x))
print(max(x))
print(x)