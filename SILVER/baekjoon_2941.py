n = input()
cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in cro:
    n = n.replace(i,'*')    # 해당 문자를 *로 바꿔머림
print(len(n))