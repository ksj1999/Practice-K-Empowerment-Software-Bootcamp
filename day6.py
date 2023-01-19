def factorial_iter(n):
    """
    반복문을 사용한 펙토리얼 함수
    :param n: n!
    :return: 팩토리얼 계산 결과 값
    """
    result = 1
    for k in range(1, n+1):
        result = result * k
    return result

def factorial_recu(n):
    """
    재귀함수를 사용한 팩토리얼 게산 함수
    :param n: n!
    :return: 자기 자신을 호출 또는 1
    """
    if n == 1:  #끝나는 조건
        return 1
    else:
        return factorial_recu(n-1) * n




print(factorial_iter(10))
print(factorial_recu(10))
