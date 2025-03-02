n, i = map(int,input().split())
handles = [input() for _ in range(n)]  # 핸들을 리스트로 저장
handles.sort()  # 사전 순 정렬

print(handles[i - 1])  # i번째 핸들 출력 (0-based index 보정)