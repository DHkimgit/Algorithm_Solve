from collections import deque

N, M = map(int, input().split())

graph = []
visited = [[False for _ in range(N)] for _ in range(M)]

for i in range(M):
    graph.append(list(str(input())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result_B = 0
result_W = 0

def bfs(x, y):
    if visited[x][y]:
        return
    global result_W, result_B

    if graph[x][y] == 'W':
        target = 'W'
    else:
        target = 'B'

    area = 0

    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        area += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= M or ny >= N or nx < 0 or ny < 0:
                continue
            if visited[nx][ny] or graph[nx][ny] != target:
                continue
            else:
                queue.append((nx, ny))
                visited[nx][ny] = True

    if target == 'W':
        result_W += area * area
    else:
        result_B += area * area

for i in range(M):
    for j in range(N):
        bfs(i, j)

print(result_W, end=' ')
print(result_B)