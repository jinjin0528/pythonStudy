from collections import Counter

n = int(input())
s = input()

counter = Counter(s)

target = ['u', 'o', 's', 'p', 'c']

print(min(counter[char] for char in target))