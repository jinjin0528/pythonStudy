def h(a) :
    s = 0
    while a//1 != 0 :
        s += (a%10)**2
        a = int(a/10)
    return (s)

a = int(input())

#각 자릿수의 제곱합이 1혹은 4가 될때 까지 반복해서 구해주는 반복문
while 1 :
    a = h(a)
    if a == 4 :
        print('UNHAPPY')
        break
    elif a == 1 :
        print('HAPPY')
        break