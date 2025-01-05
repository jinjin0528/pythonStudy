a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

a,b = input().split()
a = int(a)
b = int(b)

print(a+b)
print(a-b)
print(a*b)
print(a//b) # 몫을 구할 땐 a//b
print(a%b)  # 나머지를 구할 땐 a%b