t = int(input())

for _ in range(t):
    lt, wt, le, we = map(int, input().split())

    area_t = lt * wt  # TelecomParisTech의 면적
    area_e = le * we  # Eurecom의 면적

    if area_t > area_e:
        print("TelecomParisTech")
    elif area_t < area_e:
        print("Eurecom")
    else:
        print("Tie")
