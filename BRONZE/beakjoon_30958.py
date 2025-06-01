alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

N = int(input())
logoSong = input()
result = 0

for i in alphabet:
    result = max(logoSong.count(i), result)

print(result)
'''-------------------'''

n = input()
str = input()
str_count = []

for i in str:
    if(i !=',') and (i != ' '):
        str_count.append(str.count(i))

print(max(str_count))