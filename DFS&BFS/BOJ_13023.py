N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph: list, v: int, visited: list, depth: int):
    if depth >= 4:
        print(1)
        exit()
    
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, depth + 1)
            visited[i] = False
    
for i in range(N):
    visted = [False] * N
    dfs(graph, i, visted, 0)

print(0)
