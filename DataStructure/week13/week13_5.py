parent = []
set_size = 0

def init_set(nSets):
    global set_size, parent
    set_size = nSets
    for i in range(nSets):
        parent.append(-1)

def find(id):
    while parent[id] >= 0:
        id = parent[id]
    return id

def union(s1, s2):
    global set_size
    parent[s1] = s2
    set_size -= 1

def MSTKruskal(vertex, adj):
    weight_sum = 0
    vsize = len(vertex)
    init_set(vsize)
    eList = []

    for i in range(vsize - 1):
        for j in range(i + 1, vsize):
            if adj[i][j] is not None:
                eList.append((i, j, adj[i][j]))

    eList.sort(key=lambda e: e[2], reverse=False)

    edgeAccepted = 0
    while edgeAccepted < vsize - 1:
        e = eList.pop(-1)
        uset = find(e[0])
        vset = find(e[1])

        if uset != vset:
            print("간선 추가 : (%s, %s, %d)" %
                  (vertex[e[0]], vertex[e[1]], e[2]))
            union(uset, vset)
            weight_sum += e[2]
            edgeAccepted += 1

    print(f"\nMaximumSpanningTree 의 총 가중치: {weight_sum}")


vertex = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
weight = [
    [None,  10,  15,  None, None, None, None, None,  30],  # 0번 노드
    [10,  None,  25,  None, None, None,  40, None, None],  # 1번 노드
    [15,  25,  None,  35, None, None, None, None,  20],  # 2번 노드
    [None, None,  35,  None,  50,  45, None, None, None],  # 3번 노드
    [None, None, None,  50,  None, None,  55, None, None],  # 4번 노드
    [None, None, None,  45, None,  None, None,  60, None],  # 5번 노드
    [None,  40, None, None,  55, None,  None, None, None],  # 6번 노드
    [None, None, None, None, None,  60, None,  None,  25],  # 7번 노드
    [30,  None,  20, None, None, None, None,  25,  None]   # 8번 노드
] 

MSTKruskal(vertex, weight)
