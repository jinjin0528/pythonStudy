def find_meeting_point(X, Y, P1, P2):
    a, b = P1, P2
    visited = set()  # A의 점프 지점을 저장

    while a <= 10000:  # 넉넉하게 설정
        visited.add(a)
        a += X  # A가 다음으로 이동

    while b <= 10000:
        if b in visited:  # B의 점프 지점이 A와 겹치는지 확인
            return b
        b += Y  # B가 다음으로 이동

    return -1  # 공통 지점이 없음

X, Y, P1, P2 = map(int, input().split())
print(find_meeting_point(X, Y, P1, P2))
