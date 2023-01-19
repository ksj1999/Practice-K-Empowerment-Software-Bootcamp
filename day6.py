try:
    expr = input('분자 분모 입력 (띄어쓰기로 구분) : ').split()
    print(int(expr[0]) / int(expr[1]))


except Exception:
    print(f'Caught an oops')

