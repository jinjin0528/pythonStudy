n = int(input())

if n%3 == 0 and n%2==1:
    print('true')
elif n%2 == 0 and n%5 == 0:
    print('true')
else:
    print('false')