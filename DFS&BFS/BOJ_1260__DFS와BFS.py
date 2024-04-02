from collections import deque
N, M, V = map(int, input().split())

graph = [[] for x in range(N + 1)]
visited_dfs = [False for x in range(N + 1)]
visited_bfs = [False for x in range(N + 1)]

dfs_log = []
bfs_log = []
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N + 1):
    graph[i].sort()

def dfs(graph, v, visited):

    visited[v] = True
    dfs_log.append(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, V, visited_dfs)

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        vertax = queue.popleft()
        bfs_log.append(vertax)

        for i in graph[vertax]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, V, visited_bfs)

for i in range(len(dfs_log)):
    if i == len(dfs_log) - 1:
        print(dfs_log[i])
    else:
        print(dfs_log[i], end=' ')
for i in range(len(bfs_log)):
    if i == len(bfs_log) - 1:
        print(bfs_log[i])
    else:
     print(bfs_log[i], end=' ')