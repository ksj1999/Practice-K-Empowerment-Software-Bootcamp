def test(func):
    def new_function(*args):
        print('start')
        result = func(*args)
        print('실행결과', result)
        print('end')
        return result
    return new_function


@test
def add_ints(a, b):
    return a + b


add_ints(3, 5)