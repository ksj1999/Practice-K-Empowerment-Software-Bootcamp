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


