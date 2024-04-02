from collections import deque
answer = []

T = int(input())


def bfs(x, y):
    if cabmap[x][y] == 0 or visited[x][y] == 1:
        return 0
    
    area = 0

    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        area += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            
            if cabmap[nx][ny] == 0 or visited[nx][ny] == 1:
                continue
            
            if cabmap[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = 1
    return area

for _ in range(T):
    M, N, K= map(int, input().split())
    cabmap = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    testresult = []

    for i in range(K):
        x, y = map(int, input().split())
        cabmap[y][x] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(N):
        for j in range(M):
            chk = bfs(i, j)
            if chk != 0:
                testresult.append(chk)
    
    answer.append(len(testresult))

for ans in answer:
    print(ans)