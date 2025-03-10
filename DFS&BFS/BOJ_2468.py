from collections import deque
N = int(input())

graph = []
max_height = 0

for i in range(N):
    graph.append(list(map(int, input().split())))
    if max(graph[i]) >= max_height:
        max_height = max(graph[i])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(graph: list, visited: list, x: int, y: int, rainfall: int):
    if visited[y][x] == True or graph[y][x] <= rainfall:
        return 0
    
    queue = deque()
    
    queue.append((x, y))
    visited[y][x] = True
    area = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= N or ny >= N or nx < 0 or ny < 0:
                continue
            if visited[ny][nx] == True or graph[ny][nx] <= rainfall:
                continue
            else:
                queue.append((nx, ny))
                visited[ny][nx] = True
                area += 1
    return area

result = 0

for rainfall in range(0, max_height):
    visited = [[False for _ in range(N)] for _ in range(N)]
    safe_zone = 0
    for i in range(N):
        for j in range(N):
            if bfs(graph, visited, i, j, rainfall) > 0:
                safe_zone += 1
    
    if safe_zone >= result:
        result = safe_zone

print(result)
