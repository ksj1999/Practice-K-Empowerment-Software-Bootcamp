class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


def print_nodes(start):
	@@ -53,30 +10,96 @@ def print_nodes(start):
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()


def insert_nodes(find_data, insert_data):
    global head, current, pre
    if head.data == find_data:
        node = Node(insert_data)
        node.link = head
        head = node
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node(insert_data)
            node.link = current
            pre.link = node
            return

    node = Node(insert_data)
    current.link = node


def delete_nodes(delete_data):
    global head, current, pre

    if head.data == delete_data:
        print('첫 번째 노드 삭제 완료')
        current = head
        head = head.link
        del current
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == delete_data:
            print('중간 노드 삭제 완료')
            pre.link = current.link
            del current
            return

    print('삭제할 노드를 찾지 못함')


def find_nodes(find_data):
    global head, current, pre

    current = head
    if current.data == find_data:
        return current

    while current.link != None:
        current = current.link
        if current.data == find_data:
            return current

    return Node(None)


head, current, pre = None, None, None
data_array = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]


if __name__ == "__main__":
    node = Node(data_array[0])
    head = node

    for data in data_array[1:]:
        pre = node
        node = Node(data)
        pre.link = node

    print_nodes(head)
    insert_nodes("피카츄", "잠만보")
    print_nodes(head)
    insert_nodes("파이리", "어니부기")
    print_nodes(head)
    insert_nodes("성윤모", "거북왕")
    print_nodes(head)
    delete_nodes("잠만보")
    print_nodes(head)
    delete_nodes("어니부기")
    print_nodes(head)
    delete_nodes("강찬석")
    print_nodes(head)
    print(find_nodes("파이리").data)
    print(find_nodes("박민석").data)