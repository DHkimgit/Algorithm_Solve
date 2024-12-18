from queue import Queue

def BFS_AM(vtx, edge, s):
    n = len(vtx)
    visited = [False] * n
    Q = Queue()
    Q.put(s)
    visited[s] = True

    while not Q.empty():
        s = Q.get()
        print(vtx[s], end=' ')
        for v in range(n):
            if edge[s][v] != 0 and not visited[v]:
                Q.put(v)
                visited[v] = True

# 테스트 데이터
vtx = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
edge = [
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 노드 0
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 노드 1
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 노드 2
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # 노드 3
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 노드 4
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0],  # 노드 5
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 노드 6
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],  # 노드 7
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # 노드 8
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],  # 노드 9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 노드 10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]   # 노드 11
]

print('BFS(출발: 0): ', end="")
BFS_AM(vtx, edge, 0)
print()