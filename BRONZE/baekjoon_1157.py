n = input().upper()
n_list = list(set(n))
co = []

for i in n_list:
    cnt = n.count
    co.append(cnt(i))

if co.count(max(co)) > 1 :
    print('?')
else :
    print(n_list[co.index(max(co))])