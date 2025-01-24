n = int(input())

for i in range(1,n+1):
    # print(i*'*')  별찍기
    print(" "*(n-i)+"*"*i)  #오른쪽에 별찍기