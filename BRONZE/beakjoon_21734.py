s = list(input())
for i in range(len(s)):
    times = sum(list(map(int, list(str(ord(s[i]))))))
    print(s[i] * times)