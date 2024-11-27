parent = []
set_size = 0

def init_set(nSets) :
    global set_size, parent 
    set_size = nSets;
    for i in range(nSets):
        parent.append(-1)

def find(id) :
    while (parent[id] >= 0) :
        id = parent[id];
    return id;

def union(s1, s2) :
    global set_size
    parent[s1] = s2;
    set_size = set_size - 1;

def MSTKruskal(vertex, adj):
    weight_sum = 0
    vsize = len(vertex)
    init_set(vsize)
    eList = []

    for i in range(vsize-1):
        for j in range(i+1, vsize):
            if adj[i][j] is not None:
                eList.append((i, j, adj[i][j]))

    eList.sort(key=lambda e: e[2], reverse=True)

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

    print(f"\nMST의 총 가중치: {weight_sum}")

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

MSTKruskal(vtx, edge)