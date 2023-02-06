import math
import random

class Node:
    def __init__(self):
        self.data = None
        self.link = None



def print_stores(start):

    current = start
    if current == None:
        return

    while current.link != head :
        current = current.link
        x, y = current.data[1:]
        print(current.data[0], '편의점, 거리: ', math.sqrt(x*x + y*y))
    print()

def make_store_list(store):
    global memory, head, current, pre

    node = Node()
    node.data = store
    memory.append(node)

    if head == None:
        head = node
        node.link = head
        return

    node_x, node_y = node.data[1:]
    node_dist = math.sqrt(node_x*node_x + node_y*node_y)
    head_x, head_y = head.data[1:]
    head_dist = math.sqrt(head_x*head_x + head_y*head_y)

    if head_dist > node_dist:
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        curr_x, curr_y = current.data[1:]
        curr_dist = math.sqrt(curr_x*curr_x + curr_y*curr_y)
        if curr_dist > node_dist:
            pre.link = node
            node.link = current
            return

    current.link = node
    node.link = head


memory = []
head, current, pre = None, None, None

if __name__ == "__main__":

    store_array = []
    store_name = 'A'
    for _ in range(10):
        store = (store_name, random.randint(1, 100), random.randint(1, 100))
        store_array.append(store)
        store_name = chr(ord(store_name)+1)

    for store in store_array:
        make_store_list(store)

    print_stores(head)

