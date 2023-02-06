def is_stack_full():
    global SIZE, stack, top
    if top >= SIZE - 1:
        return True
    else:
        return False


def is_stack_empty():
    global SIZE, stack, top
    if top == - 1:
        return True
    else:
        return False


def push(data):
    global SIZE, stack, top
    if is_stack_full():
        print("Stack is full!")
        return
    top = top + 1
    stack[top] = data


def pop():
    global SIZE, stack, top
    if is_stack_empty():
        print("Stack is empty~")
        return
    temp = stack[top]
    stack[top] = None
    top = top - 1
    return temp


def peek():
    global SIZE, stack, top
    if is_stack_empty():
        print("Stack is empty~")
        return None
    return stack[top]


SIZE = int(input("Stack Size : "))
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":

    while True:
        menu = input("Insert(I)/Extract(E)/Verify(V)/Exit(X) : ")

        if menu == 'X' or menu == 'x':
            break
        elif menu == 'I' or menu == 'i':
            data = input("Input Data : ")
            push(data)
            print("Stack Status : ", stack)
        elif menu == 'E' or menu == 'e':
            data = pop()
            print("Extracted Data : ", data)
            print("Stack Status : ", stack)
        elif menu == 'V' or menu == 'v':
            data = peek()
            print("Check Data : ", data)
            print("Stack Status : ", stack)
        else:
            print("Input Mismatch")

    print("Program End")
