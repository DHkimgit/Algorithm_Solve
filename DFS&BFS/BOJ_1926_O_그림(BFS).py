from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

results = [0]
vis = [[0]*m for _ in range(n)]

def bfs(x, y):
    if graph[x][y] == 0 or vis[x][y] == 1:
        return 0
    
    area = 0

    queue = deque()
    queue.append((x, y))
    vis[x][y] = 1

    while queue:
        
        x, y = queue.popleft()
        area += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if graph[nx][ny] == 0 or vis[nx][ny] == 1:
                continue
            
            if graph[nx][ny] == 1:

                queue.append((nx, ny))
                vis[nx][ny] = 1

    return area

for i in range(n):
    for j in range(m):
        area = bfs(i, j)
        if  area != 0:
            results.append(area)
        
print(len(results) - 1)
print(max(results))
