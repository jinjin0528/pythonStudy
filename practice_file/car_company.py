# 필기 : 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 이렇게 리스트로 따로 관리할 경우 회사가 사라지거나 상품이 추가되면 일일이 관리해야 한다는 문제가 있다.
# 차량 1
car_company_1 = {'Ferrari'}
car_detail_1 = [
    {'color': 'White'},
    {'housepower': 500},
    {'price': 8000}
]
# 차량 2
car_company_2 = {'BMW'}
car_detail_2 = [
    {'color': 'Black'},
    {'housepower': 300},
    {'price': 5000}
]
# 차량 3
car_company_3 = {'Audi'}
car_detail_3 = [
    {'color': 'Silver'},
    {'housepower': 400},
    {'price': 6000}
]

# 리스트 구조
car_company_list = ['Ferrari', 'BMW', 'Audi']
car_detail_list = [
    {'color': 'White', 'housepower': 500, 'price': 8000},
    {'color': 'Black', 'housepower': 300, 'price': 5000},
    {'color': 'Silver', 'housepower': 400, 'price': 6000},
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)
print()

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키는 유일해야), 키 조회 예외 처리 등
car_dicts = [
    {'car_company': 'Ferrari', 'car_detail':{'color': 'White', 'housepower': 500, 'price': 8000}},
    {'car_company': 'BMW', 'car_detail':{'color': 'Black', 'housepower': 300, 'price': 5000}},
    {'car_company': 'Audi', 'car_detail':{'color': 'Silver', 'housepower': 400, 'price': 6000}}
]
print(car_dicts)

del car_dicts[1]
print(car_dicts)

print()


# 클래스 구조
# 필기 : 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용
class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    car1 = Car('Ferrari', {'color': 'White', 'housepower': 500, 'price': 8000})

    print(car1)