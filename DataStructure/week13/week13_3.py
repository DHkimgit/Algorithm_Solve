INF = 9999

def getMinVertex(dist, selected):
    minv = 0
    mindist = INF
    for v in range(len(dist)):
        if not selected[v] and dist[v] < mindist:
            mindist = dist[v]
            minv = v
    return minv

def MSTPrim(vertex, adj):
    weight_sum = 0 
    vsize = len(vertex)
    dist = [INF] * vsize
    selected = [False] * vsize
    dist[0] = 0

    for i in range(vsize):
        u = getMinVertex(dist, selected)
        selected[u] = True
        print(vertex[u], end=' ')

        weight_sum += dist[u]

        for v in range(vsize):
            if adj[u][v] is not None:
                if not selected[v] and adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]
    print()
    
    print(f"Prim의 MST 총 가중치: {weight_sum}")

vtx = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
edge = [
    [None, 15, 28, 22, None, None, None, None, None, None, None, None],
    [15, None, None, None, None, None, None, None, None, None, None, None],
    [28, None, None, None, 12, None, None, None, None, None, None, None],
    [22, None, None, None, 25, 18, None, None, None, None, None, None],
    [None, None, 12, 25, None, None, None, None, None, None, None, None],
    [None, None, None, 18, None, None, 20, 30, None, 27, None, None],
    [None, None, None, None, None, 20, None, None, None, None, None, None],
    [None, None, None, None, None, 30, None, None, 19, None, None, None],
    [None, None, None, None, None, None, None, 19, None, None, None, None],
    [None, None, None, None, None, 27, None, None, None, None, 13, 29],
    [None, None, None, None, None, None, None, None, None, 13, None, None],
    [None, None, None, None, None, None, None, None, None, 29, None, None]
]

MSTPrim(vtx, edge)
