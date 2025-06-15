n = int(input())

for i in range(1,n+1):
    space = ' '*(n-i)
    if i == 1:
        print(space + '*')
    else:
        spaces = ' ' * (2*(i-1)-1)
        print(space+'*'+spaces+'*')