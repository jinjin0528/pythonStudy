a,b = map(int,input().split())

gridA = [list(map(int,input().split())) for _ in range(a)]
gridB = [list(map(int,input().split())) for _ in range(a)]

for i in range(a):
    for j in range(b):
        print(0 if gridA[i][j] == gridB[i][j] else 1, end=" ")
    print() 