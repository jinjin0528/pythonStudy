class Test:
    def __init__(self, num1,num2):
        self.num1 = 3
        self.num2 = 5
        try:
            result = num1 / num2
            print(f'계산 결과 : {result}')
        except:
            print('Error')
        else:
            print('계산 성공, try 에러 없음')
        finally:
            print('수행을 종료합니다.')
'''
class Test:
    def __init__(self, num1, num2):
        self.num1 = 3
        self.num2 = 5
        try:
            result = num1 / num2
            print(f'계산 결과 : {result}')
        except ZeroDivisionError:
            print('Error: 0으로 나눌 수 없습니다.')
        else:
            print('계산 성공, try 에러 없음')
        finally:
            print('수행을 종료합니다.')
'''
# 예외처리 확인
test = Test(10, 5)
