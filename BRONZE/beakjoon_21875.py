def pos_to_coord(s):
    col = ord(s[0]) - ord('a') + 1
    row = int(s[1])
    return col, row

a = input().strip()
b = input().strip()

x1, y1 = pos_to_coord(a)
x2, y2 = pos_to_coord(b)

dx = abs(x2 - x1)
dy = abs(y2 - y1)

print(min(dx, dy), max(dx, dy))