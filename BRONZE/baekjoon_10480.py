n = int(input())

for i in range(n):
    k = int(input())
    if k % 2 == 0:
        print(f'{k} is even')
    else:
        print(f'{k} is odd')