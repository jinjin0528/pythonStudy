customer = '나손님'
show_price = 10000
print(f'{customer} 손님 커트 가격 {show_price}원 입니다.')

name = input('성함을 입력하시오 : ')
print(name)
people = int(input('인원을 입력하시오 : '))
if people > 5 :
   print('최대 4명만 가능합니다.')
else:
   print('예약이 완료되었습니다.')