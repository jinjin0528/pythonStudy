record = input()

score = {'A': 0, 'B': 0}
i = 0
while i < len(record):
    player = record[i]
    points = int(record[i + 1])
    score[player] += points
    i += 2

    # 듀스 상황인지 확인
    if score['A'] >= 10 and score['B'] >= 10:
        if abs(score['A'] - score['B']) >= 2:
            print('A' if score['A'] > score['B'] else 'B')
            break
    else:
        if score['A'] >= 11 and score['A'] - score['B'] >= 2:
            print('A')
            break
        elif score['B'] >= 11 and score['B'] - score['A'] >= 2:
            print('B')
            break
