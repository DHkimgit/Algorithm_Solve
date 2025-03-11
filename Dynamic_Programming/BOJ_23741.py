import sys
input = sys.stdin.readline

N, M, X, Y = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [[False] * (Y + 1) for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = set()

def dfs(point, move):
    visited[point][move] = True
    if move == Y:
        result.add(point)
        return
    else:
        for i in graph[point]:
            if not visited[i][move + 1]:
                dfs(i, move + 1)

dfs(X, 0)
    
if not result:
    print(-1)
else:
    print(*sorted(list(result)))

# queue = deque()
# queue.append((X, 0))

# while queue:
#     point, move = queue.popleft()
#     visited[point][move] = True
#     if move >= Y + 1:
#         break
#     if move == Y:
#         result.add(point)
#     for i in graph[point]:
#         if not visited[i][move + 1]:
#             queue.append((i, move + 1))