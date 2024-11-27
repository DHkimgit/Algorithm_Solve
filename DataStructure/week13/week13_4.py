INF = 999
def choose_vertex(dist, found) :
    min = INF
    minpos = -1

    for i in range(len(dist)) :
        if dist[i]< min and found[i]==False :
            min = dist[i]
            minpos = i
    return minpos;

def shortest_path_dijkstra(vertex, adj, start):
    vsize = len(vertex)
    dist = list(adj[start])
    path = [start] * vsize
    found = [False] * vsize

    found[start] = True
    dist[start] = 0

    for i in range(vsize):
        print("Step%2d: " % (i + 1), dist)
        u = choose_vertex(dist, found)
        found[u] = True

        for w in range(vsize):
            if not found[w]:
                if dist[u] + adj[u][w] < dist[w]:
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u

    return dist, path

        

vertex = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
weight = [
    [INF,  10,  15,  INF, INF, INF, INF, INF,  30],  # 0번 노드
    [10,  INF,  25,  INF, INF, INF,  40, INF, INF],  # 1번 노드
    [15,  25,  INF,  35, INF, INF, INF, INF,  20],  # 2번 노드
    [INF, INF,  35,  INF,  50,  45, INF, INF, INF],  # 3번 노드
    [INF, INF, INF,  50,  INF, INF,  55, INF, INF],  # 4번 노드
    [INF, INF, INF,  45, INF,  INF, INF,  60, INF],  # 5번 노드
    [INF,  40, INF, INF,  55, INF,  INF, INF, INF],  # 6번 노드
    [INF, INF, INF, INF, INF,  60, INF,  INF,  25],  # 7번 노드
    [30,  INF,  20, INF, INF, INF, INF,  25,  INF]   # 8번 노드
] 

start = 0
dist, path = shortest_path_dijkstra(vertex, weight, start)

for end in range(len(vertex)):
    if end != start:
        print("[최단경로: %s->%s] %s" % (vertex[start], vertex[end], vertex[end]), end='')
        current = end
        total_weight = dist[end]
        while path[current] != start:
            print(" <- %s" % vertex[path[current]], end='')
            current = path[current]
        print(" <- %s [가중치 합: %d]" % (vertex[path[current]], total_weight))
