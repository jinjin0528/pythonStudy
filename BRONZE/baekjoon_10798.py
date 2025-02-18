words = [input() for _ in range(5)]

# 최대 길이 계산
lists = max(len(word) for word in words)

# 세로로 읽어서 출력
result = ''
for i in range(lists):
    for word in words:
        if i < len(word):
            result += word[i]

print(result)
