n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = sum(1 for i in range(n) if b[i] >= a[i])
print(count)