# function

def inha():
    """
    숫자 출력
    :return:
    """
    print(60)


def call_func(f):
    """
    매개변수로 함수를 넘겨받아 실행
    :param f: 매개변수가 함수
    :return:
    """
    f()  #넘겨받은 함수 실행


def subtract(n1, n2):
    print(n1, n2)

def run_func(f, arg1, arg2):

a = (5, 7, -11)
print(sum(a))
    """
    
    :param f: 
    :param arg1: 
    :param arg2: 
    :return: 
    """
    f(arg1, arg2)
run_func(subtract, 99, 88)

call_func(inha)
print(type(call_func))