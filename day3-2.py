# while

while True:
    dan = int(input('Dan (0 to quit):'))

    if dan == 0: exit()
        i = 1
        while i < 10:
            print('{0} * {1} = {2}'.format(dan, i, dan * i))
            i = i + 1
        break
    else:
        print('2에서 9사이의 값을 입력 하세요')