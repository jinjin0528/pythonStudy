T = int(input())

for case_num in range(1, T + 1):
    B = int(input())
    binary_string = input()

    result = ''
    for i in range(B):
        byte_str = binary_string[i * 8:(i + 1) * 8]
        # 'I' -> '1', 'O' -> '0'
        binary = ''.join('1' if ch == 'I' else '0' for ch in byte_str)
        ascii_char = chr(int(binary, 2))
        result += ascii_char

    print(f"Case #{case_num}: {result}")