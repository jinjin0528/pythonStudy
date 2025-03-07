lv, judge = input().split()
lv = int(lv)

if judge == 'miss':
    print(0)
elif judge == 'bad':
    print(lv*200)
elif judge == 'cool':
    print(lv*400)
elif judge == 'great':
    print(lv*600)
elif judge == 'perfect':
    n = 1
    print(n*lv*1000)


