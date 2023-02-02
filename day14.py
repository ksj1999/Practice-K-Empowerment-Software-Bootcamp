# 10-4

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

a = Element('Hydrogen', 'H', '1')

print(a.name, a.number, a.symbol)