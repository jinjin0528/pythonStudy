t = int(input())

for _ in range(t):
    box = input().strip()
    w = int(input())
    words = [input().strip() for _ in range(w)]

    # 박스 글자 수 세기 (직접)
    box_counts = {}
    for c in box:
        if c not in box_counts:
            box_counts[c] = 1
        else:
            box_counts[c] += 1

    for word in words:
        # 단어 글자 수 세기 (직접)
        word_counts = {}
        for c in word:
            if c not in word_counts:
                word_counts[c] = 1
            else:
                word_counts[c] += 1

        possible = True
        for letter, count in word_counts.items():
            if box_counts.get(letter, 0) < count:
                possible = False
                break
        print("YES" if possible else "NO")
