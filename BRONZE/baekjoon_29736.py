a,b = map(int, input().split())
k,x = map(int,input().split())

mini = k-x
maxi = k+x
cnt = max(0, min(b, maxi) - max(a,mini)+1)

if cnt > 0 :
    print(cnt)
else:
    print('IMPOSSIBLE')
