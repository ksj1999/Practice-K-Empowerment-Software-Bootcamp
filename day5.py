# function

def calucate_fee(*args):
    """
    놀이공원 요금 계산
    :param args: ages
    :return: 지불할 총 입장료
    """
    total = 0
    for age in args:
        if 19 <= age:  # adult
            total = total + 10000
        else:
            total = total + 3000
    return total

print(calucate_fee(20, 20, 25))
print(calucate_fee(45, 43, 10, 7))

#
# def do_nothing():
#     pass
#
# mamamoo = ['화사', '솔라', '휘인', '문별']
#
# #print(mamamoo.pop())  # 삭제할 값 리턴 후 삭제
# print(mamamoo.remove('문별'))  # 삭제만 함, 따라서 print함수는 출력할 값이 없다
# print(mamamoo)
# #
# # do_nothing()
# # print(do_nothing())