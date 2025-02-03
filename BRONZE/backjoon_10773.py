k = int(input())
list = []
for _ in range(k):
    n = int(input())
    if n == 0:
        list.pop()
    else :
        list.append(n)
print(sum(list))