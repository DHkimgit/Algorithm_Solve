import copy

def find_connected_component(vtx, adj) :
    n = len(vtx)
    visited = [False]*n
    groups = []

    for v in range(n) :
        if visited[v] == False :
            color = bfs_cc(vtx, adj, v, visited)
            groups.append( color )

    return groups

from queue import Queue
def bfs_cc(vtx, adj, s, visited):
    group = [s]
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty() :
        s = Q.get()
        for v in range(len(vtx)) :
            if visited[v]==False and adj[s][v] != 0 :
                Q.put(v)
                visited[v] = True
                group.append(v)
    return group

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

result = []

for i in range(len(edge)):
    for j in range(len(edge[i])):
        if edge[i][j] == 1:
            new_edge = copy.deepcopy(edge)
            new_edge[i][j] = 0
            new_edge[j][i] = 0
            colorGroup = find_connected_component(vtx, new_edge)
            if len(colorGroup) != 1:
                if (vtx[j], vtx[i]) not in result:
                    result.append((vtx[i], vtx[j]))

print("브릿지 개수 = %d " % len(result))
print(result)