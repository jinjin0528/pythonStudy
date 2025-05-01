dksh = input()
count = 0

for i in range(len(dksh) - 3):  # 문자열 범위를 벗어나지 않도록 -3
    if dksh[i:i+4] == "DKSH":
        count += 1

print(count)