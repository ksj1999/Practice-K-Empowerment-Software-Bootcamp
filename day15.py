def print_poly(px):
    """
    다항식을 포맷에 맞게 출력하는 함수
    :param px: 계수를 원소로 가지고 있는 list
    :return: 다항식 문자열
    """
    term = len(px) - 1
    poly_str = "P(x) = "

    for i in range(len(px)):
        coef = px[i]
        # if coef >= 0:
        #     poly_str = poly_str + "+"

        if i > 0 and coef > 0:
            poly_str = poly_str + "+"
        elif coef == 0:
            term = term - 1
            continue

        poly_str = poly_str + f'{coef}x^{term} '
        term = term - 1

    return poly_str


def calc_poly(x_val, p_x):
    """
    다항식의 산술연산을 하는 함수
    :param x_val: x값 integer
    :param p_x: 계수를 원소로 가지고 있는 list
    :return: 다항식 계산 결과 값 integer
    """
    return_val = 0
    term = len(p_x) - 1

    for i in range(len(px)):
        coef = p_x[i]
        return_val = return_val + coef * x_val ** term
        term = term - 1

    return return_val


px = [3, -4, 0, 6]

if __name__ == "__main__":
    print(print_poly(px))

    x_value = int(input("X 값 : "))
    print(calc_poly(x_value, px))