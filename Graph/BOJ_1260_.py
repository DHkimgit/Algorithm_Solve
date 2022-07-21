from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
dfs_result = []
bfs_result = []
for i in range(M):
    a, b = map(int, input().split())
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * 9
dfs(graph, V, visited)
visited = [False] * 9
print('\n')
bfs(graph, V, visited)
