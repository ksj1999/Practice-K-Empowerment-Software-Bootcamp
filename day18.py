## 클래스 및 함수 선언 부분 ##
from collections import deque


class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


## 전역 변수 선언 부분 ##
G1 = None
queue = deque([])
visited_array = []  # 방문한 정점

## 메인 코드 부분 ##
G1 = Graph(4)
G1.graph[0][2] = 1;
G1.graph[0][3] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1;
G1.graph[2][1] = 1;
G1.graph[2][3] = 1
G1.graph[3][0] = 1;
G1.graph[3][2] = 1

print('## G1 무방향 그래프 ##')
for row in range(4):
    for col in range(4):
        print(G1.graph[row][col], end=' ')
    print()

current = 0  # 시작 정점 A
queue.append(current)  # enqueue
visited_array.append(current)

while len(queue) != 0:
    next = None
    for vertex in range(4):
        if G1.graph[current][vertex] == 1:
            if vertex in visited_array:  # 방문한 적이 있는 정점이면 탈락
                pass
            else:  # 방문한 적이 없으면 다음 정점으로 지정
                next = vertex
                break

    if next != None:  # 다음에 방문할 정점이 있는 경우
        current = next
        queue.append(current)
        visited_array.append(current)
    else:  # 다음에 방문할 정점이 없는 경우
        ##  current = queue.pop(0)  # O(n) Queue 흉내 -> OVERHEAD 발생!!
        current = queue.popleft()  # O(1) 시간 복잡도 나이스

print('방문 순서 -->', end='')
for i in visited_array:
    print(i, end=' --> ')
print("END")
