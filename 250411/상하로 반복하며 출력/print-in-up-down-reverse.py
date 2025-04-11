n = int(input())

for i in range(n):
    row = ""
    for j in range(n):
        if j % 2 == 0:
            row += str(i + 1)
        else:
            row += str(n - i)
    print(row)