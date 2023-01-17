# tuple

a = 'harry',
b = ('harry',)
c = ()  #empty tuple
d = 'harry', 'ron'  #PACKING
e = ('hermione')  #string
f = ('harry', 'ron')  #PACKING
print(f[1])
x, y = f  #unpacking
print(y)
g = ('hermione', )
print(g, id(g))
g = g + f  #concatenation
print(g, id(g))




print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))