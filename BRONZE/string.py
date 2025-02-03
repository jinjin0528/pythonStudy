# 문자열 겹쳐쓰기

# def solution(my_string, overwrite_string, s):
#     l1 = list(my_string)
#     l2 = list(overwrite_string)
#     j = 0
#     for i in range(s, s+len(l2)):
#         l1[i] = l2[i]
#         j += 1
#         answer = ''.join(l1)
#         return answer
    def solution(my_string, overwrite_string, s):
        answer = my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]
        return answer