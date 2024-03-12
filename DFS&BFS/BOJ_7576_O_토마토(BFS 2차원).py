from collections import deque

M, N = map(int, input().split())

graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    graph.append(list(map(int, input().split())))

vis = [[0]*M for _ in range(N)]

def bfs():
    queue = deque()

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append((i, j))
                vis[i][j] = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            
            if graph[nx][ny] == -1 or vis[nx][ny] == 1:
                continue
            
            if graph[nx][ny] >= 0 :
                queue.append((nx, ny))
                vis[nx][ny] = 1
                graph[nx][ny] = graph[x][y] + 1

k = bfs()
max_date = 0
fail_to_ripe = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            fail_to_ripe = 1
            break
        
        if graph[i][j] > max_date:
            max_date = graph[i][j]

if fail_to_ripe == 1:
    print(-1)
else:
    print(max_date - 1)
