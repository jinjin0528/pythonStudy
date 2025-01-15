num = [1, 2, 3, 4, 5]

for i in num:
    print(i)
    if i == 3:
        print(f'{i}에서 stop')
        continue
print(f'{i} 출력')