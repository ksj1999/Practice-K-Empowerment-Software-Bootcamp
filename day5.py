# function
import random

# def calucate_fee(*args):...
def calucate_fee(args) -> dict:

    """
    놀이공원 요금 계산
    :param args: ages in list
    :return: 전체 인원 수, 어름 수, 아이 수, 지불할 총 입장료
    """
    total = 0
    adults = 0
    kids = 0
    for age in args:
        if 19 <= age:  # adult
            total = total + 10000
            adults= adults + 1

        else:
            total = total + 3000
            kids = kids + 1
    return {'no_of_people' : len(args), 'no_of_adults' : adults,'no_of_kids' : kids, 'total_fee' : total}



no_of_visitor = int(input('몇 분 이세요? '))
ages = {random.randint(1, 60) for age in range(no_of_visitor)}
results = calucate_fee(ages)
print(f"전체인원은 {results['no_of_people']}명, 어른 {results['no_of_adults']}명 이며 어린이 {results['no_of_kids']}명 이고 가격은 {results['total_fee']} 입니다")



# 5분 방문하셨고 어른 2명 아이 3명 총 요금은 10000원 입니다
#
# print(calucate_fee(20, 20, 25))
# print(calucate_fee(45, 43, 10, 7))

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