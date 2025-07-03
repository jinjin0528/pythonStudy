n = int(input())

for i in range(n):
    box = int(input())
    print("#" * box)
    mid = "#" + "J" * (box - 2) + "#"
    for _ in range(box - 2): print(mid)
    if box != 1: print("#" * box)
    if i != n - 1: print()