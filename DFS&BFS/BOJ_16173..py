from collections import deque

N = int(input())

graph = []

dx = [0, 1]
dy = [1, 0]

for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)]

queue = deque()

queue.append((0, 0))
visited[0][0] = True

while(queue):
    x, y = queue.popleft()

    val = graph[x][y]

    for i in range(2):
        nx = x + dx[i] * val
        ny = y + dy[i] * val

        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if visited[nx][ny]:
            continue

        queue.append((nx, ny))
        visited[nx][ny] = True

if(visited[N-1][N-1]):
    print("HaruHaru")
else:
    print("Hing")