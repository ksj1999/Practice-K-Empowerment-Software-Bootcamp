# while

while True:
    dan = int(input('Dan (0 to quit):'))

    if dan == 0: #exit()
        break
    if 1 < dan < 10:
        for i in range(1, 10):
            print('{0} * {1} = {2}'.format(dan, i, dan * i))
    else:
        print('2에서 9사이의 값을 입력 하세요')