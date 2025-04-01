n = int(input())
response = input().strip()

count_bigdata = response.count("bigdata")
count_security = response.count("security")

if count_bigdata > count_security:
    print("bigdata?")
elif count_bigdata < count_security:
    print("security!")
else:
    print("bigdata? security!")
