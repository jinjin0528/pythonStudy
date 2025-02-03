''' file 입출력 :
    r = reading(읽기(조회)
    a = append(읽기 + 추가)
    w = write(쓰기)'''

# file writing
f = open('test.txt', 'w', encoding='utf8')
f.write('홍길동\n')
f.write('유관순\n')
f.write('안중근\n')
f.close()

#file reading
f = open('test.txt', 'r', encoding='utf8')
content = f.read()
print(content)
f.close()
# 같은 reading이지만 한줄씩 가져오기
f = open('test.txt', 'r', encoding='utf8')
for line in f:
    print(line, end='')
f.close()

with open('test.txt', 'w+', encoding='utf8') as f:
    f.write('one\n')
    f.write('two\n')
    f.write('three\n')

    f.seek(0)

    contents = f.read()
    print(contents)