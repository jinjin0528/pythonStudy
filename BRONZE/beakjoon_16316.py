n = int(input())
words = input().split()

sense = True

for i in range(n):
    expected = str(i + 1)
    if words[i] != "mumble" and words[i] != expected:
        sense = False
        break

print("makes sense" if sense else "something is fishy")