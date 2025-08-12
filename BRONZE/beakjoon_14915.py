m,n = map(int, input().split())
ans=''
overten='ABCDEF'
if m==0: print(0); exit()
while m!=0:
    if (m%n)>9: ans+=overten[(m%n)%10]
    else: ans+=str (m%n)
    m//=n
print(ans[::-1])