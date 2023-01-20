# 10-1
class Thing():
    pass


example = Thing()

print(example)


# 10-2
class Thing2():
    def __init__(self, letters):
        self.letters = letters


a = Thing2('abc')

print(a.letters)

# 10-3
class Thing3():
    def __init__(self, letters):
        self.letters = letters


b = Thing2('xyz')

print(b.letters)


# 10-4

class Element():
    def __init__(self):
        self.name = 'hydrogen'
        self.symbol = 'h'
        self.number = '1'




