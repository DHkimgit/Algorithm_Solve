def DFS_list(vtx, aList, s, visited):
    print(vtx[s], end=' ')
    visited[s] = True
    for v in aList[s]:
        if not visited[v]:
            DFS_list(vtx, aList, v, visited)

vtx = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
aList = [
    [1, 2, 3],       # 노드 '0'
    [0],             # 노드 '1'
    [0, 4],          # 노드 '2'
    [0, 4, 5],       # 노드 '3'
    [2, 3],          # 노드 '4'
    [3, 6, 7, 9],    # 노드 '5'
    [5],             # 노드 '6'
    [5, 8],          # 노드 '7'
    [7],             # 노드 '8'
    [5, 10, 11],     # 노드 '9'
    [9],             # 노드 '10'
    [9]              # 노드 '11'
]

print('DFS(출발: 0) : ', end="")
DFS_list(vtx, aList, 0, [False] * len(vtx))
print()