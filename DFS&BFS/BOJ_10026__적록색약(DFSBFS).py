from collections import deque
N = int(input())

graph = []

for _ in range(N):
    graph.append(input())

visited_n = [[0]*N for x in range(N)]
visited_e = [[0]*N for x in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs_n(x: int, y: int, color: str):
    if visited_n[x][y] == 1:
        return 0
    area = 1
    queue = deque()
    queue.append((x, y))
    visited_n[x][y] = 1

    while queue:
        x, y = queue.popleft()
        visited_n[x][y] = 1
        area += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            
            if visited_n[nx][ny] == 1 or graph[nx][ny] != color:
                continue
            
            if graph[nx][ny] == color:
                visited_n[nx][ny] = 1
                queue.append((nx, ny))

    return area

def bfs_e(x: int, y: int, color: str):
    if color == 'B':
        if visited_e[x][y] == 1:
            return 0
        area = 1
        queue = deque()
        queue.append((x, y))
        visited_e[x][y] = 1

        while queue:
            x, y = queue.popleft()
            visited_e[x][y] = 1
            area += 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                
                if visited_e[nx][ny] == 1 or graph[nx][ny] != color:
                    continue
                
                if graph[nx][ny] == color:
                    visited_e[nx][ny] = 1
                    queue.append((nx, ny))

        return area
    
    else:
        if visited_e[x][y] == 1:
            return 0
        area = 1
        queue = deque()
        queue.append((x, y))
        visited_e[x][y] = 1

        while queue:
            x, y = queue.popleft()
            visited_e[x][y] = 1
            area += 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                
                if visited_e[nx][ny] == 1 or graph[nx][ny] == 'B':
                    continue
                
                else:
                    visited_e[nx][ny] = 1
                    queue.append((nx, ny))

        return area

result_n = []
result_e = []
for i in range(N):
    for j in range(N):
        color = graph[i][j]
        tmp_n = bfs_n(i, j, color)
        tmp_e = bfs_e(i, j, color)
        if tmp_n > 0:
            result_n.append((tmp_n, color))
        if tmp_e > 0:
            result_e.append((tmp_e, color))

print(len(result_n), len(result_e))
