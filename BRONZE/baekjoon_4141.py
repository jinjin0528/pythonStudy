def char_to_digit(c):
    c = c.upper()
    if c in 'ABC':
        return '2'
    elif c in 'DEF':
        return '3'
    elif c in 'GHI':
        return '4'
    elif c in 'JKL':
        return '5'
    elif c in 'MNO':
        return '6'
    elif c in 'PQRS':
        return '7'
    elif c in 'TUV':
        return '8'
    elif c in 'WXYZ':
        return '9'
    else:
        return ''  # 해당하지 않는 경우

def is_phone_palindrome(name):
    number = ''.join(char_to_digit(c) for c in name)
    return number == number[::-1]

n = int(input())
for _ in range(n):
    name = input().strip()
    if is_phone_palindrome(name):
        print("YES")
    else:
        print("NO")
