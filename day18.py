## 클래스 및 함수 선언 부분 ##
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def make_graph(g):
    for x in range(g.SIZE):
        print("%9s" % store_array[x][0], end=' ')
    print()
    for y in range(g.SIZE):
        print("%9s" % store_array[y][0], end=' ')
        for z in range(g.SIZE):
            print("%8d" % g.graph[y][z], end=' ')
        print()


## 전역 변수 선언 부분 ##
G1 = None
store_array = [['GS25', 30], ['CU', 60], ['Seven11', 10], ['MiniStop', 90], ['Emart24', 40]]
# GS25, CU, Seven11, MiniStop, Emart24 = 0, 1, 2, 3, 4
SIZE = 5
G1 = Graph(SIZE)
stack = []
visited_array = []

G1.graph[0][1] = 1; G1.graph[0][2] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1; G1.graph[1][3] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][1] = 1; G1.graph[3][2] = 1
G1.graph[4][3] = 1

print("##편의점 그래프##")
make_graph(G1)

# current = 0
# max_store = current
#
# while len(stack) != 0:
#     next = None
#     for vertex in range(5):
#         if G1.graph[current][vertex] == 1:
#             if vertex in visited_array:  # 방문한 적이 있는 정점이면 탈락
#                 pass
#             else:  # 방문한 적이 없으면 다음 정점으로 지정
#                 next = vertex
#                 break
#
#     if next != None:  # 다음에 방문할 정점이 있는 경우
#         current = next
#         stack.append(current)
#         visited_array.append(current)
#     else:  # 다음에 방문할 정점이 없는 경우
#         current = stack.pop()