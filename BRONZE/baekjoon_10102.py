n = int(input())
vic = input().strip()

counta = vic.count('A')
countb = vic.count('B')

if counta > countb :
    print('A')
elif counta < countb :
    print('B')
else:
    print('Tie')
