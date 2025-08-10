while True:
    y = int(input())
    if y == 0:
        break
    if y % 4 == 0 and y >= 1896:
        if 1914 <= y <= 1918 or 1939 <= y <= 1945:
            print(y, "Games cancelled")
        elif y > 2020:
            print(y, "No city yet chosen")
        else:
            print(y, "Summer Olympics")
    else:
        print(y, "No summer games")