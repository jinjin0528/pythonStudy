from collections import defaultdict, deque

def is_possible(words):
    in_deg = defaultdict(int)
    out_deg = defaultdict(int)
    graph = defaultdict(set)
    letters = set()

    for word in words:
        start = word[0]
        end = word[-1]
        out_deg[start] += 1
        in_deg[end] += 1
        graph[start].add(end)
        graph[end].add(start)  # 무방향 연결 그래프로 연결성 확인용
        letters.add(start)
        letters.add(end)

    # 1. in-degree == out-degree 확인
    for ch in letters:
        if in_deg[ch] != out_deg[ch]:
            return 0

    # 2. 연결성 확인 (BFS)
    visited = set()
    queue = deque()
    queue.append(next(iter(letters)))

    while queue:
        cur = queue.popleft()
        if cur in visited:
            continue
        visited.add(cur)
        for neighbor in graph[cur]:
            if neighbor not in visited:
                queue.append(neighbor)

    if len(visited) != len(letters):
        return 0

    return 1

n = int(input())
words = input().split()
print(is_possible(words))
