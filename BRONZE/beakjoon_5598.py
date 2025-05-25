li = list(input())
for i in range(len(li)):
    k = ord(li[i]) - 3
    if k < ord('A'):
        k += 26
    li[i] = chr(k)
print(''.join(li))
'''----------------------'''
def decrypt_caesar(cipher_text):
    result = ''
    for ch in cipher_text:
        # A의 ASCII 값은 65, Z는 90
        # (ord(ch) - 65 - 3) % 26 을 통해 3칸 이전 문자 구함
        decrypted = chr((ord(ch) - ord('A') - 3) % 26 + ord('A'))
        result += decrypted
    return result

# 입력 받기
cipher_text = input().strip()
# 해독 결과 출력
print(decrypt_caesar(cipher_text))