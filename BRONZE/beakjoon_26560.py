n = int(input())
for _ in range(n):
    sentence = input()
    if sentence[-1] != '.':
        print(sentence+'.')
    else:
        print(sentence)