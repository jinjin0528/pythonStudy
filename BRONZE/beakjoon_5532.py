import math

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

korean = math.ceil(A / C)
maths = math.ceil(B / D)

x = max(korean, maths)

print(L - x)