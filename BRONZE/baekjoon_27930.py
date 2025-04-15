def check_subsequence(S, target):
    idx = 0
    for c in S:
        if c == target[idx]:
            idx += 1
            if idx == len(target):
                return True
    return False


def find_result(S):
    yonsei = "YONSEI"
    korea = "KOREA"

    # 먼저 YONSEI가 나오는지, 아니면 KOREA가 나오는지 비교
    i = j = 0
    for c in S:
        if i < len(yonsei) and c == yonsei[i]:
            i += 1
        if j < len(korea) and c == korea[j]:
            j += 1

        if i == len(yonsei):
            return "YONSEI"
        if j == len(korea):
            return "KOREA"


S = input().strip()
print(find_result(S))
