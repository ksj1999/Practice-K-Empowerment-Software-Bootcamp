alcohol_foods = {
    '맥주' : '치킨',
    '소주' : '골뱅이소면',
    '위스키' : '치즈',
    '고량주' : '짬뽕'
}
alcohol_list = list(alcohol_foods) # extract keys
while True:
    alcohol = input(f'술을 선택하세요 1) {alcohol_list[0]} 2) {alcohol_list[1]} 3) {alcohol_list[2]} 4) {alcohol_list[3]}:')
    if alcohol == '5':
        print('다음에 또 오세요~')
        break
    elif alcohol == '1':
        print(f'{alcohol_list[0]}에 어울리는 안주는 {alcohol_foods[alcohol_list[0]]}입니다')
        pass
    elif alcohol == '2':
        print(f'{alcohol_list[1]}에 어울리는 안주는 {alcohol_foods[alcohol_list[1]]}입니다')
        pass
    elif alcohol == '3':
        print(f'{alcohol_list[2]}에 어울리는 안주는 {alcohol_foods[alcohol_list[2]]}입니다')
        pass
    elif alcohol == '4':
        print(f'{alcohol_list[3]}에 어울리는 안주는 {alcohol_foods[alcohol_list[3]]}입니다')
        pass
    else:
        print('메뉴에서 골라주세요.')



# # dictionary
#
# students = {'name':'kiminha', 'age': 23, 'eyes': [0.9, 1.1]}
# # for k in students.keys():
# # for k in students():
# # for k in students.values():
# for k, v in students.items():
#     #print(k)
#     print(f'{k} : {v}')
# print(f'이름은 {students["name"]}, 나이는 {students["age"]}세', end=' ')
# print(f'시력은 좌: {students["eyes"][0]}, 우: {students["eyes"][1]}')
#
