str = input()
leng = len(str)

str = str[:1]+'a'+str[2:]
str = str[:leng -2]+'a'+str[leng -1]
print(str)