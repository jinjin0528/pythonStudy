n = int(input())

for i in range(n):
    row = list(range(1, n + 1))
    if i % 2 == 1:
        row.reverse()
    print("".join(str(num) for num in row))
