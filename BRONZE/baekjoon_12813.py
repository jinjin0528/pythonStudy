A = input().strip()
B = input().strip()

# 2진수 문자열을 정수로 변환
A_int = int(A, 2)
B_int = int(B, 2)

# 비트 연산 수행
AND = A_int & B_int
OR = A_int | B_int
XOR = A_int ^ B_int
NOT_A = ~A_int & ((1 << len(A)) - 1)  # NOT 연산 후 100000비트 마스크 적용
NOT_B = ~B_int & ((1 << len(B)) - 1)

print(bin(AND)[2:].zfill(len(A)))
print(bin(OR)[2:].zfill(len(A)))
print(bin(XOR)[2:].zfill(len(A)))
print(bin(NOT_A)[2:].zfill(len(A)))
print(bin(NOT_B)[2:].zfill(len(A)))