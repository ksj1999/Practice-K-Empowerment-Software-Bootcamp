try:
    # raise Exception('쉬는 시간')
    # raise TypeError('타입에러')
    expr = input('분자 분모 입력 (띄어쓰기로 구분) : ').split()
    print(int(expr[0]) / int(expr[1]))

except ValueError as err:
    print(f'숫자를 입력해주세요({err})')

except ZeroDivisionError as err:
    print(f'분모에 0이 올 수 없습니다({err})')

except IndexError as err:
    print(f'입력 값의 범위에 문제가 있습니다({err})')

except Exception as other:
    print(f'에러발생: {other}')

else:  #예외가 발생하지 않았을 때
    print('프로그램 정상', end=' ')

finally:  #예외 발생 여부와 상관 없이 무조건 실행
    print('종료')




#value error
#zerodivision error



# def div_calc(a, b):
#     """
#     나누기 함수
#     :param a: 분자
#     :param b: 분모
#     :return: 계산결과
#     """
#
#     return a / b
#
#
#
# print(div_calc(15, 3))
# print(div_calc(7, 0))