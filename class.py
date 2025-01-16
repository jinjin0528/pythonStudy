class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price
b1 = BlackBox('Red', 20000)
print(f'이름은 {b1.name}이고 가격은 {b1.price}원 입니다.')

b2 = BlackBox('Blue', 40000)
print(f'이름은 {b2.name}이고 가격은 {b2.price}원 입니다.')

# 필기 : __init__ 함수는 객체가 생성될 때 자동으로 실행된다.
