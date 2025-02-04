s = list(input())
abc = 'abcdefghijklnmopqrstuvwxyz'

for i in abc:
    if i in s:
        print(s.index(i), end=" ")
    else:
        print(-1, end=" ")