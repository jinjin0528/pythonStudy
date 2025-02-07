n = int(input())

for _ in range(n):
    a = list(input().split())
    if a[0] == 'Simon' and a[1] == 'says':
        print("",*a[2:])

'''       
N = int(input())

for _ in range(N):
    command = input()
    if command[:10] == "Simon says":
        print(command[10:]) '''
