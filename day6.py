g = 1  # global

def print_global():
    # g = 1  # local
    print(g)

def change_print_global():
    global g
    print(g)
    g = 2
    print(g)


change_print_global()
print_global()
print(g)
print(globals())
print(__name__)
