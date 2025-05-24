# 초기 재료량 입력
Fs, Cs, Es, Bs = map(int, input().split())
# 쿠키 하나 만들 때 필요한 재료량 입력
Fn, Cn, En, Bn = map(int, input().split())

# 쿼리 개수 입력
Q = int(input())

# 지금까지 만든 쿠키 수
cookie_count = 0

# 쿼리 처리
for _ in range(Q):
    query = input().split()
    t = int(query[0])  # 쿼리 유형
    i = int(query[1])  # 해당 재료 양 또는 쿠키 개수

    if t == 1:
        # 쿠키 i개 만들 수 있는지 확인
        if Fs >= Fn * i and Cs >= Cn * i and Es >= En * i and Bs >= Bn * i:
            Fs -= Fn * i
            Cs -= Cn * i
            Es -= En * i
            Bs -= Bn * i
            cookie_count += i
            print(cookie_count)
        else:
            print("Hello, siumii")
    elif t == 2:
        Fs += i
        print(Fs)
    elif t == 3:
        Cs += i
        print(Cs)
    elif t == 4:
        Es += i
        print(Es)
    elif t == 5:
        Bs += i
        print(Bs)