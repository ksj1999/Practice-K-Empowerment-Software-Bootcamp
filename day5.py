# closures

def calculate():
    x = 1
    y = 2
    temp = 0
    def add_sub(n):
        nonlocal temp
       #  x = 11  # local variable
        temp = temp + x + n - y
        return temp
    print('once')
    return add_sub

c1 = calculate()
for i in range(5):
    print(c1(i))

